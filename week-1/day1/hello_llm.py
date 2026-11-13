import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq

ROOT_DIR= Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

api_key= os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API Key not found")

client= Groq(api_key= api_key)
model= "allam-2-7b"
role= "user"
prompt= "Who is Virat Kohli"
message={
    "role": role,
    "content": prompt
}
messages= [message] 

response= client.chat.completions.create(model= model, messages= messages)
#print(response)

print("############################")

print(response.choices[0].message.content);