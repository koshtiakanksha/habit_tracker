import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "yous"
TOKEN = "asdfghkl_@2123456uhvc"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph2",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kms did you cycle today?\n")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

updated_pixel = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
new_params = {
    "quantity": "3.9"
}
# response = requests.put(url=updated_pixel, json=new_params, headers=headers)
# print(response.text)

delete_pixel_url = f"{pixel_creation_endpoint}/{datetime.now().strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_url, headers=headers)
# print(response.text)
