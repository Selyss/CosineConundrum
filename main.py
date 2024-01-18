import click
import json
import random
import math
import numpy as np
import latexify


@latexify.function
def generate():
    pass


@click.command()
@click.argument(
    "input_file", type=click.Path(exists=True, readable=True), required=True
)
def main(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    if len(lines) != 0:
        click.echo("Error: File should be blank.")
        return

    click.echo("Success: Valid file.")
    # TODO:
    click.echo(f"Success: File '{input_file}' modified.")


if __name__ == "__main__":
    main()
