from setuptools import setup, find_packages

setup(
    name = "sagemode", 
    version = "0.1",
    packages = find_packages(),
    include_package_data = True, 
    install_requirements = ["typer", "rich"],
    entry_points = {
        "console_scripts" : ["sage = cli.sage:app"]
    }
)  