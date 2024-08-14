import click
import src.command as command
import src.ai as ai


@click.command()
@click.option("-u", help="Target URL.")
def recon(u):
    command.exec(u , 'recon')
    

@click.command()
@click.option("-u", help="Target URL.")
def scan(u):
    command.exec(u , 'scan')
 

@click.command()
@click.option("-r", help="Report type (recon, scan).")
@click.option("-d", help="Directory to scan.")
def report(r,d):
    ai.report(r,d)



@click.group()
def cli():
    pass

cli.add_command(recon)
cli.add_command(scan)
cli.add_command(report)

if __name__ == '__main__':
    cli()