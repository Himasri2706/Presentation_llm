# 🤖 Presentation LLM

An AI-powered presentation generator that creates beautiful, 
colorful PowerPoint files for any topic using Large Language Models.

## 🚀 Features
- Generate full multi-slide PPT for any topic
- 8 beautiful color themes auto-selected per topic
- Detailed AI-generated content on every slide
- Beautiful Streamlit frontend UI
- Powered by Qwen LLM on Hugging Face
- MCP Tools for slide creation

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **LLM**: Qwen2.5-7B on Hugging Face
- **Slide Engine**: python-pptx + MCP Tools
- **Backend**: Gradio on Hugging Face Spaces
- **Protocol**: MCP (Model Context Protocol)

## 📁 Project Structure
- `app.py` — Gradio backend on Hugging Face
- `mcp_tools.py` — PowerPoint generation tools
- `streamlit_app.py` — Beautiful frontend UI
- `requirements.txt` — Dependencies

## 🔗 Live Demo
[Hugging Face Space](https://huggingface.co/spaces/honey2706/presentation-llm)
