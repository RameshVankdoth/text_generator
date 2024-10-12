import os

from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://gendoc.cognitiveservices.azure.com/"
api_key = "e72ce722fc3744b38892a091441410d0"

client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

def analyze_document(file_path):
    with open(file_path, "rb") as fd:
        poller = client.begin_analyze_document("prebuilt-document", fd)
        result = poller.result()

    # Process the result
    for page in result.pages:
        print("Page Number:", page.page_number)
        for line in page.lines:  # Access the 'lines' attribute
            print("Line:", line.content)  # Print the content of each line


analyze_document(r"C:\Users\vanky\OneDrive\Desktop\testapp2\TxTInsighT\young_turks_round_1_achievement.pdf")    