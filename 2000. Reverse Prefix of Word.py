class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        result = ""
        word = word.replace(ch,"_")
        for i in range(len(word)):
            if word[i] == "_":
                result += word[0:i+1]
                word = word[i+1:]
                break
        result = result[::-1] + word
        result = result.replace("_",ch)
        return result
word = "abcdefd"
ch = "d"
test = Solution()
print(test.reversePrefix(word,ch))