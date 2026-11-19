import os
from pathlib import Path
from dotenv import load_dotenv


ROOT_DIR= Path(__file__).resolve().parents[3]
load_dotenv(ROOT_DIR/ ".env")

GROQ_API_KEY= os.getenv("GROQ_API_KEY")
if(not GROQ_API_KEY):
    raise ValueError("GROQ_API_KEY Key not found")