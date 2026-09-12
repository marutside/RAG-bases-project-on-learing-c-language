# RAG-Based C Programming AI Assistant

A Retrieval-Augmented Generation (RAG) project that transforms C programming tutorial videos into searchable text and uses semantic search to retrieve relevant information for answering user questions.

## Project Pipeline

**Video → Audio → Speech-to-Text → Text Chunks → Embeddings → Semantic Search → Relevant Context → AI Answer**

## Technologies Used

* Python
* FFmpeg
* Whisper
* Sentence Transformers
* Semantic Search
* Vector Embeddings
* RAG
* LLM

## How It Works

1. C programming tutorial videos are processed using **FFmpeg** to extract audio.
2. **Whisper** converts the audio into text.
3. The generated transcript is divided into smaller chunks.
4. **Sentence Transformers** converts each text chunk into numerical embeddings.
5. When a user asks a question, the question is also converted into an embedding.
6. Semantic search finds the most relevant chunks based on meaning.
7. The retrieved information is provided as context to an LLM.
8. The LLM generates an answer based on the retrieved tutorial content.

## Objective

The goal of this project is to build an AI-powered learning assistant that allows users to ask questions about C programming tutorials and retrieve relevant information from the original video content.

## Learning Focus

This project is being developed to understand the complete RAG pipeline rather than simply using a pre-built solution. It focuses on understanding audio processing, speech recognition, text processing, embeddings, semantic search, retrieval, and AI-generated responses.
