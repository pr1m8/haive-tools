from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools

load_dotenv(".env")

tools = load_tools(["dalle-image-generator"])
print(tools)



