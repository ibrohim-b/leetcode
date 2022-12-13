class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        length = len(moves)
        if length %2 == 0:
            length += 1
        matrix = [[0]*length for _ in range(length)]
        matrix[round(length/2)-1][round(length/2)-1] = 2
        print(matrix)
        x = round(length/2)-1
        y = round(length/2)-1
        position = [x,y]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                for move in moves:
                    if move == 'L':
                        position = position[x,y-1]
                    if move == "R":
                        position = position[x,y+1]
                    if move == "U":
                        position = position[x+1, y]
                    if move == "D":
                        position = position[x-1, y]
                matrix[position[0]][position[1]] = 1
            print(matrix)
moves = "LL"
print(Solution().judgeCircle(moves))