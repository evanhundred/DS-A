# https://leetcode.com/problems/reshape-the-matrix/
# LeetCode 566 - Reshape the Matrix

def matrixReshape(mat, r, c):
    totalItems = len(mat) * len(mat[0])
    if totalItems != r * c:
        return mat

    result = []

    for row in range(r):
        result.append([])

    matIdx = 0
    resultRow = 0
    matRow = 0
    matCol = 0

    while matIdx < totalItems:
        if matCol == len(mat[matRow]):
            matRow += 1
            matCol = 0

        if len(result[resultRow]) < c:
            result[resultRow].append(mat[matRow][matCol])
            matCol += 1
            matIdx += 1
        else:
            resultRow += 1

    return result


print(matrixReshape([[1, 2], [3, 4]], r=1, c=4)) # [[1, 2, 3, 4]]
print(matrixReshape([[1, 2], [3, 4]], r=2, c=4)) # [[1,2], [3,4]]
