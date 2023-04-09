from enum import Enum
import openai


class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Message:

    def __init__(self, content, role=Role.USER):
        self.content = content
        self.role = role


class Conversation:

    def __init__(self, custom_assistant_message=None):
        openai.api_key = open("venv/openai_api_key.txt", "r").read().strip("\n")
        self.message_history = []

        if custom_assistant_message is not None:
            self.message_history.append(Message(custom_assistant_message, role=Role.SYSTEM))

    def run_message(self, message):
        if openai.api_key is None:
            return None
        self.message_history.append(message)

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": msg.role.value, "content": msg.content} for msg in self.message_history]
            )
            query_reply = completion.choices[0].message.content
            print(f"Completed querying {query_reply}")
            self.message_history.append(Message(query_reply, Role.ASSISTANT))
        except:
            query_reply = "Some error occurred in executing the query. Please try again."
            print(query_reply)
            self.message_history.append(Message(query_reply, Role.ASSISTANT))
        return query_reply

    def run_query(self, query):
        print(f"Recieved message: {query}")
        return self.run_message(Message(query))
