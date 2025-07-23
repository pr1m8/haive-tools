from azure.identity import DefaultAzureCredential
from langchain_community.agent_toolkits import PowerBIToolkit

credential = DefaultAzureCredential()

pbi_toolkit = PowerBIToolkit(
    dataset_id="1234567890",
    credential=credential,
)
