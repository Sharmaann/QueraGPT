from dotenv import load_dotenv
from openai import OpenAI, api_key
import os

load_dotenv()

# OPENAI_API_KEY is in .env file
api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI()


chat_history = ""
def chat_gpt_answer(question):
    global chat_history # it's not good to use global variables :)
    chat_history += f"Q: {question}\n"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": chat_history},
        ],
    )
    
    answer = completion.choices[0].message.content
    chat_history += f"A: {answer}\n"
    return answer

if __name__ == "__main__":
    #list of questions
    questions = []

    for question in questions:
        answer = chat_gpt_answer(question)
        print(f"Q: {question}")
        print(f"A: {answer}")
        print()