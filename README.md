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
Modify the config.yml file to specify the tools you want to run in each phase and their parameters. You can add new tools or adjust the existing ones as needed. Below is an example configuration:

```yaml
recon:
  - name: whois
    command: "whois {target}"
  
  - name: nslookup
    command: "nslookup {target}"

  - name: whatweb
    command: "whatweb {target}"
    
  - name: gobuster_dns
    command: "gobuster dns -w /usr/share/wordlists/seclist/Discovery/DNS/subdomains-top1million-20000.txt -t 50 -d {target} | grep -vE 'Progress'"

  - name: fuf_did
    command: "ffuf -w /usr/share/wordlists/seclist/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://{target}/FUZZ -recursion -recursion-depth 1 -t 50 -fc 301"

  - name: nikto
    command: "nikto -h {target}"

  - name: finalrecon
    command: "python3 /home/sn0wb/action/FinalRecon/finalrecon.py -nb --crawl --headers --whois --dns --dir --full --url http://{target} | grep -vE 'Requesting|API key not found|Skipping|Scanning|Requests'"    

  - name: katana
    command: "katana -u {target} --headless -d 3 -aff -f qurl"    

```

## Usage

### Run Reconnaissance Tools
To run the reconnaissance tools:

```bash 
python3 sn0wb.py recon -u inlanefreight.com
```
```bash
python3 sn0wb.py scan -u inlanefreight.com
```


### Generate AI Report

```bash 
python3 sn0wb.py report -r recon -d results/inlanefreight_com/recon
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

```vbnet
This `README.md` provides clear instructions on how to install, configure, and use the tool. Let me know if you need any modifications!
```







