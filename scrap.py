def doThing():
	x,y = 0,3
	s = "hello"
	myDict = dict(x=1,y=-1)
	
	for ptr, val in myDict:
		eval(ptr) += val
	eval()

print(doThing())