
from mentor_mingle.llm_handler import openai_feedback

if __name__ == '__main__':
    "Main conversational loop"

    while True:
        user_input = input('User: ')
        if user_input == 'quit':
            break
        print(openai_feedback(user_input))