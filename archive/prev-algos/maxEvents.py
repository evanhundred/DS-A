
#
# Complete the 'maxEvents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arrival
#  2. INTEGER_ARRAY duration
#

def maxEvents(arrival, duration):
    # for every arrival time conflict, pick the time that has the least conflicts
    eventsCount = 0

    # [0,0,1]
    # [4,1,1]
    # arrivalConflicts = {
    #     0: [0, 1, 2]
    # }
    
    arrivalConflicts = {}
    
    # populate arrivalConflicts object
    for idx, time in enumerate(arrival):
        nextTime = time + duration[idx]  # 3
        if idx == len(arrival) - 1:
            break
        nextIdx = idx + 1
        while arrival[nextIdx] < nextTime:
            if idx not in arrivalConflicts:
                arrivalConflicts[idx] = []
            arrivalConflicts[idx].append(nextIdx)
            nextIdx += 1

    print(arrivalConflicts)

    numConflicts = {}
    for arrivalTimeIdx in arrivalConflicts:
        for conflictIdx in arrivalConflicts[arrivalTimeIdx]:
            currentConflicts = 1
            if conflictIdx in arrivalConflicts:
                currentConflicts += len(arrivalConflicts[conflictIdx])
            numConflicts[conflictIdx] = currentConflicts

    # print(numConflicts)
    
    # minConflictIdx = arrivalConflicts[arrivalConflicts.keys[0]]
    # print(list(arrivalConflicts.keys()))

    
    # print(minConflictIdx)

    minConflicts = len(arrivalConflicts[list(arrivalConflicts.keys())[0]])
    
    for conflictIdx in numConflicts:
        if numConflicts[conflictIdx] < minConflicts:
            minConflicts = numConflicts[conflictIdx]
    print(minConflicts)




# n = 5
arrival = [1, 3, 3, 4, 5, 7]
duration = [2, 2, 1, 1, 2, 1]

maxEvents(arrival, duration);