import gradio
from chat.Conversation import Conversation

conversation = Conversation()
def gradio_start_chat(text):
    global conversation
    conversation.run_query(text)
    messages = conversation.message_history
    return [(messages[i].content, messages[i + 1].content) for i in range(0, len(messages)-1, 2)]


with gradio.Blocks() as demo:
    with gradio.Column():
        txt = gradio.Dropdown()
    chatbot = gradio.Chatbot()
    with gradio.Row():
        txt = gradio.Textbox(show_label=False, placeholder="Type your message here").style(container=False)
        txt.submit(gradio_start_chat, txt, chatbot)
        # txt.submit(lambda: "", None, txt)
        txt.submit(None, None, txt, _js="() => {''}")

demo.launch()
