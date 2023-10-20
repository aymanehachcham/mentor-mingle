from mentor_mingle.llm_handler import ChatHandler
from mentor_mingle.persona.mentor import Mentor

if __name__ == "__main__":
    mentor = Mentor()
    handler = ChatHandler(persona=mentor)

    while True:
        user_prompt = input("\nUser: ")
        for res in handler.stream_chat(user_prompt):
            end_char = "\n" if "." in res else ""
            print(res, end=end_char, flush=True)
