from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)

documents = [
    'what is the capital of India?',
    'What is the fincancial capital of India?',
    'What is the capital of Japan?'
]
embedding_vector = embedding_model.embed_documents(documents)
print(embedding_vector[:10])