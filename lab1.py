import requests
# response = requests.get("https://google.com/")
# print(requests.__version__)
# print (response.status_code)
# print (response.content)

url = "https://raw.githubusercontent.com/moenuma/404lab1/master/lab1.py?token=GHSAT0AAAAAABQEZJ6ORTTEMC767TZLGHEWYPLEXEA"
r = requests.get(url, allow_redirects=True)
open('download.py', 'wb').write(r.content)
