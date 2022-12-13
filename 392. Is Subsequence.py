class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_l = []
        t_l = []
        for i in s:
            s_l.append(i)
        for i in t:
            t_l.append(i)
        matches = 0
        for i in range(len(s_l)):
            if s_l[i] == t_l[i]:
                matches+= 1
            else:
                for j in range(len(t_l)):
                    if s_l[i] == t_l[j]:
                        matches += 1
        return matches == len(s)
s = "axc"
t = "ahbgdc"
Test = Solution()
print(Test.isSubsequence(s,t))
