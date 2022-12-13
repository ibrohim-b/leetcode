class Solution(object):
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        index_x = 0
        index_y = 0
        new_matrix = []
        List = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                List.append(matrix[index_x][index_y])
                new_matrix.append(List)
                index_x += 1
                #print(List)
            List = []
            index_x = 0
            index_y += 1
        result = []
        for i in new_matrix:
            if i not in result:
                result.append(i)
        new_matrix = []
        for i in range(len(result)):
            new_matrix.append(result[i][::-1])
        matrix = new_matrix.copy()
        return matrix


matrix =[[1,2,3],[4,5,6],[7,8,9]]
Test = Solution()
print(Test.rotate(matrix))