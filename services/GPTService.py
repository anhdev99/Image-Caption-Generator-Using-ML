from typing import Any

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="sk-proj-p9QWuDpwbF0V15vr3WfTT3BlbkFJinCK0vn9I8FEzIrhxGHs"
)

class GPTService:
    def chatbot(self, msg: str, messages: Any) -> Any:

        # Keep repeating the following
        while True:
            # Prompt user for input
            message = msg

            # Exit program if user inputs "quit"
            if message.lower() == "quit":
                break

            # Add each new message to the list
            messages.append({"role": "user", "content": message})

            print(messages)
            # Request gpt-3.5-turbo for chat completion
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Print the response and add it to the messages list
            chat_message =  response.choices[0].message.content

            print(f"Bot: {chat_message}")

            messages.append({"role": "assistant", "content": chat_message})


            return chat_message


gpt_service = GPTService()