class Solution:
    @staticmethod
    def get_max_meetings(start_times, end_times):
        meeting_slots = [(start_times[i], end_times[i], i) for i in range(len(start_times))]
        meeting_slots.sort(key=lambda x: x[1])
        meetings_performed = [meeting_slots[0][2], ]
        free_time = meeting_slots[0][1]
        for i in range(1, len(meeting_slots)):
            start_time, end_time, index = meeting_slots[i]
            if start_time > free_time:
                meetings_performed.append(index)
                free_time = end_time
        return meetings_performed


print(Solution.get_max_meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
print(Solution.get_max_meetings([10, 12, 20], [20, 25, 30]))
print(Solution.get_max_meetings([1, 2], [100, 99]))