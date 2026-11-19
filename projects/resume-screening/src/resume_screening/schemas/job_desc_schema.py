from pydantic import BaseModel

class JobDesc(BaseModel):
    role: str
    required_skills: list[str]
    preferred_skills: list[str]
    minimum_experience: float | None
    education_requirements: list[str]
    responsibilities: list[str]

job_desc_schema= JobDesc.model_json_schema()