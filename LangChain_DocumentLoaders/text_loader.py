from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

documentLoader = TextLoader('cricket.txt', encoding='UTF-8')
docs = documentLoader.load()

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)



tempelate = PromptTemplate(
    template='generate a summary of the {poem}',
    input_variables=['poem']
)

model = GoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

chain = tempelate | model | parser
result = chain.invoke({'poem':docs[0]})

print(result)


