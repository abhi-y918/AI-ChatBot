# 🚀 AI Agent Chatbot with LangGraph & Streamlit

Welcome to the **AI Agent Chatbot**! This project demonstrates a solid, stateful conversational AI application. It is powered by robust large language models via **Hugging Face**, orchestrated securely with **LangGraph**, and wrapped in a clean, responsive frontend built using **Streamlit**.

This repository is an excellent demonstration of constructing a modular, scalable AI chat application by clearly separating the presentation UI layer from the LLM orchestration backend.

---

## ✨ Key Skills & Capabilities Highlighted

- **Advanced LLM Orchestration (LangGraph & LangChain):** Uses `StateGraph` and `InMemorySaver` to build a reliable and persistent conversational memory graph. This ensures the chatbot effectively retains user context across complex chat threads.
- **Modern AI Integration (Hugging Face Serverless Inference):** Leverages `ChatHuggingFace` and `HuggingFaceEndpoint` to interact seamlessly with state-of-the-art LLMs (powered by `Qwen/Qwen2.5-72B-Instruct` out of the box), keeping the app lightweight without requiring heavy local compute.
- **Rapid UI Development (Streamlit):** Constructs a native, highly-reactive chat interface, leveraging advanced `st.session_state` manipulation to handle user chat histories asynchronously.
- **Python Architecture & Design Patterns:** Highlights strong backend API patterns by cleanly dividing the UI (`streamlit_frontend.py`) and AI Engine/Graph Logic (`langgraph_backend.py`).
- **Secure Configuration Management:** Employs standard `.env` patterns to manage remote API secrets preventing accidental leakage into version control.

## 🛠️ Technology Stack

* **Language:** Python 3.10+
* **Frontend UI Framework:** Streamlit
* **AI Orchestration:** LangGraph, LangChain Core
* **Model Provider:** Hugging Face Inference API
* **Environment Management:** `python-dotenv`

## 🏗️ Architecture Overview

The application follows a simple but powerful flow:
1. **Frontend Layer:** `streamlit_frontend.py` captures user input and holds UI-specific chat memory. It pushes user prompts into the LangGraph backend.
2. **Graph Backend:** `langgraph_backend.py` parses requests using an `InMemorySaver` to append messages.
3. **LLM Node Execution:** The state passes cleanly to the Hugging Face Inference Endpoint wrapper, retrieving generated text, updating backend state, and transmitting the final result payload back to the UI.

---

## 🚀 Local Setup Guide

Follow these instructions to spin up the application on your local machine.

### 1. Requirements & Cloning

Ensure you have Python installed and clone the project to your local directory.

### 2. Set Up a Virtual Environment
Isolate your dependencies to avoid global conflicts:
```bash
python -m venv myvenv

# For Windows:
myvenv\Scripts\activate
# For Mac/Linux:
source myvenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit langgraph langchain_core langchain_huggingface python-dotenv
```

### 4. Provide Environment Variables
You will need a Hugging Face Access Token to converse with the models.

Create a `.env` file in the root directory (if not already present) and populate it:
```env
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

### 5. Launch the Chatbot!
Start the Streamlit application server:
```bash
streamlit run streamlit_frontend.py
```
Open the local server link generated in your terminal (typically `http://localhost:8501`) and start chatting!

---

## 💡 Future Enhancements
- Expanding the LangGraph to support tool-calling agents allowing web-search functionalities.
- Migrating `InMemorySaver` to persistent database solutions (SQLite/PostgreSQL) for cross-session continuity.
- Incorporating RAG (Retrieval-Augmented Generation) nodes to chat with local documents.
