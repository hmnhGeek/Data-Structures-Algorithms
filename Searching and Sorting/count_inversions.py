# Problem link - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
# Solution - https://www.youtube.com/watch?v=AseUmwVNaoY&t=933s


def bruteforce():
    # The bruteforce approach takes O(n^2) time and O(1) space.
    # The idea is to count all the numbers on the right of ith index which are smaller than ith element.
    def count(arr):
        n = len(arr)
        count_inversion = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count_inversion += 1
        return count_inversion

    print(count([2, 4, 1, 3, 5]))
    print(count([2, 3, 4, 5, 6]))
    print(count([10, 10, 10]))
    print(count([3, 2, 1]))
    print(count([2, 5, 1, 3, 4]))


class CountInversions:
    def __init__(self, arr):
        self.arr = arr
        self.inversions = 0

    def merge(self, low, high):
        mid = int(low + (high - low)/2)
        left = self.arr[low:mid+1]
        right = self.arr[mid+1:high+1]
        i, j = 0, 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # if left array has a greater element than the right array, simply add (len(left) - i) to the
                # inversion count because all elements greater than left[i], i.e., right of `i` will give one
                # pair each to the inversion count.
                self.inversions += (len(left) - i)
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def _merge_sort(self, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        self._merge_sort(low, mid)
        self._merge_sort(mid + 1, high)
        self.arr[low:high+1] = self.merge(low, high)

    def merge_sort(self):
        self._merge_sort(0, len(self.arr) - 1)

    def count_inversions(self):
        # perform a simple merge sort in O(nlog(n)) time and O(n) space.
        self.merge_sort()
        # return the inversion count
        return self.inversions


print(CountInversions([2, 4, 1, 3, 5]).count_inversions())
print(CountInversions([1, 2, 3, 4, 5]).count_inversions())
print(CountInversions([10, 10, 10]).count_inversions())
print(CountInversions([2, 5, 1, 3, 4]).count_inversions())
print(CountInversions([3, 2, 1]).count_inversions())
print(CountInversions([4, 3, 2, 1]).count_inversions())
print(CountInversions([7, 2, 6, 3]).count_inversions())
