import base64
import requests
import json
import time

key = ''
key = base64.b64encode(bytes(key, 'utf-8'))
keyDecoded = key.decode('ascii')
header = {'Authorization': 'Basic ' + keyDecoded}

var = 1
url = 'https://api.printful.com/mockup-generator/create-task/71'
cont = {
    "variant_ids" : [4012, 4013, 4014, 4017, 4018, 4019],
    "format": "jpg",
    "files" : [
        {
            "placement": "front",
            "image_url": "https://www.computerhope.com/jargon/r/random-dice.jpg",
            "position": {
                "area_width": 1800,
                "area_height": 2400,
                "width": 1800,
                "height": 1800,
                "top": 300,
                "left": 0
            }
        }
    ]
}
y = json.dumps(cont) 
r = requests.get(url,data=y, headers=header)
jsonstr = r.content

ds = jsonstr.decode("utf-8")
json_object = json.loads(ds)

taskkey = json_object['result']['task_key']


	

while var == 1 :
	url2 = 'https://api.printful.com/mockup-generator/task?task_key=' 
	url3 = url2 + taskkey
	
	w = requests.get(url3, headers=header)
	
	getjson = w.content

	ws = getjson.decode("utf-8")
	object_json = json.loads(ws)
#	code = json.loads(w.content)
	status = object_json['result']['status']
	print(status)
	time.sleep(15)

	if status == "completed" :
		break

mockup = object_json['result']['mockups'][0]['mockup_url']
print(mockup)

	

