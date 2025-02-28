from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)

embedding_vector = embedding_model.embed_query('what is the meaning of life?')
print(embedding_vector[:10])