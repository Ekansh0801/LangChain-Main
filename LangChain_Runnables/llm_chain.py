from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

model1 = GoogleGenerativeAI(model='gemini-2.0-flash')

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}.",
    input_variables=['topic']
)

topic = input("Enter the Topic:")

chain = LLMChain(llm=model1, prompt=prompt)

result = chain.run(topic)

print(result)

                