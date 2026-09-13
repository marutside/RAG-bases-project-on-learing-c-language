import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Page title
st.title("🤖 C Language RAG Assistant")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read transcript
with open("transcript3.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Create chunks
chunk_size = 500
chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

# Create embeddings
chunk_embeddings = model.encode(chunks, convert_to_tensor=True)

# Ask question
question = st.text_input("Ask a question about C language:")

if question:

    # Convert question into embedding
    question_embedding = model.encode(
        question,
        convert_to_tensor=True
    )

    # Compare question with chunks
    similarities = util.cos_sim(
        question_embedding,
        chunk_embeddings
    )[0]

    # Find best matching chunk
    best_index = similarities.argmax().item()

    # Get relevant chunk
    best_chunk = chunks[best_index]

    st.subheader("Most relevant information")
    st.write(best_chunk)

    st.write(
        "Similarity score:",
        similarities[best_index].item()
    )