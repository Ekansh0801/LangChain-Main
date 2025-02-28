from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

# this don't work here 

# chat_tempelate = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple words, what is {topic}')
# ])

# prompt = chat_tempelate.invoke({'domain':'Cricket','topic':'Doosra'})

# print(prompt)


chat_tempelate = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple words, what is {topic}')
])

prompt = chat_tempelate.invoke({'domain':'Cricket','topic':'Doosra'})

print(prompt)
