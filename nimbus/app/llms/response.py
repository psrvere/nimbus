from app.models import ProcessedRequest, ProcessedResponse


class ResponseGenerator:
    def __init__(self, provider: str, model: str):
        self.provider = provider
        self.model = model

    def prepare_llm(self) -> None:
        pass

    def generate_response(self, request: ProcessedRequest) -> ProcessedResponse:
        pass