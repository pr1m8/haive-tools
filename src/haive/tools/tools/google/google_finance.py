from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools

load_dotenv(".env")

google_finance_tool=load_tools(["google-finance"])
#print(google_finance_tool)
#print(google_places_tool)
