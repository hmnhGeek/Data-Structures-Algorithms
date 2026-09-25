# Problem link - https://www.geeksforgeeks.org/dsa/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/


class Solution:
    @staticmethod
    def count_frequent(arr, k):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        mp = {i: 0 for i in arr}
        for i in arr:
            mp[i] += 1
        n = len(arr)
        threshold = n // k
        count = 0
        for i in mp:
            if mp[i] > threshold:
                count += 1
        return count


print(Solution.count_frequent([3, 4, 2, 2, 1, 2, 3, 3], 4))
print(Solution.count_frequent([9, 10, 7, 9, 2, 9, 10], 3))
