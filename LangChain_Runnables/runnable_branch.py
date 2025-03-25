from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = GoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)


report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))


# LangChain Expression Language (LCEL)
#since sequential chain is most commonly used so instead of writing this RunnableSequence
# we can use | pipes to implement this like prompt1 | model | parser