# Problem link - https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/
# Solution - https://www.youtube.com/watch?v=mKfhTotEguk


class Meeting:
    def __init__(self, start, end, number):
        self.start = start
        self.end = end
        self.number = number


class Solution:
    @staticmethod
    def print_meetings(start_times, end_times):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        # construct all the meetings by zipping start and end times.
        meetings = []
        n = len(start_times)
        for i in range(n):
            meeting = Meeting(start_times[i], end_times[i], i + 1)
            meetings.append(meeting)

        # sort the meetings by end time in O(n * log(n)) time.
        meetings.sort(key=lambda x: x.end)

        # first meeting (after sorting) will always be performed
        performed_meetings = [meetings[0].number,]
        free_time = meetings[0].end

        # now loop from 1st index meeting
        for i in range(1, n):
            meeting = meetings[i]
            # if this meeting can start after free time, add it.
            if meeting.start > free_time:
                performed_meetings.append(meeting.number)
                free_time = meeting.end

        # return the performed meetings.
        return performed_meetings


print(Solution.print_meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
print(Solution.print_meetings([10, 12, 20], [20, 25, 30]))
print(Solution.print_meetings([1, 2], [100, 99]))
