import requests

response = requests.get("https://av.by/")

print(response.status_code)

print(response.headers)

# print(response.content)

# print(response.text)
