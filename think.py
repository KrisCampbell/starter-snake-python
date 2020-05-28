import json
import random

def checknb(snakes,position):
	leftpos = position.copy()
	rightpos = position.copy()
	uppos = position.copy()
	downpos = position.copy()
	leftpos['x'] -= 1
	rightpos['x'] += 1
	uppos['y'] += 1
	downpos['y'] -= 1
	neighborsOpen = 4
	for snake in snakes:
		if leftpos in snake['body'] or leftpos['x'] < 0:
			neighborsOpen -= 1
		if rightpos in snake['body'] or rightpos['x'] > 10:
			neighborsOpen -= 1
		if uppos in snake['body'] or uppos['y'] > 10:
			neighborsOpen -= 1
		if downpos in snake['body'] or downpos['y'] < 0:
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
	leftpos = myHead.copy()
	rightpos = myHead.copy()
	uppos = myHead.copy()
	downpos = myHead.copy()
	leftpos['x'] -= 1
	rightpos['x'] += 1
	uppos['y'] += 1
	downpos['y'] -= 1
	leftCheck = checknb(snakes,leftpos)
	rightCheck = checknb(snakes,rightpos)
	upCheck = checknb(snakes,uppos)
	downCheck = checknb(snakes,downpos)
	maxCheck = max(leftCheck,rightCheck,upCheck,downCheck)
	if(maxCheck == leftCheck):
		return 'left'
	elif(maxCheck == upCheck):
		return 'up'
	elif(maxCheck == rightCheck):
		return 'right'
	elif(maxCheck == downCheck):
		return 'down'