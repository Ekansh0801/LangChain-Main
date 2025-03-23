from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model1 = GoogleGenerativeAI(model='gemini-2.0-flash')

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}.",
    input_variables=['topic']
)

topic = input("Enter the Topic:")

formatted_prompt = prompt.invoke({"topic": topic})


result = model1.invoke(formatted_prompt)

print(result)

                