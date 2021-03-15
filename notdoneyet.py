import base64
import requests
import json
key = ''
key = base64.b64encode(bytes(key, 'utf-8'))
keyDecoded = key.decode('ascii')
header = {'Authorization': 'Basic ' + keyDecoded}

var = 1
url = 'https://api.printful.com/mockup-generator/create-task/71'
cont = '{"variant_ids": [4012,4013,4014,4017,4018,4019],"format": "jpg","files": [{"placement": "front","image_url": "https://www.computerhope.com/jargon/r/random-dice.jpg","position": {"area_width": 1800,"area_height": 2400,"width": 1800,"height": 1800,"top": 300,"left": 0}},{"placement": "back","image_url": "https://www.computerhope.com/jargon/r/random-dice.jpg","position": {"area_width": 1800,"area_height": 2400,"width": 1800,"height": 1800,"top": 300,"left": 0}}]}'
r = requests.get(url,data=cont, headers=header)
json_object = json.loads(r.content)
resul1 = json_object["result"]
print(resul1)
task = resul1["task_key"]
status = resul1["status"]
print(task)
	

while var == 1 :
	url2 = 'https://api.printful.com/mockup-generator/task?task_key=z787b740b384eace5cb8e7348ff0693f' 
	w = requests.get(url2, headers=header)
	
	code = json.loads(w.content)
	

	

