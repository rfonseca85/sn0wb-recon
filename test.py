from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.markdown import Heading

def display_markdown_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            markdown = Markdown(content)
            console = Console()

            # Align headings to the left
            for element in markdown.elements:
                if isinstance(element, Heading):
                    element.align = "left"

            console.print(markdown)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
display_markdown_file("google/google.md")
