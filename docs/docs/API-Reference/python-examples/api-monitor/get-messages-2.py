import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/messages?flow_id={os.getenv('FLOW_ID', '')}&session_id=code-explorer-224&sender=Machine&sender_name=AI&order_by=timestamp"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
