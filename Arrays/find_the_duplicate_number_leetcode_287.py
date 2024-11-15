# Problem link - https://leetcode.com/problems/find-the-duplicate-number/description/
# Solution - https://www.youtube.com/watch?v=hCIdhv7-5Ms


class DuplicateFinder:
    @staticmethod
    def using_extra_space(arr):
        """
            Overall time complexity is O(n) and overall space complexity is O(n).
        """

        frequencies = dict()
        # This frequencies dictionary will be filled up in O(n) time and will take O(n)
        # space in worst case.
        for i in arr:
            if i not in frequencies:
                frequencies[i] = 1
            else:
                frequencies[i] += 1

        # Additional loop in O(n) time to find the duplicate number.
        for i in frequencies:
            if frequencies[i] > 1:
                return i
        return -1

    @staticmethod
    def using_floyd_cycle_detection(arr):
        """
            This takes O(n) time and O(1) space.
        """

        # start with a slow pointer pointed at index arr[0] (not 0, but .next).
        slow = arr[0]

        # start with a fast pointer pointing at index arr[arr[0]] (.next.next).
        fast = arr[arr[0]]

        # typical Floyd Cycle Detection
        while slow != fast:
            # move slow one at a time.
            slow = arr[slow]
            # move fast two places at a time.
            fast = arr[arr[fast]]

        # reset slow to 0, once slow and fast match
        slow = 0
        while slow != fast:
            # now move both pointers one at a time.
            slow = arr[slow]
            fast = arr[fast]

        # once they again match, that's the index which represents the repeated integer.
        return slow


print(DuplicateFinder.using_extra_space([1, 3, 4, 2, 2]))
print(DuplicateFinder.using_extra_space([3, 1, 3, 4, 2]))
print(DuplicateFinder.using_extra_space([3, 3, 3, 3, 3]))
print()
print(DuplicateFinder.using_floyd_cycle_detection([3, 1, 3, 4, 2]))
print(DuplicateFinder.using_floyd_cycle_detection([3, 3, 3, 3, 3]))
print(DuplicateFinder.using_floyd_cycle_detection([1, 3, 4, 2, 2]))