import typer
from rich.console import Console
import socket

# Create a Typer "app" specifically for network-related commands.
# This allows you to group commands under: cyber-cli network <command>
network_app = typer.Typer(help="Commands related to networking information.")

# Console object from Rich for colourful printing.
console = Console()


@network_app.command("info")
def show_network_info():
    # Show basic network information about the machine.
    # This is a simple, beginner-friendly command that demonstrates
    # how to gather system/network details using Python.
    try:
        # Get the hostname (computer name)
        hostname = socket.gethostname()

        # Get the local IP address associated with the hostname
        local_ip = socket.gethostbyname(hostname)

        console.print("[bold cyan]Network Information[/]")
        console.print(f"[green]Hostname:[/] {hostname}")
        console.print(f"[green]Local IP Address:[/] {local_ip}")

    except Exception as e:
        # If anything goes wrong, show a user-friendly error message
        console.print(f"[red]Error retrieving network info: {e}[/]")
