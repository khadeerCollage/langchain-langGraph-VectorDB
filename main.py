from dotenv import load_dotenv
import os
from pinecone import Pinecone
load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

client = Pinecone(api_key = PINECONE_API_KEY)

index = client.Index(host="https://demo-day-je9pxaw.svc.aped-4627-b74a.pinecone.io")

records = [
    {"id": "policy1", "text": "leave policy states that you can take leave more than 3 days."},
    {"id": "policy2", "text": "the company provides health insurance to all full time employees."}
]
# index.upsert_records(
#     "hr",
#     records
# )



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