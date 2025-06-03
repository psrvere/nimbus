from pydantic import BaseModel

class ProcessedRequest(BaseModel):
    query: str
    conversation_id: str
    valid: bool

class ProcessedResponse(BaseModel):
    response: str
    conversation_id: str