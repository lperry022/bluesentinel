import typer

# importing a library for rich text formatting
from rich.console import Console

# console from the rich library allows for printing text in colours and different styles - make it pretty <3
from . import __version__

# importing the version number from the package
from .logger import log_info, log_error

# Import the network command group
from .commands.network import network_app

app = typer.Typer(help="Security Toolkit")
# app is like the main controller
# help is the command somone can run to see how to use the tool

console = Console()
# initializing the console object


@app.command()
# tells the Typer that the following function is a command
def hello(name: str = typer.Argument("world")):
    """Say hello (first command)."""
    try:
        console.print(f"[bold green]Hello, {name}![/]")
        log_info(f"Greeted {name}")
    except Exception as e:
        log_error(f"Failed to greet {name}: {e}")


@app.command()
def logs():
    """
    Display recent log entries.
    Simply reads the last few lines of the log file.
    """
    console.print("[bold cyan]Recent Logs:[/]")
    try:
        with open("logs/cli.log", "r") as log_file:
            for line in log_file.readlines()[-10:]:  # show last 10 lines
                console.print(line.strip())
    except FileNotFoundError:
        console.print("[red]No logs found yet.[/]")


# the command is called hello - i could call it harry if i really wanted to
# it takes one argument called name - if no name is provided it defaults to "world"


@app.command()
def version(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Show more detailed output."
    ),
):
    """Show the current version of BlueTeam Sentinel."""
    if verbose:
        console.print("[yellow]Verbose mode is ON[/]")
        console.print("[dim]Preparing version output…[/]")
    console.print(f"[bold cyan]BlueTeam Sentinel v{__version__}[/]")


# Add the new "network" command group
# This is what allows `python -m cyber_cli network info` to work
app.add_typer(network_app, name="network")


def main(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Show more detailed output."
    ),
):
    if verbose:
        console.print("[yellow]Verbose mode is ON[/]")
    app()


# entry point for the CLI application
