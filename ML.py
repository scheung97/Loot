import numpy as np 

"""
Implement scoring for the food category
"""
swipe = np.zeros(75).reshape(1,75) #75 products put into 1x75 array
score = np.zeros(75).reshape(75,1) #75 scores put into 75x1 array


if category == "12b47723-3381-4ffc-b699-07d4b8e1bc1a" #id for food category in our shop
	#matrix idx = sku-1
	#neg. number -> unhealthy / pos. number -> healthy
	score[0] = -50
	score[2] = 50
	score[6] = -50
	score[9] = 50
	score[11] = 50
	score[13] = -50
	score[16] = 50
	score[24] = 50
	score[25] = -50
	score[29] = -50
	score[32] = 50
	score[34] = -50
	score[35] = -50
	score[42] = -50
	score[43] = -50
	score[44] = 50
	score[57] = -50

	#for each sku we have, determine card is swiped
	#increment values in the swipe array based on direction
	for x in sku 
		if swipe_direction == "left"
			swipe[sku-1] = swipe[sku-1] - 1
		elif swipe_direction = "right"
			swipe[sku-1] = swipe[sku-1] + 1
		elif swipe_direction == "up"
			swipe[sku-1] = swipe[sku-1] + 5
		else 
			swipe[sku-1] = swipe[sku-1]

	#matrix multi
	category_score = np.matmul(swipe,score)

	if category_score > 0
		for x in score > 0
			sku = x+1 
	elif category_score < 0
		for x in score < 0 
			sku = x+1
	else 
		pass 
