import json
import random

def think(data):
	choice = random.choice(data)
	print(data)
	# me = data['snakes']['you']['body']
	# myHead = data['snakes']['you']['head']
	# possibleMoves = [myHead.copy()['x']+=1,myHead.copy()['x']-=1,myHead.copy()['y']+=1,myHead.copy()['y']-=1]
	# print("Possible:",possibleMoves)

	with open('lastmove.json','w') as json_file:
		json.dump({"move":choice},json_file)

	return choice