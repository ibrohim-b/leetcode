class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return command
command = "(al)G(al)()()G"
test = Solution()
print(test.interpret(command))