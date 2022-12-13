class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lists = [[]]
        max = 0
        for i in range(len(s) + 1):
            for j in range(i):
                if s[j: i] not in lists and self.is_valid_parentheses(s[j: i]):
                    lists.append(s[j: i])
                    if max < len(s[j: i]):
                        max = len(s[j: i])
        return max
    def is_valid_parentheses(self, s):
        if s[0] == ")" or s[-1] == "(":
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif len(stack) == 0 or (s[i] != ")" and stack[-1] == "("):
                return False
            else:
                stack.pop(-1)
        return len(stack) == 0
s = "((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))"
print(Solution().longestValidParentheses(s))