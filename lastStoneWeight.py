
def lastStoneWeight(stones):
    # templateDict = {"weight":0,"idx":0}
    # heaviest, secondHeaviest = dict(templateDict),dict(templateDict)

    heaviest = {"weight":0,"idx":0}
    secondHeaviest = {"weight":0,"idx":0}

    print(secondHeaviest['weight'])

    while len(stones) > 1:
        for idx, stone in enumerate(stones):
            if stone > heaviest["weight"]:
                secondHeaviest = heaviest
                heaviest["weight"],heaviest["idx"] = stone,idx
            elif stone > secondHeaviest["weight"]:
                secondHeaviest["weight"],secondHeaviest["idx"] = stone,idx
        if heaviest["idx"] > secondHeaviest["idx"]:
            stones.pop(heaviest["idx"])
            stones.pop(secondHeaviest["idx"])
        else:
            stones.pop(secondHeaviest["idx"])
            stones.pop(heaviest["idx"])
        resultStone = heaviest["weight"] - secondHeaviest["weight"]
        stones.append(resultStone)
    if len(stones) == 1:
    	print('GO')
    	return stones[0]
    else:
        return 0
        
stones = [1,2,3,4,5]
print(lastStoneWeight(stones))