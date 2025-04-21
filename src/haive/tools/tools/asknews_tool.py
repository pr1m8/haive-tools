
from dotenv import load_dotenv
from langchain_community.tools.asknews import AskNewsSearch

load_dotenv(".env")
asknews_search_tool=[AskNewsSearch()]








