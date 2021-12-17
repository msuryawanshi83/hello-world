
import json
import requests
import sys

print('\nUpload report started.. \n')
baseUrl = 'https://archerysec-host.c-764b793.kyma-stage.shoot.live.k8s-hana.ondemand.com'
loginUrl = baseUrl + '/api-token-auth/'



headers = {
    'Content-type': 'application/json',
}

data = '{"username":"manojsuryawanshi@gmail.com","password":"admin123","email" : "manojsuryawanshi@gmail.com"}'

response = requests.post(loginUrl, headers=headers, data=data)

responseBody = response.content.decode("utf-8")

tokenJson = json.loads(responseBody)

print('Token Generated Successfully \n')


if len(sys.argv) >= 5:

	token = tokenJson['token']
	file = sys.argv[1]
	target = sys.argv[2]
	scanner = sys.argv[3]
	project_id = sys.argv[4]


	headers = {"Authorization": "JWT "+token}
	f = (open(file, "rb")).read()
	files = {
	"filename": (None, f),
	"project_id": (None, project_id),
	"scanner": (None, scanner),
	'scan_url': (None, target)
	}
	#url = self.host + "/api/v1/uploadscan/"
	url = baseUrl + "/api/uploadscan/"
	#print(headers)
	#print(files)
	send_request = requests.post(url, files=files, headers=headers)

	print('Scan Report uploaded Successfully \n')
	#return send_request.json()
else:
	print('Please pass valid argument with given sequence {filePath , targetName, scannerName, projectId}')	




