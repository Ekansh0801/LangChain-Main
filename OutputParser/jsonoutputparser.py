from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1.0)
parser = JsonOutputParser()

tempelate = PromptTemplate(
    template ='give me a name, age and city of a fictional indian character \n {format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = tempelate.format()

# result = chatModel.invoke(prompt)

# final_result = parser.parse(result.content)

chain = tempelate | chatModel | parser

result = chain.invoke({})
print(result)