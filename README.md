# ✈️ Air India RAG Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/AWS%20Bedrock-Powered-orange?logo=amazon-aws" alt="AWS Bedrock">
  <img src="https://img.shields.io/badge/LangChain-Integrated-green?logo=chainlink" alt="LangChain">
  <img src="https://img.shields.io/badge/RAG-Architecture-purple" alt="RAG">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

> An **Retrieval-Augmented Generation (RAG)** chatbot tailored for Air India, leveraging **AWS Bedrock APIs** for natural language processing. The chatbot provides real-time customer support by answering queries about company and airline services using a knowledge base of Air India-related given documents.

---

## 📋 Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [What You Will Learn](#what-you-will-learn)
- [What You'll Build](#what-youll-build)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the App](#running-the-app)
- [Key Features](#key-features)
- [Contributing](#contributing)
- [License](#license)

---

## 🧾 Overview

An AI-powered **RAG chatbot** for Air India built with AWS Bedrock, LangChain, and Python. Provides real-time support for flight schedules, bookings, and airline services using Retrieval-Augmented Generation.

- Ingests and processes Air India-related PDF documents
- Generates vector embeddings using AWS Bedrock's Titan Text Embeddings V2 model
- Stores embeddings in a vector database for efficient similarity search
- Retrieves relevant document chunks based on user queries
- Generates accurate, context-grounded answers using a Large Language Model (LLM)
- Provides a user-friendly chat interface for real-time support

---

## 🏗️ System Architecture

> *High-level architecture overview of the Air India RAG Chatbot pipeline — from document ingestion and embedding creation to vector storage, retrieval, and LLM-powered response generation.*
>

### 🔄 Architecture Flow

![Architecture Flow](images/architecture_flow.svg)

### Architecture Breakdown

| Stage | Component | Description |
|-------|-----------|-------------|
| **1. Document Ingestion** | PDF Parser | Collection of Air India PDFs (flight schedules, booking guides, FAQs) |
| **2. Text Preprocessing** | Text Splitter | Split documents into smaller, meaningful chunks (~15 sentences each) |
| **3. Embedding Creation** | AWS Bedrock Titan | Convert chunks into high-dimensional vector representations |
| **4. Vector Storage** |Chroma db | Store and index embeddings for fast similarity lookup |
| **5. Query Processing** | Bedrock Embeddings | Convert user query into vector for similarity matching |
| **6. Retrieval** | Vector Search | Fetch top-K most relevant document chunks |
| **7. LLM Generation** | Claude / Titan LLM | Generate grounded, context-aware response using retrieved chunks |
| **8. UI Interface** | Streamlit | Interactive chat interface for Air India customers |

---

## 🎓 What You Will Learn

- ✅ Mastering the use of **AWS Bedrock** for NLP tasks
- ✅ Implementing **Retrieval-Augmented Generation (RAG)** to enhance chatbot responses
- ✅ Building a real-time chatbot for **customer support** using AI
- ✅ Integrating a chatbot with an existing **knowledge base**
- ✅ Understanding the architecture of **cloud-based AI solutions**
- ✅ Applying **machine learning concepts** to improve chatbot performance
- ✅ **Fine-tuning LLMs** for domain-specific applications

---

## 🛠️ What You'll Build

- A functional **Air India chatbot prototype**
- An **information retrieval system** connected to the chatbot
- An **AI model integrated with AWS Bedrock**
- A **user interface** for interacting with the chatbot

---

## 🧰 Tech Stack

| Technology | Purpose |
|-----------|----------|
| **Python 3.10+** | Core programming language |
| **LangChain** | RAG pipeline orchestration | 
| **AWS Bedrock** | Foundation LLM & Embeddings (Nova Pro, Titan text embedding V2) |
| **LangChain** | RAG pipeline orchestration |
| **CHROMA** | Vector database for similarity search |
| **Boto3** | AWS SDK for Python |
| **PyPDF2 / pdfplumber** | PDF document parsing |
| **Streamlit** | Chat user interface |
| **dotenv** | Environment variable management |

---

## 📁 Project Structure

```
Air-India-RAG-Chatbot/
├── images/
│   ├── system_architecture.png   # System architecture diagram
├── AirIndia/
│   └── air_india_docs/           # Air India PDF knowledge base
├── app.py                        # Streamlit chat interface
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- AWS Account with Bedrock access enabled
- AWS CLI configured with appropriate IAM permissions
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Vishalkumarjaiswal16/Air-India-RAG-Chatbot.git
cd Air-India-RAG-Chatbot
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Configuration

1. **Copy the environment template**

```bash
cp .env.example .env
```

2. **Fill in your AWS credentials in `.env`**

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
BEDROCK_EMBEDDING_MODEL_ID=amazon.titan-embed-text-v1
```

### Running the App

1. **Ingest documents into the vector store**

```bash
python src/ingestion.py
```

2. **Launch the Streamlit chatbot UI**

```bash
streamlit run app.py
```

3. Open your browser at `http://localhost:8501`

---

## ✨ Key Features

- 🔍 **Semantic Search** — Finds the most relevant Air India documents using vector similarity
- 🤖 **LLM-Powered Responses** — Uses state-of-the-art foundation models via AWS Bedrock
- 📄 **Document Grounded** — Answers are always backed by real Air India documents
- ⚡ **Real-time Support** — Low latency responses for customer queries
- 🖥️ **Interactive UI** — Clean Streamlit-based chat interface
- ☁️ **Cloud-Native** — Fully powered by AWS services
- 🔒 **Private & Secure** — All data stays within your AWS account

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 🙏 Acknowledgements
- Built using **AWS Bedrock**, **LangChain**, and **Python**
- Architecture reference: (https://github.com/krishnaik06)

---

Made with ❤️ by [Vishal Kumar Jaiswal](https://github.com/Vishalkumarjaiswal16)
