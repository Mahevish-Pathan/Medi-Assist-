# MediAssist AI

## Overview

MediAssist AI is an AI-powered healthcare assistant that combines:

* Retrieval-Augmented Generation (RAG)
* MCP (Model Context Protocol) tools
* PostgreSQL database integration
* Medical report analysis
* OCR-based prescription understanding
* Vision-based image understanding
* FastAPI backend
* Streamlit frontend

The system allows users to:

* Ask healthcare-related questions based on uploaded hospital documents
* Retrieve patient information through MCP tools
* Analyze prescriptions and medical reports
* Extract text from medical images
* Generate structured report summaries using AI guardrails

---

## Features

### 1. RAG Chatbot

* Document ingestion using PDF and DOCX files
* Embedding generation using Sentence Transformers
* ChromaDB vector database
* Semantic search and retrieval
* Groq LLM-powered response generation
* Source citation support

### 2. MCP Integration

Implemented MCP tools:

* Search Patients
* Get Patient History
* Get Lab Results
* Get Payment Summary

Flow:

User → Backend → MCP Tool → PostgreSQL → Response

### 3. Medical Report Analysis

Supports:

* PNG
* JPG
* JPEG

Capabilities:

* Upload prescription images
* OCR text extraction
* Vision analysis
* Medical report summarization

### 4. OCR

Technology:

* EasyOCR

Extracts:

* Medicine Name
* Dosage
* Frequency
* Doctor Notes
* Observations

### 5. Vision Analysis

Technology:

* BLIP Image Captioning Model

Used for:

* Understanding medical images
* Generating image descriptions
* Supporting multimodal analysis

### 6. Guardrails

The system follows strict medical safety rules:

* No diagnosis generation
* No treatment recommendations
* No medication prescriptions
* Only information explicitly present in uploaded reports is extracted

---

## Project Architecture

User

↓

Streamlit Frontend

↓

FastAPI Backend

↓

├── RAG Pipeline

│ ├── Embeddings

│ ├── ChromaDB

│ ├── Retriever

│ └── Groq LLM

│

├── MCP Tools

│ ├── Search Patients

│ ├── Lab Results

│ ├── Billing Summary

│ └── PostgreSQL

│

└── Multimodal AI

├── OCR

├── Vision Analysis

└── Report Analyzer

---

## Project Structure

app/

├── backend/

│ ├── api/

│ ├── rag/

│ ├── services/

│ ├── models/

│ └── main.py

│

├── frontend/

│ ├── components/

│ └── streamlit_app.py

│

├── mcp/

│ ├── server.py

│ ├── connector.py

│ ├── tools.py

│ └── database.py

│

└── multimodal/

├── image_processor.py

├── ocr.py

├── vision_analyzer.py

├── report_analyzer.py

└── multimodal_analyzer.py

---

## Technology Stack

### Backend

* FastAPI
* Python

### Frontend

* Streamlit

### Database

* PostgreSQL
* ChromaDB

### AI & NLP

* Groq LLM
* LangChain
* Sentence Transformers

### OCR

* EasyOCR

### Vision

* BLIP

### Data Processing

* Pandas
* NumPy

---

## Installation

### Clone Repository

git clone <repository-url>

cd Medi-Assist

### Create Virtual Environment

python -m venv .venv

### Activate Virtual Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a `.env` file:

GROQ_API_KEY=your_groq_api_key

### Run Backend

python -m uvicorn app.backend.main:app --reload

### Run Frontend

streamlit run app/frontend/streamlit_app.py

---

## API Endpoints

### Health Check

GET /health

### Chat

POST /chat

### Upload Documents

POST /upload

### Retrieve Documents

POST /retrieve

### Analyze Medical Report

POST /analyze-report

### Multimodal Analysis

POST /analyze-multimodal

---

## Current Status

Completed:

* RAG Pipeline
* ChromaDB Integration
* MCP Server
* PostgreSQL Connection
* OCR Module
* Vision Analysis Module
* Report Analyzer
* FastAPI APIs
* Streamlit Integration
* Guardrails

Future Improvements:

* Better prescription extraction
* Advanced vision models (LLaVA)
* Patient dashboard
* Authentication
* Medical report history
* Production deployment


