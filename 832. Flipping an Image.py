class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] += 1
                elif image[i][j] == 1:
                    image[i][j] -= 1
        return image
image = [[1,1,0],[1,0,1],[0,0,0]]
Test = Solution()
print(Test.flipAndInvertImage(image))