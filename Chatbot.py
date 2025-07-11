from typing import TypedDict,Annotated
from langgraph import graph
from langgraph.graph import add_messages,StateGraph,END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(temperature=0,model="llama3-8b-8192")
class Basicchatstate(TypedDict):
    messages: Annotated[list,add_messages]
    
    
def chatbot(state:Basicchatstate):
    return{
        "messages":[llm.invoke(state["messages"])]
    }

graph=StateGraph(Basicchatstate)
graph.add_node("chatbot",chatbot)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)
app=graph.compile()

while True:
    user_input=input("user:")
    if user_input=="exit":
        break
    else:
        results=app.invoke({
         "messages":   [HumanMessage(content=user_input)]
        })
        print("AI:", results["messages"][-1].content)
    
    








