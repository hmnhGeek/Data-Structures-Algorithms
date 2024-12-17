class Solution:
    @staticmethod
    def single_element(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).

            You might ask why check where the duplicate number is lying. Can't we directly check where there are odd
            number of elements and move to that side for getting the single element? No, we cannot! Dry run on this case
            low           mid            high
            4              5              5

            In this case both sides actually have even number of elements. Where should we move now? :)
        """

        # if the array is empty, return -1.
        if len(arr) == 0:
            return -1

        # if array has only a single element, return 0th element.
        if len(arr) == 1:
            return arr[0]

        # if first element is single, return it.
        if arr[0] != arr[1]:
            return arr[0]

        # if last element is single, return it.
        if arr[-1] != arr[-2]:
            return arr[-1]

        # define a search space from second index till n - 3, because we have checked for the edges already.
        low, high = 2, len(arr) - 3

        # typical Binary Search
        while low <= high:
            mid = int(low + (high - low)/2)

            # if the mid-element is single, return it.
            if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]:
                return arr[mid]

            # if mid-element is not single, check on which side it's duplicate lies.

            # if the duplicate lie on left side
            if arr[mid - 1] == arr[mid]:
                # exclude the duplicate numbers (subtract -2) from (mid - low + 1) and check if the left side has even
                # numbers. If yes, then single element cannot lie there, move to the right half.
                if (mid - low + 1 - 2) % 2 == 0:
                    low = mid + 1
                else:
                    # if after excluding duplicate numbers the left side has odd numbers, the single element must be
                    # on left side.
                    high = mid - 1
            else:
                # similarly, if the duplicate number lie on the right half, and after excluding the duplicate number
                # from right side, there are even numbers on the right side, then the single element cannot lie on the
                # right side, move to lower half.
                if (high - mid + 1 - 2) % 2 == 0:
                    high = mid - 1
                else:
                    # if there are odd numbers on the right side even after excluding the duplicate number, then the
                    # single element must lie on right half.
                    low = mid + 1

        # return -1 if no single element was found.
        return -1


print(Solution.single_element([3, 3, 7, 7, 10, 11, 11]))
print(Solution.single_element([1, 1, 2, 2, 4, 5, 5]))
print(Solution.single_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.single_element([1, 1, 4, 4, 15]))
print(Solution.single_element([1, 1, 3, 5, 5]))
print(Solution.single_element([1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]))
print(Solution.single_element([1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]))
