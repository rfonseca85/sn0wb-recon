import yaml
import subprocess
import os
import re
from tqdm import tqdm
from rich import print
from rich.panel import Panel
import threading
import time

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

    command_list = command.replace("{target}", target).split() 

    with open(result_file, 'w') as file:
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
        
        with tqdm(desc="Progress", ncols=100, unit="line") as pbar:
            for line in process.stdout:
                file.write(line)
                file.flush()  # Ensure the buffer is written to the file immediately
                pbar.update(1)  # Update progress bar for each line read
        
        stderr = process.stderr.read()
        if stderr:
            file.write("\nErrors:\n")
            file.write(stderr)
        
        process.wait()
    
    print(f"[italic purple] --> Command {real_command} completed. Output saved to {result_file}[/italic purple]")

def recon(target):
    config_data = load_config("./config.yaml")
    threadsRecon = []
    
    for command in config_data['commands']:
        
        t = threading.Thread(target=run_command, args=("recon", command['name'], command['command'], target))
        threadsRecon.append(t)
        t.start()
        time.sleep(3)  # Wait for 5 seconds before starting the next command

    for t in threadsRecon:
        t.join()
        