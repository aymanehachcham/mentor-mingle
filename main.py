from src.mentor_mingle.llm_handler import ChatHandler
from src.mentor_mingle.persona.mentor import Mentor

if __name__ == "__main__":
    mentor = Mentor()
    handler = ChatHandler(persona=mentor)

    while True:
        user_prompt = input("\nUser: ")
        handler.stream_chat(user_prompt)
