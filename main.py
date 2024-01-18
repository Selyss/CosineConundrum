import click

@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True), required=True)
def generate(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    if len(lines) != 0:
        click.echo("Error: File should be blank.")
        return

if __name__ == '__main__':
    generate()

