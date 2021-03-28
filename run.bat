@echo off
if exist venv (
  echo Virtual Environment Detected
) else (
  echo Creating new Virtual Environment
  python -m venv venv
)
cd venv/Scripts && activate && cd ../../ && pip install -r requirements.txt && python main.py
