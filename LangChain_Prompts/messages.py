from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

messages = [
    SystemMessage(content='You are a helpul assistant'),
    HumanMessage(content='Tell me about LangChain')
] 

result = chatModel.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
