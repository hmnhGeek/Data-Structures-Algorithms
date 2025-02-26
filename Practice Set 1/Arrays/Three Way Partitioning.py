# Problem link - https://www.geeksforgeeks.org/problems/three-way-partitioning/1
# Solution - https://www.youtube.com/watch?v=LHhskIBz8_M


class Solution:
    @staticmethod
    def three_way_partitioning(arr, a, b):
        # define low, mid and high pointers for the dutch national flag algorithm.
        low, high = 0, len(arr) - 1
        mid = 0

        # while mid <= high (DNF)...
        while mid <= high:
            # if mid-element is < `a`, swap with low and increase both low and mid.
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1

            # elif mid-element > `b`, swap high and mid and decrement only high.
            elif arr[mid] > b:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            else:
                # else if element is between [a, b], only increment mid and do nothing.
                mid += 1

        # finally the array would be three-way partitioned.
        print(arr)


Solution.three_way_partitioning([1, 2, 3, 3, 4], 1, 2)
Solution.three_way_partitioning([1, 4, 3, 6, 2, 1], 1, 3)