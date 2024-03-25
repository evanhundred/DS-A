import math

def minEatingSpeed(piles, h):
	total = sum(piles)

	return math.ceil(total / h)

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h)) # expeted: 4

piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h)) # expeted: 30

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h)) # expeted: 23