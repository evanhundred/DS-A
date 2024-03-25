import math

def minEatingSpeed(piles, h):
        l, r = 0, 1

        def good(speed):
            hours = 0
            for idx in piles:
                hours += (idx + speed - 1) // speed        
            return hours <= h

        while not good(r):
            r *= 2
        
        while r > l + 1:
            midpoint = (r - l) // 2 + l
            if good(midpoint):
                r = midpoint
            else:
                l = midpoint

        return r


piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h)) # expeted: 4

piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h)) # expeted: 30

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h)) # expeted: 23