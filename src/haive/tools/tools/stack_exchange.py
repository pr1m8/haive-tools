from langchain_community.tools.stackexchange.tool import StackExchangeTool
from langchain_community.utilities import StackExchangeAPIWrapper


stackexchange_tool = [StackExchangeTool(api_wrapper=StackExchangeAPIWrapper())]
