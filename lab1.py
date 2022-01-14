import requests
response = requests.get("https://google.com/")
# print(requests.__version__)
print (response.status_code)
print (response.content)

