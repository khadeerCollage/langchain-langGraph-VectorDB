from dotenv import load_dotenv
import os
from pinecone import Pinecone
load_dotenv()
import random

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

client = Pinecone(api_key = PINECONE_API_KEY)

index = client.Index(host="https://demo-day-je9pxaw.svc.aped-4627-b74a.pinecone.io")


def generate(vector_count,vector_dim):
    vector_to_upsert = []
    genres = ["drama", "action", "comedy", "thriller", "romance", "sci-fi"]
    for i in range(vector_count):
        unique_id = f"vec-{i}"
        
        # Generate a list of random floats for the 'values' (the embedding)
        # In a real application, you would replace this with actual model embeddings
        values = [random.random() for _ in range(vector_dim)]
        
        # Generate sample metadata
        metadata = {
            "genre": random.choice(genres),
            "year": random.randint(2000, 2024),
            "title": f"Sample Movie Title {i}"
        }
        
        # Append the record to the list
        vector_to_upsert.append({
            "id": unique_id,
            "values": values,
            "metadata": metadata
        })
        
    return vector_to_upsert

# Embed the Query: Convert the user's input (e.g., a search question) into a vector using the exact same embedding model you used for your stored data.
# Perform Query: Send the query vector to Pinecone, specifying the top_k (how many results you want back), whether to include metadata, and which namespace to search.
# Process Results: Pinecone returns a ranked list of the most similar vector IDs and their associated similarity scores. You use the IDs to retrieve the original data.

NUM_VECTORS = 100
VECTOR_DIMENSION = 8 # Use 1536 for OpenAI models

# Generate the 100 vectors
my_upsert_data = generate(NUM_VECTORS, VECTOR_DIMENSION)










# to search for as namespace 'hr'
result = index.search(
    namespace="hr",
    query={
    "top_k":1,
    "inputs" : {
        "text": " Leave Policy "
    }
} 
) 
print(result)