import json
import random

def checknb(snakes,position):
	leftpos = position.copy()['x'] -= 1
	rightpos = position.copy()['x'] += 1
	uppos = position.copy()['y'] += 1
	downpos = position.copy()['y'] -= 1
	neighborsOpen = 4
	for snake in snakes:
		if leftpos in snake['body']:
			neighborsOpen -= 1
		if rightpos in snake['body']:
			neighborsOpen -= 1
		if uppos in snake['body']:
			neighborsOpen -= 1
		if downpos in snake['body']:
			neighborsOpen -= 1

	return neighborsOpen


def think(data,possible_moves):
	me = data['you']['body']
	myHead = data['you']['head']
	myID = data['you']['id']
	opponent = data['board']['snakes']
	snakes = data['board']['snakes']
	for snake in opponent:
		if snake['id'] == myID:
			opponent.remove(snake)
	opponent = opponent[0]
	oppBody = opponent['body']
	headCopy = myHead.copy()
	leftpos = headCopy.copy()['x'] -= 1
	rightpos = headCopy.copy()['x'] += 1
	uppos = headCopy.copy()['y'] += 1
	downpos = headCopy.copy()['y'] -= 1
	leftCheck = checknb(snakes,leftpos)
	rightCheck = checknb(snakes,rightpos)
	upCheck = checknb(snakes,up)
	downCheck = checknb(snakes,down)
	maxCheck = max(leftCheck,rightCheck,upCheck,downCheck)
	if(maxCheck == leftCheck):
		return 'left'
	elif(maxCheck == upCheck):
		return 'up'
	elif(maxCheck == rightCheck):
		return 'right'
	elif(maxCheck == downCheck):
		return 'down'