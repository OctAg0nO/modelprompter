![logo-title 8a56eaae](https://github.com/ZacTolle/modelprompter/assets/139601580/e302ce36-acd5-4c70-be65-04d490d30c70)
# Work in progress

## Motivation
To design the easiest and most hackable Graphical User Interface (GUI) and process manager for [Microsoft Autogen](https://github.com/microsoft/autogen) and other Large Language Model (LLM) frameworks that can run from anywhere. The vision roadmap includes:
- [ ] Setup wizard to help you configure everything (including local models)
- [ ] Customizable no-code command palette
- [ ] Agent code/skill viewer and editor
- [ ] Customizable dashboards to manage multiple projects
- [ ] No-code Autogen generator
- [ ] Voice to text
- [ ] Text to voice
- [ ] Remove reliance on displays completely

> This project is still in development and is not ready for use.

# Work in progress screenshots
### Configuration Wizard
<img width="989" alt="image" src="https://github.com/ZacTolle/modelprompter/assets/139601580/095fbb9f-f939-4367-8cca-2d82f136cce8">

### Early prototype mockups
<table>
  <tr>
    <td><h3>Terminal</h3><img width="800" alt="image" src="https://github.com/ZacTolle/modelprompter/assets/139601580/b2815cd5-82e4-4493-a71b-58eb01d09943"></td>
    <td><h3>VSCode</h3><img width="800" alt="image" src="https://github.com/ZacTolle/modelprompter/assets/139601580/aeb621b2-2e73-477a-9575-9b12028d6f5b"></td>
  </tr>
  <tr>
    <td><h3>Powershell</h3><img width="737" alt="image" src="https://github.com/ZacTolle/modelprompter/assets/139601580/d3906709-576f-4395-9ed9-b0ba1935f517"></td>
    <td><h3>Glitch.com Terminal</h3><img width="958" alt="image" src="https://github.com/ZacTolle/modelprompter/assets/139601580/60b6c6ba-b931-43ea-9d62-7ae6b3c8e722"></td>
  </tr>
</table>


# Local Development
## Requirements
- Python 3.6+ - https://www.python.org/downloads/
- git - https://git-scm.com/downloads

## Install
```bash
# Clone the repository
git clone https://github.com/zactolle/modelprompter
cd modelprompter

# Create and activate a virtual environment
python -m venv env

# Windows only:
./env\Scripts\activate
# Everywhere else:
source ./env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Or one of these
# python3 -m pip install -r requirements.txt
```

## Running
```bash
# Start
watchmedo auto-restart -p "*.py" -R python src/app.py

# Stop
CTRL+C
```
