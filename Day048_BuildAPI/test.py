import requests

BASE = "http://127.0.0.1:5000/"
my_url = BASE + "helloworld/Joe/6"
# print(my_url)

response = requests.get(my_url)

print(response.json())


