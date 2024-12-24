# Problem link - https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# Solution - https://www.youtube.com/watch?v=mKfhTotEguk


class Solution:
    @staticmethod
    def get_max_meetings(start_times, end_times):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        # create n sized array having all the meeting information
        meeting_slots = [(start_times[i], end_times[i], i) for i in range(len(start_times))]
        # sort the meetings by end time in O(nlog(n)) time.
        meeting_slots.sort(key=lambda x: x[1])
        # add the first meeting because the shortest one can always be performed
        meetings_performed = [meeting_slots[0][2], ]
        # set the free time as the end time of first (0th) meeting.
        free_time = meeting_slots[0][1]

        # now start looping from 1st index.
        for i in range(1, len(meeting_slots)):
            start_time, end_time, index = meeting_slots[i]
            # check if this meeting can be performed if its start time is post the free time of the meeting room
            if start_time > free_time:
                # if yes, then update the free time and add the meeting index.
                meetings_performed.append(index)
                free_time = end_time

        # return the meetings performed.
        return meetings_performed


print(Solution.get_max_meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
print(Solution.get_max_meetings([10, 12, 20], [20, 25, 30]))
print(Solution.get_max_meetings([1, 2], [100, 99]))