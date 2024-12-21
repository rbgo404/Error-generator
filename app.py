from time import perf_counter

class InferlessPythonModel:
    def initialize(self):
        model_id = "mistralai/Ministral-8B-Instruct-2410"

    def infer(self, inputs):
        prompts = inputs["prompt"]
        prompts = inputs["temperature"]
        
        return 'generated_text'

    def finalize(self):
        llm = None
