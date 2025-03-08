from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1.0)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

tempelate = PromptTemplate(
    template='Give me 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction':parser.get_format_instructions}
)

# prompt = tempelate.invoke({'topic':'any random topic'})

# result = chatModel.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

chain = tempelate | chatModel | parser

result = chain.invoke({'topic':'black hole'})

print(result)