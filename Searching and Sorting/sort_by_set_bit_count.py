class Solution:
    @staticmethod
    def _count_set_bits(x):
        count = 0
        while x != 0:
            count += 1 if x % 2 == 1 else 0
            x = x // 2
        return count

    @staticmethod
    def sort_by_set_bit(arr):
        hash_map = {}
        min_set_bit, max_set_bit = 1e6, -1e6
        for i in arr:
            set_bits = Solution._count_set_bits(i)
            min_set_bit = min(min_set_bit, set_bits)
            max_set_bit = max(max_set_bit, set_bits)
            if set_bits not in hash_map:
                hash_map[set_bits] = [i]
            else:
                hash_map[set_bits].append(i)

        index = 0
        start_bits = max_set_bit
        while start_bits != min_set_bit:
            for i in hash_map[start_bits]:
                arr[index] = i
                index += 1
            start_bits -= 1
        for i in hash_map[start_bits]:
            arr[index] = i
            index += 1
        print(arr)
        print()


Solution.sort_by_set_bit([5, 2, 3, 9, 4, 6, 7, 15, 32])
Solution.sort_by_set_bit([1, 2, 3, 4, 5, 6])
