import click
import re
import json
import random

# LaTeX matching for primary stuff
sine = r"\\sin\\theta"
sinesqrd = "\\sin^2\\theta"
consine = "\\cos\\theta"
consinesqrd = "\\cos^2\\theta"
tangent = "\\tangent\\theta"
tangentsqrd = "\\tangent^2\\theta"


def random_sine():
    # open config.json
    with open("config.json", "r") as file:
        data = json.load(file)

    rand = random.choice(data["sine"])
    return rand


def random_sinesqrd():
    # open config.json
    with open("config.json", "r") as file:
        data = json.load(file)

    rand = random.choice(data["sinesquared"])
    return rand


def expand(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

        sines = re.finditer(sine, lines)
        for s in sines:
            lines[s.start()] = random_sine()

    with open(input_file, "w") as file:
        file.writelines(lines)

    click.echo("Success: Equations expanded.")


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
    with open(input_file, "w") as file:
        file.write("\\[{\\sin^2\\theta}={\\sin^2\\theta}\\]")

    click.echo("Success: File modified.")
    expand(input_file)


if __name__ == "__main__":
    main()
