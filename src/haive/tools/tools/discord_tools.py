from dotenv import load_dotenv
from langchain_discord_shikenso.toolkits import DiscordToolkit

load_dotenv(".env")

discord_toolkit = DiscordToolkit()

discord_tools = discord_toolkit.get_tools()


