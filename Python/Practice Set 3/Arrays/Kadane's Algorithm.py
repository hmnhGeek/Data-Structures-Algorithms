# Problem link - https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Solution - https://www.youtube.com/watch?v=HCL4_bOd3-4


class Solution:
    @staticmethod
    def kadane(arr):
        """
            Time complexity is O(n) and space complexity is O(1).

            Find the maximum sum subarray using Kadane's algorithm and also return the subarray.

            This version keeps track of start and end indices of the maximum subarray
            by maintaining two types of indices:

            - s (temporary start): candidate starting index of the subarray currently being tested.
              Whenever we decide it's better to start fresh at the current element arr[i]
              (i.e., arr[i] > curr_sum + arr[i]), we reset curr_sum = arr[i] and set s = i.

            - start, end (committed indices): true start and end of the best subarray found so far.
              We only update them when curr_sum > result, i.e., we have discovered a better subarray.

            This separation ensures correctness in edge cases like all-negative arrays.
            If we updated start immediately on every reset, we'd overshoot the true max element.

            Example:
                arr = [-2, -4]
                Walkthrough:
                    i=0: curr_sum = -2, result = -2, start=0, end=0, s=0
                    i=1: arr[1] = -4
                         Compare arr[i] vs curr_sum+arr[i]: -4 > -6 → restart
                         curr_sum = -4, s = 1
                         curr_sum > result? -4 > -2 → no
                Final result = -2, subarray = [-2]

            Args:
                arr (List[int]): Input array (may contain negative numbers).

            Returns:
                Tuple[int, List[int]]:
                    - Maximum subarray sum
                    - The subarray itself
        """
        curr_sum = arr[0]
        result = arr[0]
        start = end = s = 0
        for i in range(1, len(arr)):
            if arr[i] > curr_sum + arr[i]:
                curr_sum = arr[i]
                s = i
            else:
                curr_sum += arr[i]
            if curr_sum > result:
                result = curr_sum
                start = s
                end = i
        return result, arr[start:end+1]


print(Solution.kadane([2, 3, -8, 7, -1, 2, 3]))
print(Solution.kadane([-2, -4]))
print(Solution.kadane([5, 4, 1, 7, 8]))
