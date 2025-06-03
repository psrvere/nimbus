from fastapi import APIRouter
from typing import Optional, List
import uuid
from app.models import ProcessedRequest, ProcessedResponse

router = APIRouter(tags=["query"])

class LLMRequest:
    def __init__(self, query: str, conversation_id: Optional[str] = None,
                 provider: Optional[str] = None, model: Optional[str] = None):
        self.query = query
        self.conversation_id = conversation_id
        self.provider = provider
        self.model = model

class LLMResponse:
    def __init__(self, response: str, conversation_id: Optional[str] = None):
        self.response = response
        self.conversation_id = conversation_id

def conversaton_request(request: LLMRequest) -> LLMResponse:
    try:
        conversation_id = request.conversation_id or generate_conversation_id()
        if not validate_request(request):
            return LLMResponse(
                response="Are you trying to ask me something?",
                conversation_id=conversation_id
            )
        response = generate_response(request)
        return LLMResponse(
            response=response,
            conversation_id=conversation_id
        )
    except Exception as e:
        return LLMResponse(
            response=f"An error occurred: {str(e)}",
            conversation_id=conversation_id
        )
    
def process_request(request: LLMRequest) -> ProcessedRequest:
    valid = validate_request(request)

    return ProcessedRequest(
        query=request.query,
        conversation_id=request.conversation_id,
        valid=valid
    )

def generate_conversation_id() -> str:
    return str(uuid.uuid4())

def validate_request(request: LLMRequest) -> bool:
    return len(request.query) > 0

def generate_response(request: LLMRequest) -> LLMResponse:
    return f"Response to {request.query}"