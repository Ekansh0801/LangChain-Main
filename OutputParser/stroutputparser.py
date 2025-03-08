from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()
chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

tempelate1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables=['topic'],
)


tempelate2 = PromptTemplate(
    template = 'Write a 5 line summary on {text}',
    input_variables=['text'],
)

chain = tempelate1 | chatModel | parser | tempelate2 | chatModel | parser

result = chain.invoke({'topic': 'Swati'})

print(result)


