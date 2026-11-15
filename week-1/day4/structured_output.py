import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema= Ticket.model_json_schema()
response_format= {
    "type": "json_object"
}

ROOT_DIR= Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

api_key= os.getenv("GROQ_API_KEY")
if(not api_key):
    raise ValueError("Api key not found")

client= Groq(api_key= api_key)

#System prompt
system_prompt= f"Extract personal information from the ticket scrictly based on this schema, {schema} and return output in json format"
system_message= {
    "role": "system",
    "content": system_prompt
}

role= "user"
model= "openai/gpt-oss-20b"
text= "My name is Pratyush. I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134"
prompt= f"This is a customer ticker, Extract the personal information from this. {text}"

message= {
    "role": role,
    "content": prompt
}
messages= [system_message, message] 

response= client.chat.completions.create(model= model, messages= messages, response_format= response_format)
answer= response.choices[0].message.content
print(answer);

## Extraction of data
import json

raw_json= answer
data_file= json.loads(raw_json)
ticket= Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
