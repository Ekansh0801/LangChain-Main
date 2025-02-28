from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, max_tokens=100) 

chathistory = [
    SystemMessage('You are a helpful AI Assistant')
]

while True:
    user_input = input('You: ')
    chathistory.append(HumanMessage(user_input))
    if(user_input == 'exit'):
        break
    result = chatModel.invoke(chathistory)
    chathistory.append(AIMessage(result.content))
    print("AI: ",result.content)

print(chathistory)