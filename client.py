
import requests
import json

url = 'http://127.0.0.1:5000/'

data = [[1650,0,143.6,163.8,0,1005.6,900.9,3]]
j_data = json.dumps(data)
print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
result = eval(r.text).partition('.')
print(result[0])