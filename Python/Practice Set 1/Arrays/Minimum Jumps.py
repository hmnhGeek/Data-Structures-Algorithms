# Problem link - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
# Solution - https://www.youtube.com/watch?v=fyQpHH3rP_0


class Solution:
    @staticmethod
    def get_min_jumps(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # base cases
        n = len(arr)
        if n == 0:
            return -1
        if n == 1:
            return 0

        # max reach denotes the maximum index that can be reached within a range.
        max_reach = 0

        # the last index after making a jump
        last_index = 0

        # jumps count
        jumps = 0

        # loop on the indices
        for i in range(n):
            # update the max reach
            max_reach = max(max_reach, i + arr[i])

            # if i = last index, it is time to make a jump
            if i == last_index:
                # however, if i = max reach then no further jumps can be made, return -1
                if max_reach == i:
                    return -1

                # else make the jump and update the last index from previous range.
                last_index = max_reach
                jumps += 1

                # if you can reach the end already, simply return the jumps count
                if max_reach >= n - 1:
                    return jumps

        # finally return the jumps count.
        return jumps
    

print(Solution.get_min_jumps([1, 2, 3, 1, 1, 0, 2, 5]))
print(Solution.get_min_jumps([1, 2, 4, 1, 1, 0, 2, 5]))
print(Solution.get_min_jumps([1, 4, 3, 2, 6, 7]))
print(Solution.get_min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(Solution.get_min_jumps([0, 10, 20]))
print(Solution.get_min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution.get_min_jumps([2, 3, 1, 1, 4]))
print(Solution.get_min_jumps([2, 3, 0, 1, 4]))
