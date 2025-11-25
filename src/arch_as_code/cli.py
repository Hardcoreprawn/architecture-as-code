"""Command-line interface for Architecture as Code."""

import typer
from rich.console import Console

app = typer.Typer(
    name="arch",
    help="Architecture as Code - Manage enterprise architecture programmatically",
    add_completion=False,
)
console = Console()


@app.command()
def discover(
    subscription: str = typer.Option(..., "--subscription", "-s", help="Azure subscription ID"),
    output: str = typer.Option("./output", "--output", "-o", help="Output directory"),
) -> None:
    """Discover current architecture from Azure subscriptions.
    
    Queries Azure Resource Graph to find resources and groups them
    by application for architecture documentation.
    """
    console.print(f"[bold]Discovering resources in subscription:[/bold] {subscription}")
    console.print(f"[bold]Output directory:[/bold] {output}")
    console.print("\n[yellow]⚠️  Not implemented yet - see issue #1[/yellow]")


@app.command()
def version() -> None:
    """Show version information."""
    from arch_as_code import __version__
    
    console.print(f"Architecture as Code v{__version__}")


if __name__ == "__main__":
    app()
