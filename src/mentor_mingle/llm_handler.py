
from dotenv import load_dotenv
import logging
import openai
import os

load_dotenv()
logger = logging.getLogger(__name__)

def openai_feedback(user_prompt: str) -> str:
    """
    This function is used to engage in feedback with the user.
    The user will be asked to provide feedback on the generated transcript.
    """
    openai.api_key = os.getenv('OPENAI_KEY')
    logger.info('OPENAI API is running for feedback...\n\n')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": "Your are a interviewer and you will be asked questions about an interview test case."
            },
            {"role": "user", "content": f"User: {user_prompt}"},
        ],
        max_tokens=150
    )
    return completion.choices[0]['message']['content']



