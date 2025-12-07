# Problem link - https://www.naukri.com/code360/problems/smallest-divisor-with-the-given-limit_1755882
# Solution - https://www.youtube.com/watch?v=UvBKTVaG6U8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=15


from math import ceil


class Solution:
    @staticmethod
    def find_smallest_divisor(arr, threshold):
        """
            Time complexity is O(n * log(max)) and space complexity is O(1).
        """
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            quotient_sum = Solution.get_quotient_sum(arr, mid)
            if quotient_sum <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    @staticmethod
    def get_quotient_sum(arr, mid):
        _sum = 0
        for i in arr:
            _sum += ceil(i/mid)
        return _sum
    

print(Solution.find_smallest_divisor([1, 2, 5, 9], 6))
print(Solution.find_smallest_divisor([1, 2, 3, 4, 5], 8))
print(Solution.find_smallest_divisor([8, 4, 2, 3], 10))
print(Solution.find_smallest_divisor([2, 3, 5, 7, 11], 11))
print(Solution.find_smallest_divisor([44, 22, 33, 11, 1], 5))
print(Solution.find_smallest_divisor([1, 1, 1, 1], 4))
