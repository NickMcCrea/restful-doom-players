#!/usr/bin/python

import requests
import logging
import random
import time
import json
import math

RESTFUL_HOST="localhost"
RESTFUL_PORT=6001

def sendAction(objectName, payload):
	global RESTFUL_HOST
	global RESTFUL_PORT
	
	url = 'http://{}:{}/api/{}/actions'.format(RESTFUL_HOST, RESTFUL_PORT, objectName)
	logging.debug('Calling {} with payload {}'.format(url, payload))
	try:
		requests.post(url, json=payload)
		return True
	except:
		logging.error('POST API call failed')
		return False
		
def getAction(objectName):
	global RESTFUL_HOST
	global RESTFUL_PORT
	
	url = 'http://{}:{}/api/{}'.format(RESTFUL_HOST, RESTFUL_PORT, objectName)
	logging.debug('Calling {}'.format(url))
	try:
		req = requests.get(url)
		data = json.loads(req.text)
		return data
	except:
		logging.error('GET API call failed')
		return None






while 1 == 1:
	playerData = getAction('player')
	worldObjectData = getAction('world/objects')
	playerId = playerData['id']
	enemies = []
	
	for worldObject in worldObjectData:
		if worldObject['typeId'] >= 3000:
			enemies.append(worldObject)
			id = worldObject['id']
			testdata = getAction('world/los/%d/%d' %(playerId, id))
			if testdata['los'] == 1:
				print testdata
    
	
	
	time.sleep(5)
