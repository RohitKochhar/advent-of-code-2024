from .Solver import Solver

import click
import sys


@click.group()
def cli():
    """AOC CLI"""
    pass

@cli.command()
@click.argument("day")
def solve(day: int) -> None:
    """Solves AOC for the given day"""
    print(f"Running Advent of Code for day {day}")
    print(f"- - - - - - - - - - - - - - - - - - ")
    print("Part 1:")

    try:
        Solver(day)
    except RuntimeError:
        print("Exiting without solution")
        sys.exit(1)

    print("--------------")
    print("Part 2:")

    try:
        Solver(day, part_1=False)
    except RuntimeError as e:
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    cli()
