# https://neetcode.io/problems/anagram-groups

# hashMap solution:
    # time complexity: O(m * n)
    # space complexity: O(m)
from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        res[tuple(count)].append(word)
    return list(res.values())

# sorting solution:
#   time complexity: O(m * n log n)
#   space complecity: O(m * n)

def groupAnagrams(strs):
    anagramsDict = {}
    for word in strs:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in anagramsDict:
            anagramsDict[sortedWord] = [word]
        else:
            anagramsDict[sortedWord].append(word)
    result = []
    for key in anagramsDict:
        result.append(anagramsDict[key])
    return result
