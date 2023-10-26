from mentor_mingle.llm_handler import ChatHandler

if __name__ == "__main__":
    handler = ChatHandler()
    while True:
        user_prompt = input("\nUser: ")
        for res in handler.stream_chat(user_prompt):
            end_char = "\n" if "." in res else ""
            print(res, end=end_char, flush=True)

        handler.last_chat = {
            "query": user_prompt,
            "assistant": "",
        }
