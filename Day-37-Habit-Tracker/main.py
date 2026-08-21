import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("USERNAME")
GRAPH_ID = "graph1"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

# --Graph Creation--

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Commit Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --Pixel Creation--

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

formated_date = today.strftime("%Y%m%d")

pixel_data  ={
    "date": formated_date,
    "quantity": input("How many commits did you make today"),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# --Updating Pixel--

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# --Pixel Deletion--

pixel_deletion_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formated_date}"

response = requests.delete(url=pixel_deletion_endpoint, json=pixel_data, headers=headers)
print(response.text)