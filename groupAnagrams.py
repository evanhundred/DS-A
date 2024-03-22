# hackerrank:
#   3940 ms / 5%
#   22.4 MB / 16%
def groupAnagrams(strs):
    stringHashes = {}
    outputArr = []
    
    for str in strs:
        stringHashes[str] = {}
        for char in str:
            if char in stringHashes[str]:
                stringHashes[str][char] +=1
            else:
                stringHashes[str][char] = 1
        matched = False
        for idx, outputStr in enumerate(outputArr):
            # print(stringHashes)
            if stringHashes[outputStr[0]] == stringHashes[str]:
                outputArr[idx].append(str)
                matched = True
                break
        if matched == False:
            outputArr.append([str])
            
    return outputArr

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
strs = [""]
print(groupAnagrams(strs))
strs = ["a"]
print(groupAnagrams(strs))