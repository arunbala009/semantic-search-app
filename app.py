import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read data
with open("data.txt", "r") as file:
    documents = file.readlines()

documents = [doc.strip() for doc in documents]

# Convert documents into embeddings
doc_embeddings = model.encode(documents)

st.title("Semantic Search App")

query = st.text_input("Search anything")

if query:
    # Convert search query into embedding
    query_embedding = model.encode([query])[0]

    # Cosine similarity
    similarities = []

    for emb in doc_embeddings:
        similarity = np.dot(query_embedding, emb) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(emb)
        )
        similarities.append(similarity)

    # Get best matches
    top_indices = np.argsort(similarities)[::-1]

    st.subheader("Results")

    for idx in top_indices[:3]:
        st.write(f"✅ {documents[idx]}")
        st.write(f"Score: {similarities[idx]:.2f}")
        st.write("---")