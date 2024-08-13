import click
import yaml
import subprocess
import threading
from rich import print
from rich.panel import Panel
import os
import re
import aiReport as aiReport

def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9]', '_', filename)

def run_command(command, args, name, target):
    sanitized_name = sanitize_filename(name)
    directory = f"./{sanitized_name}"
    os.makedirs(directory, exist_ok=True)
    result_file = os.path.join(directory, f"{command}_{sanitized_name}.txt")
    
    with open(result_file, 'w') as file:
        process = subprocess.Popen([command] + args + [target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        file.write(stdout.decode(errors='replace'))
        if stderr:
            file.write("\nErrors:\n")
            file.write(stderr.decode(errors='replace'))
    
    print(Panel(f"Command [italic red]{command} {target}[/italic red] finished. Output saved to {result_file}"))

@click.command()
@click.option("-u", help="Target URL.")
@click.option("-n", help="Target name.")
def recon(u, n):
    target = u
    target_name = n
    
    config_data = load_config("config.yaml")
    threads = []
    
    for command in config_data['commands']:
        t = threading.Thread(target=run_command, args=(command['name'], command.get('args', []), target_name, target))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

@click.command()
@click.option("-o", help="Output file.")
def report(o):
    print(Panel(f"Generating report [italic red]{o}[/italic red]"))
    aiReport.main(o)

@click.group()
def cli():
    pass

cli.add_command(recon)
cli.add_command(report)

if __name__ == '__main__':
    cli()