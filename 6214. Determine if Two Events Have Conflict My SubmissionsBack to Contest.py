class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        print(int(event1[1][0:2]),int(event2[0][0:2]),int(event1[0][0:2]),int(event2[1][0:2]))
        if int(event1[1][0:2]) >= int(event2[0][0:2]):
            if int(event1[0][0:2]) < int(event2[1][0:2]):
                return True
        else:
            return False"""
        event1[0] = int(event1[0][:-3]) * 60 + int(event1[0][-2:])
        event1[1] = int(event1[1][:-3]) * 60 + int(event1[1][-2:])

        event2[0] = int(event2[0][:-3]) * 60 + int(event2[0][-2:])
        event2[1] = int(event2[1][:-3]) * 60 + int(event2[1][-2:])
        if event1[1] >= event2[0]:
            if event1[0] <= event2[1]:
                return True
        return False
EVENT1 = ["01:15","02:00"]
EVENT2 =["02:00","03:00"]
print(Solution().haveConflict(EVENT1,EVENT2))