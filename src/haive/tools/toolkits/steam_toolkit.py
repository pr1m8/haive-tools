# Python-steam-api, installation instrucitons and get pass


from dotenv import load_dotenv
from langchain_community.agent_toolkits.steam.toolkit import SteamToolkit
from langchain_community.utilities.steam import SteamWebAPIWrapper

load_dotenv(".env")




Steam = SteamWebAPIWrapper()
steam_toolkit = SteamToolkit.from_steam_api_wrapper(Steam)



#print(toolkit.get_tools())
