import os
import subprocess
from pathlib import Path

def build_llama_cpp():
    llama_dir = Path(__file__).resolve().parents[1] / "llama.cpp"
    build_dir = llama_dir / "build"
    bin_path = build_dir / "bin" / "llama-cli"
    if bin_path.exists():
        print("llama.cpp already exists. Your good!") 
    build_dir.mkdir(parents=True, exist_ok=True)
    print("llama.cpp is being built...")
    subprocess.run(["cmake", ".."], cwd= build_dir, check=True)
    subprocess.run(["cmake", "--build", ".", "--config", "Release"], cwd=build_dir, check=True)
    print("llama.cpp is completed")

    if __name__=="__main__":
        build_llama_cpp()


