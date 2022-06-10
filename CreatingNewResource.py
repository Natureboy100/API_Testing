import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"
# Read Input Json file
file = open("C:\\Users\\hasee\\Desktop\\API\\CreateUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
# Make POST request with Json Input body
response= requests.post(url,request_json)
print(response.content)

assert response.status_code==201

print(response.headers.get('Content-Length'))

response_json=json.loads(response.text)

id= jsonpath.jsonpath(response_json,'id')

print(id[0])