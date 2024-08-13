# sn0wbRecon: Web Scan Tool

sn0wbRecon is a web reconnaissance tool designed to assist with recon tasks and generate payloads with the help of AI.

## Installation

### Option 1: Run in a Controlled Environment

To avoid installing the required libraries globally, you can set up a virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

### Option 2: Install Libraries Globally
If you prefer to install the required libraries globally, run:

```bash
pip3 install -r requirements.txt
```

## Configuration

### API Key
Before running the tool, you need to add a .env file in the root directory with your OpenAI API key:

```plaintext
OPENAI_API_KEY=YOUR_OPENAI_KEY_HERE
```

### Tool Configuration
Modify the config.yml file to specify the tools you want to run and their parameters. You can add new tools or adjust the existing ones as needed. Below is an example configuration:

```yaml
commands:
  - name: ping
    args: ["-c", "4"]

  - name: curl
    args: ["-i"]
```

## Usage

### Run Reconnaissance Tools
To run the reconnaissance tools:

```bash 
python3 sn0wbRecon.py recon -u https://www.inlanefreight.com/ -n inlanefreight
```

### Generate AI Report

```bash 
python3 sn0wbRecon.py report -o inlanefreight
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

```vbnet
This `README.md` provides clear instructions on how to install, configure, and use the tool. Let me know if you need any modifications!
```







