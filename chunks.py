# import os

# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# with open("transcript3.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# chunk_size = 500

# chunks = []

# for i in range(0, len(text), chunk_size):
#     chunk = text[i:i + chunk_size]
#     chunks.append(chunk)

# print("Total chunks:", len(chunks))

# for i, chunk in enumerate(chunks):
#     print("\n--- Chunk", i + 1, "---")

#   print(chunk)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")