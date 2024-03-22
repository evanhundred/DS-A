def fixPotholes(str, bank):
	# find all pothole streaks
	streaks = {}
	i = 0
	while i < len(str):
		if str[i] == 'x':
			j = i + 1
			while j < len(str) and str[j] == 'x':
				j += 1
			streaks[i] = j - i
			i = j + 1
		else:
			 i += 1
	sortedStreaks = sorted(streaks.items(),key=lambda x:x[1], reverse=True)
	# print(sortedStreaks)
	# for k, v in streaks.items():
	# 	print(k,v)

	fixed = 0
	for streak in sortedStreaks:
		# print(streak,bank,fixed)
		if bank == 0:
			return fixed
		if streak[1] >= bank - 1:
			fixed += bank - 1
			return fixed
		else:
			fixed += streak[1]
			bank -= streak[1] + 1

print(fixPotholes('.xx...x.xxx', 6))