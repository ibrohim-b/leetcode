class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry=  0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):
            CharA = ord(a[i]) - ord("0") if i < len(a) else 0
            CharB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = CharA + CharB + carry
            char = str(total %  2)
            res = char + res
            carry  = total // 2
        if carry:
            res = '1' + res
        return res



a = "10100"
b = "1"
print(Solution().addBinary(a,b))