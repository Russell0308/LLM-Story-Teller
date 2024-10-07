from llama_cpp import Llama

llm = Llama(model_path='./openorca-platypus2-13b.Q4_K_M.gguf')


class MemoryBot:
    def __call__(self, user_prompt: str) -> str:
        system_prompt = 'You are to take these chuncks of text I give you and summarize it. When you summarize try to keep it under 50 words. Also summarize with the goal of helping me understand and remember. Only return what is explicitly asked for.'
        prompt = f"### Instruction: {system_prompt}\n\n{user_prompt}\n\n### Response:\n"
        raw_output = llm(prompt, stop=["###"], max_tokens=-1, temperature=0.5)
        reply = raw_output.get("choices")[0].get("text").strip()
        return reply


    def create_memory(self, text):
        user_prompt = f'Summarize this {text}. Keep it short and sweet.'
        bot_output = self(user_prompt)
        return bot_output


    def create_memory_body(self, intro, body):
        user_prompt = f"Here is the introduction summarized: {intro}, here is your last paragraph's summary too: {body}. Summarize these two texts."
        bot_output = self(user_prompt)
        return bot_output


    def create_memory_characters(self, text):
        user_prompt = f"Make a list of the characters and their roles in this story. Use this format 'character (role)': {text}"
        bot_output = self(user_prompt)
        return bot_output
