from langchain_community.agent_toolkits import AzureAiServicesToolkit
from haive.config.config import Config


azure_toolkit = AzureAiServicesToolkit().get_tools()

