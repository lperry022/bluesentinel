import typer

# importing a library for rich text formatting
from rich.console import Console

# console from the rich library allows for printing text in colours and different styles - make it pretty <3

app = typer.Typer(help="Security Toolkit")
# app is like the main controller
# help is the command somone can run to see how to use the tool

console = Console()
# initializing the console object


@app.command()
# tells the Typer that the following function is a command
def hello(name: str = typer.Argument("world")):
    """Say hello (first command)."""
    console.print(f"[bold green]Hello, {name}![/]")


# the command is called hello - i could call it harry if i really wanted to
# it takes one argument called name - if no name is provided it defaults to "world"


def main():
    app()


# entry point for the CLI application
