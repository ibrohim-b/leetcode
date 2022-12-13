"""class Solution(object):
    def diagonalSum(self, mat):
        numbers = []
        for i in range(len(mat)):
            numbers.append(mat[i][i])
        for i in range(len(mat)):
            mat[i] = mat[i][::-1]
        for i in range(len(mat)):
            numbers.append(mat[i][i])
        if len(mat)%2 == 1:
            duplicate_n = int(round(len(mat)/2)-1)
            numbers.pop(duplicate_n)
        return sum(numbers)"""
class Solution(object):
    def diagonalSum(self, mat):
        numbers = []
        m = len(mat)
        for i in range(m):
            numbers.append(mat[i][i])
            numbers.append(mat[i][m-i+1])
        return sum(numbers)
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().diagonalSum(mat))