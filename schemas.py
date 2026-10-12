from pydantic import BaseModel, Field

class SoftwareProject(BaseModel):
    project_name: str | None = None
    frontend: str | None = None
    backend: list[str] = Field(default_factory=list)
    database: str | None = None
    authentication: str | None = None
    deployment: str | None = None