from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, max_tokens=100) 
# temperature argument is used for creativity in the response
# lower temperature value means lower creative response and vice-versa
# max_tokens for restricting tokens as the pricing for api depeds of tokens used so we cn limit 

result = chatModel.invoke("give me names of 5 indian males and only names not meaning")

print(result.content)