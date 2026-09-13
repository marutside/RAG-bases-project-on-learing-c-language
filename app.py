import streamlit as st
from sentence_transformers import SentenceTransformer, util


# -----------------------------
# Page title
# -----------------------------

st.title("🤖 C Language RAG Assistant")

st.write("Ask a question about C language")


# -----------------------------
# Load the embedding model
# -----------------------------

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


# -----------------------------
# Read transcript
# -----------------------------

with open("transcript3.txt", "r", encoding="utf-8") as f:
    text = f.read()


# -----------------------------
# Create chunks
# -----------------------------

chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)


# -----------------------------
# Create embeddings
# -----------------------------

@st.cache_resource
def create_embeddings(_model, chunks):
    return _model.encode(chunks, convert_to_tensor=True)


chunk_embeddings = create_embeddings(model, chunks)


# -----------------------------
# Ask a question
# -----------------------------

question = st.text_input("Ask your question:")


# -----------------------------
# Search when question is entered
# -----------------------------

if question:

    # Convert question into embedding
    question_embedding = model.encode(
        question,
        convert_to_tensor=True
    )


    # Compare question with all chunks
    similarities = util.cos_sim(
        question_embedding,
        chunk_embeddings
    )[0]


    # Find the best matching chunk
    best_index = similarities.argmax().item()


    # Get the most relevant chunk
    best_chunk = chunks[best_index]


    # Get similarity score
    similarity_score = similarities[best_index].item()


    # -----------------------------
    # Display result
    # -----------------------------

    st.subheader("📚 Most Relevant Information")

    st.write(best_chunk)


    # -----------------------------
    # Display similarity score
    # -----------------------------

    st.write(
        "Similarity Score:",
        round(similarity_score, 4)
    )