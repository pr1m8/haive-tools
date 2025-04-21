

import getpass
import os

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper

from src.config.config import Config

load_dotenv(".env")

if not Config.WOLFRAM_ALPHA_APPID:
    os.environ["WOLFRAM_ALPHA_APPID"] = getpass.getpass("Enter your Wolfram Alpha App ID: ")
    raise ValueError("WOLFRAM_ALPHA_APP_ID is not set")
#print(Config.WOLFRAM_ALPHA_APP_ID)


wolfram = WolframAlphaAPIWrapper()
wolfram_alpha_tools = load_tools(["wolfram-alpha"])



