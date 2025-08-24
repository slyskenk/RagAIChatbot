# UNICEF RAG AI Chatbot 🤖📚

![UNICEF Logo Placeholder](./static/images/unicef_logo.png)

## Overview

This project is a **Retrieval-Augmented Generation (RAG) AI chatbot** specifically built for **UNICEF's Education Outcomes Fund (EOF)**.  
It helps users **ask questions about official UNICEF/EOF reports**, retrieves relevant excerpts from stored PDFs, and **provides concise answers with sources**.  
It also includes a **summarization feature** for reports.  

The project is designed with a **professional, UNICEF-inspired UI**, making it ideal for educational research or internal data analysis.  

---

## 💻 Demo

![UI Screenshot](./static/assets/screenshot1.png)
![UI Screenshot](./static/assets/screenshot2.png)

![Link to Chatbot Video Demo](./static/assets/FinalDemo.mp4)

---

## Features

- ✅ Answers questions related only to **UNICEF reports**  
- ✅ Summarizes long reports on request  
- ✅ Provides **source references** for transparency  
- ✅ Beautiful, professional UI with space for UNICEF logo  
- ✅ Easily extendable with more PDFs or powerful language models  

---

## Tech Stack

- **Backend:** Python, Flask, LangChain  
- **Frontend:** HTML, CSS, JS (UNICEF-inspired styling)  
- **Vector Database:** Chroma  
- **Embeddings & LLM:** Ollama  

---

## Ollama Methods Used

1. **Download Ollama** from [https://ollama.com](https://ollama.com) and install locally.  
2. **Download and use the following models in Ollama:**  
   - `llama3.2` → Primary chatbot LLM for question answering.  
   - `mxbai-embed-large` → Embedding model for vector search.  

> ⚡ You can use more powerful LLM models if you like, depending on your local resources and license.  

---

## Project Structure

- `main.py` → Flask server and main RAG logic for chatbot  
- `vector.py` → Handles PDF loading, splitting, embedding, and Chroma vector database  
- `data/pdf/` → Store all official UNICEF/EOF PDF reports here  
- `templates/index.html` → Frontend UI for interacting with the chatbot  
- `static/css/style.css` → All styling for professional UNICEF look  
- `static/js/script.js` → Frontend interactivity (sending messages, updating chat window)  
- `static/assets/` → Logo placeholders and demo GIFs/screenshots  
- `README.md` → Explains project, setup, usage, and portfolio showcase  
---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/slyskenk/RagAIChatbot.git
cd RagAIChatbot
Create and activate a virtual environment
```

```bash

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:  pip install -r requirements.txt     
```



```bash

pip install -r requirements.txt
Add UNICEF PDF reports
Place PDFs in data/pdf/.


Run the chatbot

```

```bash

python app.py
```
![UI Screenshot](./static/assets/screenshot3.png)
Then
```bash
Visit http://127.0.0.1:5000 or the respective url provided in your terminal in your browser.

```

## Usage
Type UNICEF-related questions in the input box.

Ask "summarize [report name]" to get a concise summary.

The chatbot only answers questions related to UNICEF reports.

Answers include a Sources section referencing the reports used.

## Contributions
Contributions are welcome! Suggestions include:

Adding more PDFs for a richer knowledge base

Using more powerful LLMs for better answers

Improving UI/UX for mobile responsiveness

## License**
APACHE License 2.0 © 2025

## Screenshots / Demo Placeholder


![UI Screenshot](./static/assets/screenshot1.png)
![UI Screenshot](./static/assets/screenshot2.png)


****Made with ❤️ for UNICEF research and educational insights.****