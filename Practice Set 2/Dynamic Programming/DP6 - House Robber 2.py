# Problem link - https://www.naukri.com/code360/problems/house-robber_839733?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=3WaxQMELSkw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=7


class Solution:
    @staticmethod
    def __house_robber(arr):
        n = len(arr)
        prev1 = prev2 = 0
        for index in range(n):
            left = arr[index] + prev2
            right = prev1
            curr = max(left, right)
            prev2 = prev1
            prev1 = curr
        return prev1

    @staticmethod
    def get_circular_house_robber(arr):
        # Overall time complexity is O(2n) and space complexity is O(1).
        # get the max loot from houses 1-(n-1) or 0-(n-2) to avoid first and last house to be together.
        return max(Solution.__house_robber(arr[1:]), Solution.__house_robber(arr[:-1]))


print(Solution.get_circular_house_robber([2, 3, 2]))
print(Solution.get_circular_house_robber([1, 3, 2, 1]))
print(Solution.get_circular_house_robber([1, 5, 1, 2, 6]))
print(Solution.get_circular_house_robber([2, 3, 5]))
print(Solution.get_circular_house_robber([1, 3, 2, 0]))