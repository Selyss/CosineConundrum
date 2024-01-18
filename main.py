import click

@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True), required=True)
def main(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    if len(lines) != 0:
        click.echo("Error: File should be blank.")
        return
    
    click.echo("Success: Valid file.")
    with open(input_file, 'w') as file:
        file.write("\\[{\\sin\\theta}\\]") 

    click.echo("Success: File modified.")   



if __name__ == '__main__':
    main()

