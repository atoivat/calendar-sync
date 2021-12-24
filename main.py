import os

import requests
from dotenv import load_dotenv

load_dotenv()


NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")
NOTION_BASE_URL = "https://api.notion.com/v1/databases/"


headers = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Notion-Version": "2021-08-16"
}


response = requests.get(f"{NOTION_BASE_URL}{NOTION_DB_ID}", headers=headers)
if response.status_code != 200:
    raise Exception("Could not retrieve Notion database.")
notion_database = response.json()

payload = {
    "filter": {
        "property": "Type",
        "select": {
            "equals": "Event"
        }
    }
}
response = requests.post(
    f"{NOTION_BASE_URL}{NOTION_DB_ID}/query",
    headers=headers,
    json=payload
)
print(response.status_code)