import json
import random

def checknb(snakes,position,you):
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
		if position in snake['body'] or position in you or position['x'] < 0 or position['x'] > 10 or position['y'] < 0 or position['y'] > 10:
			return -1
		if leftpos in snake['body'] or leftpos in you or leftpos['x'] < 0: 
			neighborsOpen -= 1
		if rightpos in snake['body'] or rightpos in you or rightpos['x'] > 10: 
			neighborsOpen -= 1
		if uppos in snake['body'] or uppos in you or uppos['y'] > 10: 
			neighborsOpen -= 1
		if downpos in snake['body'] or downpos in you or downpos['y'] < 0: 
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
	leftCheck = checknb(snakes,leftpos,me)
	rightCheck = checknb(snakes,rightpos,me)
	upCheck = checknb(snakes,uppos,me)
	downCheck = checknb(snakes,downpos,me)
	maxCheck = max(leftCheck,rightCheck,upCheck,downCheck)
	if(maxCheck == leftCheck):
		return 'left'
	elif(maxCheck == upCheck):
		return 'up'
	elif(maxCheck == rightCheck):
		return 'right'
	elif(maxCheck == downCheck):
		return 'down'