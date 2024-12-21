from time import perf_count

class InferlessPythonModel:
    def initialize(self):
        model_id = "mistralai/Ministral-8B-Instruct-2410"

    def infer(self, inputs):
        prompts = inputs["prompt"]
        prompts = inputs["tops"]
        
        return {'generated_text': "primary"}

    def finalize(self):
        llm = None
