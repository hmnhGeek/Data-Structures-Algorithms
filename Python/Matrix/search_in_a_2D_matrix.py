# Problem link - https://leetcode.com/problems/search-a-2d-matrix/description/


class Sorted2DMatrix:
    def __init__(self, matrix):
        self.mtx = matrix
        self.r = len(matrix)
        self.c = len(matrix[0])

    def _elem_at_mid(self, mid):
        # do a dry run, and you will find that flattened[mid] = matrix[mid//num_cols][mid % num_cols]
        return self.mtx[mid//self.c][mid % self.c]

    def contains(self, element):
        # consider the matrix as a flattened array. low would point to 0th index of that virtual array and high would
        # point to the n*m - 1 index of that flattened array. Since the flattened array would be sorted, perform a
        # simple binary search which would take O(log(n*m)) time.
        low = 0
        high = self.r*self.c - 1

        while low <= high:
            mid = int(low + (high - low)/2)

            # find the element at mid
            mid_element = self._elem_at_mid(mid)

            if mid_element == element:
                # if found return true.
                return True
            elif mid_element > element:
                high = mid - 1
            else:
                low = mid + 1

        # if the element was not found, return False
        return False


print(Sorted2DMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]]).contains(3))
print(Sorted2DMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]]).contains(13))
print(Sorted2DMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]).contains(8))
print(Sorted2DMatrix([[1, 2, 4], [6, 7, 8], [9, 10, 34]]).contains(78))