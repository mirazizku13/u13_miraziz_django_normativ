import requests

url = "https://jsonplaceholder.typicode.com/posts"

resource = requests.get(url)
print(resource.status_code)
print(resource.json())


data =   {
    "title": "Mening birinchi postim",
    "body": "Bu test post",
    "userId": 1
  }
r = requests.post(url, json=data)
print(r.status_code)
print(r.json())

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title":"Yangilandi",
    "body":"Qarang",
    "userid":2
}
r = requests.put(url,json=data)
print(r.status_code)
print(r.json())


url = "https://jsonplaceholder.typicode.com/posts/1"
r = requests.delete(url)
print(r.status_code)
print(r.json())