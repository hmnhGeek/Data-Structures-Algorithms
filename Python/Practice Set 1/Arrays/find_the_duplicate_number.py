# Problem link - https://leetcode.com/problems/find-the-duplicate-number/description/
# Solution - https://www.youtube.com/watch?v=49HrEGt6D2s


class Solution:
    @staticmethod
    def find_duplicate_number(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        slow = fast = arr[0]
        while 1:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow


print(Solution.find_duplicate_number([1, 3, 4, 2, 2]))
print(Solution.find_duplicate_number([3, 1, 3, 4, 2]))
print(Solution.find_duplicate_number([3, 3, 3, 3, 3]))
