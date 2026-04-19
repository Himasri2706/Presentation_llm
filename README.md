<div align="center">
  
  # 🤖 Presentation LLM
  
  **An AI-powered presentation generator that crafts beautiful, colorful PowerPoint files for any topic using Large Language Models.**

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  </p>

  <h3>
    <a href="https://presentationllm-zflg2b24ocrgf2gcgvcwem.streamlit.app/">Live Web App Link</a>
    <span> | </span>
    <a href="https://huggingface.co/spaces/honey2706/presentation-llm">Hugging Face Space</a>
  </h3>

</div>

---

## 🎯 Overview

**Presentation LLM** is an advanced tool that allows anyone to generate complete, multi-slide PowerPoint presentations by simply giving it a topic. It automatically selects beautiful color themes based on the context and uses the powerful **Qwen2.5-7B** LLM to structure and generate high-quality text for every slide.

<div align="center">
  <video src="https://github.com/Himasri2706/Presentation_llm/raw/main/assets/demo.mov" controls="controls" width="800" title="Presentation LLM Demo"></video>
  <br>
  <em>*Click to watch the demo of Presentation LLM creating a beautifully crafted PPT in seconds.*</em>
</div>

---

## ✨ Features

- 📑 **Comprehensive Content Generation**: Automatically structures your presentation into title, introduction, body, and conclusion slides.
- 🎨 **Smart Theming**: Uses 8 distinct, beautiful color themes auto-assigned to suit the given topic.
- 🚀 **Fast & Responsive UI**: Clean and beautiful user interface built with Streamlit.
- 🧠 **Cutting-Edge AI**: Powered by Qwen LLM on Hugging Face, utilizing Model Context Protocol (MCP) Tools.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Qwen2.5-7B (Hosted via Hugging Face)
- **Slide Engine**: `python-pptx` + MCP Tools
- **Backend / Hosting**: Gradio & Hugging Face Spaces

## 📁 Project Structure

```bash
📦 Presentation_llm
 ┣ 📂 assets/
 ┃ ┗ 📜 demo.mov             # Demo video of the platform
 ┣ 📜 app.py                 # Gradio backend script
 ┣ 📜 config.py              # Configuration constants
 ┣ 📜 mcp_tools.py           # PowerPoint generation engine
 ┣ 📜 streamlit_app.py       # Main Streamlit frontend interface
 ┣ 📜 requirements.txt       # Project dependencies
 ┗ 📜 README.md              # Project documentation
```

## 🚀 How to Run Locally

You can easily run this AI generator on your own machine!

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Himasri2706/Presentation_llm.git
   cd Presentation_llm
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open in Browser**
   Navigate to `http://localhost:8501` to view your application!

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/Himasri2706">Himasri</a></sub>
</div>
