#from langchain_community.tools import ElevenLabsText2SpeechTool
from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools

load_dotenv(".env")

eleven_labs_text2speech_tool = load_tools(["eleven_labs_text2speech"])



