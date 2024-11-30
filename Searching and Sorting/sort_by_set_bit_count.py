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
        """
            Overall time complexity is O(n * log(max(arr))) and space complexity is O(max(set_bit_count)).
        """

        # initialize a hash map which will store all the set bits count and an array of elements with that set bit count
        hash_map = {}

        # store min and max set bits count, to use them as range later.
        min_set_bit, max_set_bit = 1e6, -1e6

        # loop on the arr in O(n) time. Worse, this will take O(n * log(max(arr))).
        for i in arr:
            # get the set bits count of this `i` in O(log(i)) time.
            set_bits = Solution._count_set_bits(i)

            # update the range
            min_set_bit = min(min_set_bit, set_bits)
            max_set_bit = max(max_set_bit, set_bits)

            # add `i` to its appropriate place in the hash map.
            if set_bits not in hash_map:
                hash_map[set_bits] = [i]
            else:
                hash_map[set_bits].append(i)

        # SORTING THE ARRAY FROM HERE

        # set index = 0 to update the array.
        index = 0

        # set start bits to max set bit because we want decreasing order sort.
        start_bit = max_set_bit

        # while start bit is not yet the minimum bit. This will take O(n) time.
        while start_bit != min_set_bit:
            # push all the elements (the order from original array is maintained) into the arr.
            for i in hash_map[start_bit]:
                arr[index] = i
                index += 1
            # move to the next lower set bit count.
            start_bit -= 1

        # do the same for the minimum bit count.
        for i in hash_map[start_bit]:
            arr[index] = i
            index += 1
        print(arr)
        print()


Solution.sort_by_set_bit([5, 2, 3, 9, 4, 6, 7, 15, 32])
Solution.sort_by_set_bit([1, 2, 3, 4, 5, 6])
Solution.sort_by_set_bit([0, 1, 2, 3, 4, 5, 6, 7, 8])
Solution.sort_by_set_bit([2, 4, 8])
Solution.sort_by_set_bit([4, 3, 8])
