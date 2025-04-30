@echo off

:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

echo Virtual environment setup complete. Activate it using "venv\Scripts\activate".