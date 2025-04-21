from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.utilities.google_search import GoogleSearchAPIWrapper

# Load environment variables from the .env file
load_dotenv(".env")  # Or '.env' if you're using that file

# Initialize the GoogleSearchAPIWrapper
tool = GoogleSearchAPIWrapper()

# Example of using the tool
google_search_tool = load_tools(["google-search"])

print(google_search_tool)
