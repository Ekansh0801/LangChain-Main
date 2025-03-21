from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template= 'Generate 5 interesting facts about {topic}',
    input_variables= ['topic']
)

chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash") 

parser = StrOutputParser()

chain = prompt | chatModel | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()
