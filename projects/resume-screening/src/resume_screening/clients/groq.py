from groq import Groq
from ..configs.env_variables import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)
