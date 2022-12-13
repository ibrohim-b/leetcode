class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if i not in s:
                return ""
        if len(t) > len(s):
            return ""
        elif t == s:
            return t
        def sub_lists(l):
            lists = [[]]
            for i in range(len(l) + 1):
                for j in range(i):
                    lists.append(l[j: i])
            return lists

        sub = sub_lists(s)
        windows = []
        t = sorted(t)
        t = ''.join(t)
        matched_el = 0
        for i in sub:
            ic = sorted(i)[:len(t)]
            ic = ''.join(ic)
            for j in t:
                if j in ic:
                    matched_el += 1
                if matched_el == len(t):
                    windows.append(ic)
                    matched_el = 0
        windows.sort(key=len)
        if len(windows) == 0:
            return s
        return windows[0]
# s = "ADOBECODEBANCKOLI"
# t = "ABC"
#s = "abc"
# t = "ac"
# s = "abc"
# t = "cba"
#s = "bbaa"
#t = "aba"
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
print(Solution().minWindow(s,t))