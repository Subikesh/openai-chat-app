import gradio
from chat.Conversation import Conversation

if __name__ == "__main__":
    conversation = Conversation()
    application = gradio.Interface(
        fn=conversation.run_query,
        inputs="text",
        outputs="text",
        title="Your personalized Chat GPT"
    )
    application.launch()
