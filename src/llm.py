import ollama

class OllamaLLM:

    def __init__(self):
        self.model = "qwen3:8b"

    def generate(self, prompt):

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]