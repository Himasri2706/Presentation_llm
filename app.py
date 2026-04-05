import gradio as gr
from huggingface_hub import InferenceClient
import mcp_tools
import os

HF_TOKEN = os.environ.get("HF_TOKENS", "")
client = InferenceClient(token=HF_TOKEN)
MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

SYSTEM_PROMPT = """You are a helpful presentation assistant."""

def chat(user_message, history):
    msg = user_message.lower()

    if "create presentation" in msg or "create a presentation" in msg:
        title = user_message.split("about")[-1].strip() if "about" in msg else "My Presentation"
        result = mcp_tools.create_presentation(title=title, filename="output.pptx")
        reply = f"{result}\n\n📊 Presentation created! Want me to add slides?"

    elif "add slide" in msg:
        result = mcp_tools.add_slide(filename="output.pptx", layout=1)
        reply = f"{result}\n\n📝 Want me to write content on this slide?"

    elif "write" in msg and "slide" in msg:
        parts = user_message.split("slide")
        idx = int(''.join(filter(str.isdigit, parts[-1]))) if any(c.isdigit() for c in parts[-1]) else 2
        result = mcp_tools.write_text(filename="output.pptx", slide_index=idx, title="New Slide", body=user_message)
        reply = f"{result}\n\n✍️ Content written!"

    elif "search" in msg or "tell me about" in msg:
        topic = msg.replace("search", "").replace("tell me about", "").strip()
        result = mcp_tools.search_web(topic=topic)
        reply = f"{result}"

    else:
        try:
            response = client.chat_completion(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=512
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"⚠️ LLM Error: {str(e)}"

    history.append((user_message, reply))
    return "", history

with gr.Blocks(title="Presentation LLM") as demo:
    gr.Markdown("# 🤖 Presentation LLM\n### Powered by Mistral + MCP Tools")
    chatbot = gr.Chatbot(height=450, label="Chat")
    msg = gr.Textbox(placeholder="Try: Create a presentation about AI", label="Your Message")
    clear = gr.Button("🗑️ Clear Chat")
    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot)

demo.launch()