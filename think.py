import json
import random

def think(data,possibleMoves):
	lastMove = "None"
	with open('lastmove.json') as json_file:
		data = json.load(json_file)
		lastMove = data['move']

	choice = random.choice(possibleMoves.remove(lastMove))
	return choice