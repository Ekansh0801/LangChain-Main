from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


chatModel = ChatGoogleGenerativeAI(model="google/gemma-2-2b-it", temperature=0, max_tokens=100) 

# 1st Prompt
tempelate1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd Prompt
tempelate2 = PromptTemplate(
    template='Write a 5 line summary on following text report on {text} \n',
    input_variables=['text']
)

prompt1 = tempelate1.invoke({'topic':'Black Hole'})

result = chatModel.invoke(prompt1)

prompt2 = tempelate2.invoke({'text': result})

result1 = chatModel.invoke(prompt2)

print(result1.content)

