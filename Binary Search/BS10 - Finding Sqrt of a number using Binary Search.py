# Problem link - https://www.naukri.com/code360/problems/square-root-integral_893351?leftPanelTab=0%3Futm_source%3Dyoutube
# Solution - https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


class Solution:
    @staticmethod
    def find_square_root(x):
        """
            Time complexity is O(log(x)) and space complexity is O(1).
        """

        if x < 0:
            return -1

        # define the search space of the binary search. The root of x will lie between [0, x].
        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)
            # if the mid-value is the square root, i.e., x is a perfect square, return mid.
            if mid * mid == x:
                return mid

            # if the square value is greater than target, reduce the range from right side.
            if mid * mid > x:
                high = mid - 1
            # else reduce the range from left side.
            else:
                low = mid + 1

        # finally, high will always point to the nearest square root of x.
        return high


print(Solution.find_square_root(30))
print(Solution.find_square_root(25))
print(Solution.find_square_root(35))
print(Solution.find_square_root(6))
print(Solution.find_square_root(100))
print(Solution.find_square_root(1))
print(Solution.find_square_root(0))
print(Solution.find_square_root(-100))
print(Solution.find_square_root(225))
