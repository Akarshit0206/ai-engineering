from ..configs import job_desc

user_prompt = f"""
Analyze the following job description:

{job_desc}
"""

user_message={
    "role" : "user",
    "content" : user_prompt
}