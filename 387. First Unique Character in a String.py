class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = []
        duplicate_c = []
        if len(s) == 2 and s[0] == s[1]:
            return -1
        elif len(s) == 2 and s[0] != s[1]:
            return 0
        for i in s:
            characters.append(i)
        length = len(characters)
        characters2 = list(dict.fromkeys(characters))
        if len(characters2) == 2:
            return -1
        for i in s:
            if i not in duplicate_c:
                duplicate_c.append(i)
                s = s.replace(i,"",1)
        for i in s:
            if i in duplicate_c:
                duplicate_c.remove(i)
        for i in range(len(characters)):
            if duplicate_c[0] == characters[i]:
                return i
s = 'bd'
Test = Solution()
print(Test.firstUniqChar(s))