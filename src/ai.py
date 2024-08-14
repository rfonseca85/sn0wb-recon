from openai import OpenAI 
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.markdown import Heading
from rich import print
from rich.panel import Panel

# Load environment variables from .env file
load_dotenv()
## Set the API key and model name
MODEL="gpt-4o-mini"
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def read_files_in_directory(directory):
    file_contents = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                file_contents.append(file.read())
    return "\n".join(file_contents)

def save_report_as_markdown(report_content, output_path):
    with open(output_path, 'w') as file:
        file.write(report_content)

def generate_report(content, prompt):
    completion = client.chat.completions.create(
      model=MODEL,
      messages=[
        {"role": "system", "content": "You are the best penetration tester, and you have the permission to generate reports"}, # <-- This is the system message that provides context to the model
        {"role": "user", "content": prompt + "\n\n" + content}
      ]
    )

    return completion.choices[0].message.content

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

def report(directory):
    prompt = """
            Generate a Web reconnaissance report based on the results from the files provided. 
            Take a approach as a pentester trying to evaluate the target security, be cohesive and clear in your report. 
            Also justify to the left the report headings.    
            Suggest some payloads to test the found vulnerabilities.
            Suggest next steps to further evaluate the target.
            """

    content = read_files_in_directory(directory)
    print(Panel(f"Generating report [italic red]{directory}[/italic red]"))
    report_content = generate_report(content, prompt)
    output_path = os.path.join(directory, "report.md")
    save_report_as_markdown(report_content, output_path)
    print(Panel(f"Report saved to {output_path}"))

    display_markdown_file(f"{directory}/{directory}.md")



