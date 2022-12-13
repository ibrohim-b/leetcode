class Solution(object):
    def divideString(self, s, k, fill):
        import textwrap
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        if len(s)%k!=0:
            while len(s)%k!=0:
                s += fill
        return textwrap.wrap(s, k)


s = "abcde"
k = 3
fill = "x"
Test = Solution()
print(Test.divideString(s,k,fill))