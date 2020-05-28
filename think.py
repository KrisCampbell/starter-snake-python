import json
import random

def think(data,possible_moves):
	choice = random.choice(possible_moves)

	me = data['you']['body']
	myHead = data['you']['head']
	myID = data['you']['id']
	opponent = data['snakes']
	for snake in opponent:
		if snake['id'] == myID:
			opponent.remove(snake)
	opponent = opponent[0]
	oppBody = opponent['body']
	headCopy = myHead.copy()
	headCopy['x'] += 1
	if headCopy not in me and headCopy['x'] < 11 and headCopy not in oppBody:
		return 'right'

	headCopy['x'] -= 2
	if headCopy not in me and headCopy['x'] >= 0 and headCopy not in oppBody:
		return 'left'

	headCopy['x'] += 1
	headCopy['y'] += 1
	if headCopy not in me and headCopy['y'] < 11 and headCopy not in oppBody:
		return 'up'

	headCopy['y'] -= 2
	if headCopy not in me and headCopy['y'] >= 0 and headCopy not in oppBody:
		return 'down'

	return 'up'