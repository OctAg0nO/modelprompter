# Work in progress
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
python -m venv venv

# Windows only:
venv\Scripts\activate
# Everywhere else:
source venv/bin/activate

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
- `textual run --dev app.py` for CSS hot reloading