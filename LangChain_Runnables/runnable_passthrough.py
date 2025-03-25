from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Give explanantion of the following {joke}.',
    input_variables=['joke']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'Cricket'})

print(result)

