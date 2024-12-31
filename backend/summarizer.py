from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

class SummarizerService:
    def __init__(self):
        self.template = """Summarize the following text:

        {text}

        Summary: """
        self.prompt = ChatPromptTemplate.from_template(self.template)
        self.model = OllamaLLM(model="llama3.2")
        self.chain = self.prompt | self.model

    def generate_summary(self, text):
        if not text:
            raise ValueError("No text provided")
        return self.chain.invoke({"text": text})