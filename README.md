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
```

## Running
```bash
# Start
python app.py

# Stop
CTRL+C
```

## Development notes
Ignore this I'm just very new to Python 😅:
- `textual run --dev app.py` for CSS hot reloading. `python app.py` is more for aesthetic