import logging
from rich.console import Console

# coloured console output

console = Console()

# Setup how the logs will look
logging.basicConfig(
    filename="logs/cli.log",  # Save logs here
    level=logging.INFO,  # Default level (INFO = normal messages)
    format="%(asctime)s — %(levelname)s — %(message)s",  # Timestamp + level + message
)


def log_info(message: str):
    """Write normal events to the log and show them in green"""
    logging.info(message)
    console.print(f"[green]INFO:[/] {message}")


def log_error(message: str):
    """Write errors to the log and show them in red"""
    logging.error(message)
    console.print(f"[red]ERROR:[/] {message}")
