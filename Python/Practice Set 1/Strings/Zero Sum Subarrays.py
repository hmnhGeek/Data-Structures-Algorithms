# Problem link - https://www.geeksforgeeks.org/problems/zero-sum-subarrays1825/1
# Solution - https://www.youtube.com/watch?v=xvNwoz-ufXA


class Solution:
    @staticmethod
    def find_zero_sum_subarrays(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        mp = {0: 1}
        _sum = count = 0
        for i in range(len(arr)):
            _sum += arr[i]
            if _sum - 0 in mp:
                count += mp[_sum - 0]
            if _sum in mp:
                mp[_sum] += 1
            else:
                mp[_sum] = 1
        return count


print(Solution.find_zero_sum_subarrays([0, 0, 5, 5, 0, 0]))
print(Solution.find_zero_sum_subarrays([6, -1, -3, 4, -2, 2, 4, 6, -12, -7]))
print(Solution.find_zero_sum_subarrays([0]))
