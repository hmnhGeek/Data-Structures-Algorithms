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
        if i >= n:
            return
        next_apt_index = Solution._find_next(arr, i + 1, n - 1, arr[i][1])
        for j in range(i + 1, next_apt_index):
            print(f"{arr[i]} conflicts with {arr[j]}")
        Solution._solve(arr, next_apt_index, n)
        Solution._solve(arr, i + 1, n)

    @staticmethod
    def find_conflicting_appointments(appointments):
        appointments.sort(key=lambda x: x[0])
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