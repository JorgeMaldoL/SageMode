from rich import print # to be able to style and color the terminal outputs
import typer #typer library that helps build CLI apps using python functions 
from typing import Optional #allows for function arguments to be optional
from pathlib import Path # A way for python to handle file and folder paths  

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

@app.command()
def scan(path: Path = typer.Argument(..., help="The file or Folder your scanning"), # path: file or folder path, pathlib.Path object
         recursive: bool = typer.Option(False, "--recursive", "-r", help="Recusive scan on folders"),
         summarize: bool = typer.Option(False, "--summarize", "-s", help="Summarize the contents"), 
         ):
    #Use to scan files and folders and then passes the scanned contents to Sage
    print(f"[green]Scanning {path}...[/]")

if __name__ == "__main__":
    app()