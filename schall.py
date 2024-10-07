from llama_cpp import Llama
from memory import MemoryBot
import time

llm = Llama(model_path='./openorca-platypus2-13b.Q4_K_M.gguf')


class StoryBot:


    def __call__(self, temperature, user_prompt: str) -> str:
        system_prompt = '''You are a storyteller who tells joyful stories that end in dark unexpected ways. Do not return a list. Only return what is explicitly asked, please.'''
        prompt = f"### Instruction: {system_prompt}\n\n{user_prompt}\n\n### Response:\n"
        raw_output = llm(prompt, stop=["###"], max_tokens=-1, temperature=temperature)
        reply = raw_output.get("choices")[0].get("text").strip()
        return(reply)


    def stream_gen(self, temperature, prompt):
        bot_output = self(temperature, prompt)
        return bot_output


def count_text(text):
    word_count = 0
    text = text.split(' ')
    for i in text:
        word_count += 1
    return(word_count)


def to_file(text, path):
    with open(path, 'w') as file:
        file.write(str(text))
        file.write('\n')


def to_file_a(text, path):
    with open(path, 'a') as file:
        file.write(str(text))
        file.write('\n')


def story_time(path, temperature):

    story_bot = StoryBot()
    mb = MemoryBot()

    #character_list = []

    #test_prompt = 'Just write a really long story'


    def write_paragraph(prompt, temperature):
        stream_gen_out = story_bot.stream_gen(temperature, prompt)
        return stream_gen_out

#INTRO
    intro_prompt = f'This is the first part, Introduce a story with a main character, antagonist, side characters, and a destintaion/goal. Please be detailed. Only return the story and nothing extra.'
    intro = write_paragraph(intro_prompt, temperature)
    to_file(intro, path)
    intro_memory = mb.create_memory(intro)
    intro_char_memory = mb.create_memory_characters(intro)

#BODY 1    
    body1_prompt = f'This is the second part, go more in depth about the side characters. You have a limit of 125 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory}'
    body1 = write_paragraph(body1_prompt, temperature)
    to_file_a(body1, path)

#BODY 2
    body2_prompt = f'This is the third part, go more in depth on the main character and their motivation/goals. You have a limit of 125 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory}'
    body2 = write_paragraph(body2_prompt, temperature)
    to_file_a(body2, path)

#BODY 3
    body3_prompt = f'This is the fourth part, take the characters through a lesson while they are on their journey. You have a limit of 125 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory}'
    body3 = write_paragraph(body3_prompt, temperature)
    to_file_a(body3, path)

#BODY 4    
    body4_prompt = f'This is the fifth part, explain what the characters learned in their journey so far. You have a limit of 125 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory}'
    body4 = write_paragraph(body4_prompt, temperature)
    to_file_a(body4, path)

#BODY 5
    body5_prompt = f"This is the sixth part, explain the antagonist's backstory. You have a limit of 125 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory}"
    body5 = write_paragraph(body5_prompt, temperature)
    to_file_a(body5, path)

#BODY 6
    body6_prompt = f'This is the seveth part, give me the climax of the story. You have a limit of 125 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory}'
    body6 = write_paragraph(body6_prompt, temperature)
    to_file_a(body6, path)
    
    body6_memory = mb.create_memory(body6)

#CONCLUSION
    conclusion_prompt = f'This is the ninth part, write the conclusion for this story. You have a limit of 150 words. Only return the story and nothing extra. Important context: Intro - {intro_memory} Characters - {intro_char_memory} Climax - {body6_memory}'
    conclusion = write_paragraph(conclusion_prompt, temperature)
    to_file_a(conclusion, path)


texts = [('story10.txt', 10), ('story5.txt', 5), ('story1.txt', 1), ('story0.5.txt', 0.5), ('story0.1.txt', 0.1)]


story_time(texts[2][0], texts[2][1])

#for text in texts:
#    story_time(texts[2], 1)
#    print(f'Story: {text[1]}')


