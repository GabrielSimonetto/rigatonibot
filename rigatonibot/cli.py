import click
from pathlib import Path
import requests
import send

@click.command()
@click.argument('filename', type=click.Path(exists=True, readable=True), nargs=1)
def cli(filename):
    """Usage:
    run `python rigatonibot/cli.py <file>`, 
    it will create and output via terminal your `paste.rs` link"""

    print(send.filepath_to_paste(filename))

if __name__ == '__main__':
    cli()

