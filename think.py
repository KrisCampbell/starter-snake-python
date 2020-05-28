import json
import random

def think(data,possibleMoves):
	lastMove = "None"
	with open('lastmove.json') as json_file:
		data = json.load(json_file)
		lastMove = data['move']

	copy = possibleMoves.copy()
	if lastMove in copy: copy.remove(lastMove)
	choice = random.choice(copy)
	return choice