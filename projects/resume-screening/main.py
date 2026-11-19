from src.resume_screening.clients.groq import client
from src.resume_screening.configs.models import openAI_model
from src.resume_screening.messages.system_message import system_message
from src.resume_screening.messages.user_message import user_message

messages= [system_message, user_message]
response_format={
    "type" : "json_object"
}

res= client.chat.completions.create(model= openAI_model, messages=messages, response_format=response_format)
raw_json= res.choices[0].message.content



