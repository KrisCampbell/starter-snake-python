import json
import random

def think(data,possibleMoves):
	lastMove = "None"
	with open('lastmove.json') as json_file:
		data = json.load(json_file)
		lastMove = data['move']

	if lastMove == "None":
		pass()
	elif lastMove == "Up":
		lastMove = "Down"
	elif lastMove == "Down":
		lastMove == "Up"
	elif lastMove == "Left":
		lastMove = "Right"
	elif lastMove == "Right":
		lastMove == "Left"
	copy = possibleMoves.copy()
	if lastMove in copy: copy.remove(lastMove)
	choice = random.choice(copy)

	with open('lastmove.json','w') as json_file:
		json.dump({"move":choice},json_file)

	return choice