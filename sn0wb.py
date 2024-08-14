import click
from rich import print
from rich.panel import Panel
import src.command as command
import src.ai as ai


@click.command()
@click.option("-u", help="Target URL.")
def recon(u):
    command.recon(u)
    
 

@click.command()
@click.option("-d", help="Directory to scan.")
def report(d):
    ai.report(d)



@click.group()
def cli():
    pass

cli.add_command(recon)
cli.add_command(report)

if __name__ == '__main__':
    cli()