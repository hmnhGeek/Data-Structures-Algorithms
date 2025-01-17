class Meeting:
    def __init__(self, start, end, number):
        self.start = start
        self.end = end
        self.number = number


class Solution:
    @staticmethod
    def print_meetings(start_times, end_times):
        meetings = []
        n = len(start_times)
        for i in range(n):
            meeting = Meeting(start_times[i], end_times[i], i + 1)
            meetings.append(meeting)
        meetings.sort(key=lambda x: x.end)
        performed_meetings = [1,]
        free_time = meetings[0].end
        for i in range(1, n):
            meeting = meetings[i]
            if meeting.start > free_time:
                performed_meetings.append(meeting.number)
                free_time = meeting.end
        return performed_meetings


print(Solution.print_meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
print(Solution.print_meetings([10, 12, 20], [20, 25, 30]))
