from rich import print # to be able to style and color the terminal outputs
import typer #typer library that helps build CLI apps using python functions 
from typing import Optional, List #type hintting for optional and lists
from pathlib import Path # A way for python to handle file and folder paths  
from enum import Enum #prevents typos and gives you fixed choices to pick
import sys
from models.model_downloader import snapshot_download

app = typer.Typer()(
    help ="This is SageModes CLI for using AI models. You can ask the AI questions and manage your chat sessions. Hope you enjoy :)",
    no_args_is_help = True
)

class EraseMode(str, Enum): #use for type safty 
    SOFT = 'soft'
    HARD = 'hard'

#makes sure that the user has llama is built and builds it if it doesn't 
def working_llama_cli():
    llama_cli = Path(__file__).resolve().parents[1] / "llama.cpp" / "build" / "bin" / "llama-cli"
    if not llama_cli.exists():
        print("[yellow]:D Building llama.cpp ... [/]")
        from scripts.build_llama import build_llama_cpp
        try:
            build_llama_cpp()
        except Exception as error:
            print (f"[red] Error with Building llama.cpp {error} :(")
            sys.exit(1) #exit with error code 

@app.command()
def ask(    
    prompt: str = typer.Argument(..., help="Ask the question to the AI"),
    model: str = typer.Option(snapshot_download.repo_id, "--model", "-m", help="The model that is being used"),
    tempature: float = typer.Option(0.7, "--temperature", "-t", help="The sampling temp of 0.0 to 1.0"),
):
    #Ask's the prompt to the AI
    try:
        print(f"[yellow]Model: {model}[/] [dim yellow] (temp= {tempature})[/]")
        print(f"[bold green]You: [/] {prompt}")
    except Exception as error:
        print(f"[red] error with processing question: {error}")


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