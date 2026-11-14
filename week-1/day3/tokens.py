import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

ROOT_DIR= Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

api_key= os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API Key not found")

client= Groq(api_key= api_key)
role= "user"
model= "allam-2-7b"

prompt1= "Hi!"
prompt2= "Explain Time travel in detail"
prompt3= "Write an essay on ML in 1000 words"
prompts= [prompt1, prompt2, prompt3]

for prompt in prompts:
    message= {"role": role, "content": prompt}
    messages= [message]

    res= client.chat.completions.create(model= model, messages= messages, max_tokens=50)
    print(f"Prompt: {prompt} --> Your Tokens: {res.usage.prompt_tokens} --> Comp. Tokens: {res.usage.completion_tokens}");