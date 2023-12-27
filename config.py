```python
# config.py

# Importing required libraries
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Google Chrome Path
CHROME_PATH = os.getenv('CHROME_PATH')

# Task Cycle List
TASK_CYCLE = os.getenv('TASK_CYCLE').split(',')

# Validate the necessary configurations
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Please set it in your .env file.")

if not CHROME_PATH:
    raise ValueError("Missing Google Chrome Path. Please set it in your .env file.")

if not TASK_CYCLE:
    raise ValueError("Missing Task Cycle List. Please set it in your .env file.")
```
