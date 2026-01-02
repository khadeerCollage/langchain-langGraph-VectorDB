security_qa_data = [
    {
        "instruction": "What is RAG in LLM security?",
        "context": "Retrieval-Augmented Generation helps prevent data leakage by keeping sensitive data in vector stores instead of model weights.",
        "response": "RAG enhances LLM security by separating knowledge retrieval from model parameters, reducing risks of exposing sensitive training data."
    },
    {
        "instruction": "How to secure API keys in LLM applications?",
        "context": "Store credentials in environment variables, use secret managers, never commit to git.",
        "response": "Use .env files with python-dotenv, implement secret rotation, and use services like AWS Secrets Manager or Azure Key Vault."
    }
]
