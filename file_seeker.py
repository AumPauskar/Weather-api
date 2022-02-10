import imp


def GetMode():
	import json
	with open('config.json', 'r') as file:
		data = json.load(file)
		return data['mode-tag']