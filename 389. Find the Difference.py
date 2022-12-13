class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        length = len(s)
        for i in range(length):
            if s[i] in t:
                t = list(t)
                t.pop(t.index(s[i]))
                t = ''.join(t)
                s = list(t)
                s.pop(i)
                s = ''.join(s)
                length -= 1
        return t[0]
s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s,t))