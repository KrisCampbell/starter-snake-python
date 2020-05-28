import json
import random

def think(data,possible_moves):
	me = data['you']['body']
	myHead = data['you']['head']
	myID = data['you']['id']
	opponent = data['board']['snakes']
	for snake in opponent:
		if snake['id'] == myID:
			opponent.remove(snake)
	opponent = opponent[0]
	oppBody = opponent['body']
	headCopy = myHead.copy()
	headCopy['x'] += 1
	left = False
	right = False
	up = False
	down = False
	if headCopy not in me and headCopy['x'] < 11 and headCopy not in oppBody:
		right = True

	headCopy['x'] -= 2
	if headCopy not in me and headCopy['x'] >= 0 and headCopy not in oppBody:
		left = True

	headCopy['x'] += 1
	headCopy['y'] += 1
	if headCopy not in me and headCopy['y'] < 11 and headCopy not in oppBody:
		up = True

	headCopy['y'] -= 2
	if headCopy not in me and headCopy['y'] >= 0 and headCopy not in oppBody:
		down = True

	options = []
	if left: options.append("left")
	if right: options.append("right")
	if up: options.append("up")
	if down: options.append("down")
	choice = random.choice(options)

	return choice