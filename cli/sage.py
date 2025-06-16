from rich import print
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def ask(prompt: str):
    #Question
    print(f"[bold red]You asked: [/] {prompt} ")

@app.command()
def gui():
    #opens up gui
    print(f"[green] Loading GUI...[/]")

@app.command()
def end():
    #ends the session
    print(f"[yellow] Ending...[/]")

@app.command()
def erase(id: Optional[str] = typer.Option(None, help="Delete session by its ID "),
                  before: Optional[str] = typer.Option(None, help="Delete all sessions before date: "),
                  after: Optional[str] = typer.Option(None, help="Delete all sessions after date: "),
                  range: Optional[list[str]] = typer.Option(None, help="Delete all sessions in the range of: "),
                  all: bool = typer.Option(False, help="Delete all of the sessions."),
                  force: bool = typer.Option(False, help="Permanently delete instead of soft delete."),
                  trash_list: bool = typer.Option(False, help="Show items in trash") 
                  ):
    #reset chats history, by its ID, by time, or just in all. Offers soft delete after 30 days will give it full hard delete. Or you can do a force hard delete
    print("[yellow] Reset history activated...[/]")

if __name__ == "__main__":
    app()