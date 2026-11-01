# Problem link - https://www.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1
# Solution - https://www.youtube.com/watch?v=2owpaafBIgw


from functools import cmp_to_key


class Solution:
    @staticmethod
    def _comparator(a, b):
        x, y = Solution._get_set_bits_count(a), Solution._get_set_bits_count(b)

        if x < y:
            return 1
        elif x > y:
            return -1
        return 0

    @staticmethod
    def sort_by_set_bits(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """
        arr.sort(key=cmp_to_key(Solution._comparator))
        print(arr)

    @staticmethod
    def _get_set_bits_count(num):
        count = 0
        while num != 0:
            count += (num % 2)
            num = num // 2
        return count


Solution.sort_by_set_bits([5, 2, 3, 9, 4, 6, 7, 15, 32])
Solution.sort_by_set_bits([1, 2, 3, 4, 5, 6])
