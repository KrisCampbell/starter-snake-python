import json
import random

def think(data,possible_moves):
	choice = random.choice(possible_moves)

	me = data['you']['body']
	myHead = data['you']['head']
	headCopy = myHead.copy()
	headCopy['x'] += 1
	if headCopy not in me and headCopy['x'] < 11:
		return 'right'

	headCopy['x'] -= 2
	if headCopy not in me and headCopy['x'] >= 0:
		return 'left'

	headCopy['x'] += 1
	headCopy['y'] += 1
	if headCopy not in me and headCopy['y'] < 11:
		return 'up'

	headCopy['y'] -= 2
	if headCopy not in me and headCopy['y'] >= 0:
		return 'down'

	return 'up'