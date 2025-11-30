# 📄 PDF Insighter — AI-Powered PDF Chat Assistant

[**Try it live!**](https://rag-pdf-assistant-yxeoz3bziaq3pswbylhbdc.streamlit.app/) 🚀

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-red)

---

## 🔹 Project Overview

**PDF Insighter** is a smart AI assistant that lets you **upload PDFs and interactively ask questions** about their content. Think of it as a **ChatGPT for your documents** — it reads, understands, and explains your files in clear, structured responses.  

Using **RAG (Retrieval-Augmented Generation)**, the app first retrieves the most relevant information from your PDFs and then generates **concise answers, step-by-step reasoning, and source references**.  

---

## ⚡ Key Features

- Upload **single or multiple PDFs** at once  
- Ask questions in a **ChatGPT-style interface** with scrollable conversation  
- **Persistent sessions**: refresh the page without losing your data  
- Answers include:  
  - A **concise answer**  
  - A **structured rationale**  
  - **Source references** (page number or chunk ID)  
- Uses **Pinecone** for vector storage of PDF embeddings  
- Uses **Groq LLM** leveraging **LPU (Latent Process Unit) technology** for fast, accurate document reasoning  

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **Streamlit** — for the interactive web interface  
- **LangChain** — handles RAG pipeline and prompt templates  
- **HuggingFace Embeddings** — converts PDF text into vectors  
- **Pinecone** — vector database for storing PDF chunks  
- **Groq LLM** — generates precise answers using LPU for reasoning  

---

## 🚀 How It Works

1. **Upload your PDFs** via the sidebar.  
2. **Vectorization**: Each PDF is split into chunks and stored in **Pinecone**.  
3. **Retriever**: Finds the most relevant chunks based on your question.  
4. **Prompt Template**: Combines context and question for the LLM.  
5. **LLM Response**: Generates a **concise answer**, **step-by-step rationale**, and **sources**.  
6. **Chat Interface**: Shows your questions and AI responses in a **scrollable conversation**, just like ChatGPT.  

---

## 📌 Live Demo

Check out the app here:  
[https://rag-pdf-assistant-yxeoz3bziaq3pswbylhbdc.streamlit.app/](https://rag-pdf-assistant-yxeoz3bziaq3pswbylhbdc.streamlit.app/)

---

## 💡 Notes

- Groq’s **LPU (Latent Process Unit)** allows the LLM to reason over PDF context efficiently and generate accurate answers quickly.  
- Pinecone ensures your PDF embeddings are **stored and searchable**, enabling fast retrieval for any number of queries.  

---

## 👨‍💻 Author

**Sarvesh S**
