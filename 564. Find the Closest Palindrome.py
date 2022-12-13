class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n)-1)
        sn = int(n)
        mn = int(n)
        while sn != n[::-1] and mn != n[::-1]:
            sn -= 1
            mn += 1
            if str(sn) == str(sn)[::-1]:
                return str(sn)
            elif str(mn) == str(mn)[::-1]:
                return str(mn)
print(Solution().nearestPalindromic("807045053224792883"))