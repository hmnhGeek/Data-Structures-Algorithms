# Problem link - https://www.geeksforgeeks.org/given-n-appointments-find-conflicting-appointments/
# Solution - https://www.youtube.com/watch?v=OXSmfJ3NdbA&t=165s


class Solution:
    @staticmethod
    def _find_next(arr, low, high, end_time):
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid][0] < end_time:
                low = mid + 1
            elif arr[mid][0] >= end_time:
                high = mid - 1
        return low

    @staticmethod
    def _solve(arr, i, n):
        """
            For each index we are running a loop to print, hence time complexity is O(n^2) and stack space is O(n).
        """

        # if you reach the end, return from recursion stack.
        if i >= n:
            return

        # find the next non-conflicting appointment index using binary search in O(log(n)) time.
        next_apt_index = Solution._find_next(arr, i + 1, n - 1, arr[i][1])

        # now loop on the conflicting appointments and print them in O(n) time.
        for j in range(i + 1, next_apt_index):
            print(f"{arr[i]} conflicts with {arr[j]}")

        # recursively, find the conflicting appointments from the next index
        Solution._solve(arr, i + 1, n)

    @staticmethod
    def find_conflicting_appointments(appointments):
        """
            Time complexity is O(n^2 + n*log(n)) and space complexity is O(n).
        """

        # sort all the appointments by their start times in O(n * log(n))
        appointments.sort(key=lambda x: x[0])
        # recursively print the conflicting appointments
        Solution._solve(appointments, 0, len(appointments))


Solution.find_conflicting_appointments(
    [
        [1, 5],
        [3, 7],
        [2, 6],
        [10, 15],
        [5, 6],
        [4, 100]
    ]
)
