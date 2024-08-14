import yaml
import subprocess
import os
from tqdm import tqdm
from rich import print
from rich.panel import Panel
import threading

def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def run_command(phase, name, command, target):
    target_sanitized = target.replace("http://", "").replace("https://", "").replace("/", "_").replace(":", "_").replace(".", "_")
    directory = f"results/{target_sanitized}/{phase}"
    os.makedirs(directory, exist_ok=True)
    result_file = os.path.join(directory, f"{name}.txt")

    real_command = command.replace("{target}", target)
    print(Panel(f"Command [italic red]{real_command}[/italic red] started. Output will be saved to {result_file}"))

    process = subprocess.Popen(real_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    with open(result_file, 'w') as file:
        with tqdm(desc=f"Progress on {name}", ncols=100, unit=" lines") as pbar:
            for line in process.stdout:
                file.write(line)
                file.flush()  # Ensure the buffer is written to the file immediately
                pbar.update(1)  # Update progress bar for each line read
        
        stderr = process.stderr.read()
        if stderr:
            file.write("\nErrors:\n")
            file.write(stderr)
        
        process.wait()
    
    print(f"[italic purple] --> Command {name} completed. Output saved to {result_file}[/italic purple]")

def exec(target, web_type):
    config_data = load_config(f"./config.yaml")
    selected_commands = []
    
    for command in config_data[web_type]:
        user_input = input(f"Run command {command['name']}? (y/n): ")
        if user_input.lower() == "y":
            selected_commands.append(command)

    threadsRecon = []
    for command in selected_commands:
        t = threading.Thread(target=run_command, args=(web_type, command['name'], command['command'], target))
        threadsRecon.append(t)
        t.start()

    for t in threadsRecon:
        t.join()

