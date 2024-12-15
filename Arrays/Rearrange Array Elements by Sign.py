# Problem link - https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/#expected-approach-using-two-pointers-on-time-and-on-space


class Solution:
    @staticmethod
    def _segregate_positives_negatives(arr, positives, negatives):
        for i in range(len(arr)):
            if arr[i] >= 0:
                positives.append(arr[i])
            else:
                negatives.append(arr[i])

    @staticmethod
    def rearrange(arr):
        """
            Overall time complexity is O(2n) and space complexity is O(n).
        """

        # get positive and negative numbers from the original array into two separate arrays in O(n) time and O(n)
        # space.
        positives = []
        negatives = []
        Solution._segregate_positives_negatives(arr, positives, negatives)

        # set `i` for the original array as 0.
        i = 0
        # start with inserting positive integer first
        insert_positives = True
        # keep 0 pointers for both the positive and negative arrays.
        x, y = 0, 0

        # This loop will run for another O(n) time.
        while i < len(arr):
            # positive needs to be inserted
            if insert_positives:
                if x in range(len(positives)):
                    arr[i] = positives[x]
                    x += 1
                    i += 1
            else:
                # else if negative needs to be inserted.
                if y in range(len(negatives)):
                    arr[i] = negatives[y]
                    y += 1
                    i += 1
            # toggle the insertion flag.
            insert_positives = not insert_positives


# Example 1
arr = [1, 2, 3, -4, -1, 4]
Solution.rearrange(arr)
print(arr)

# Example 2
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
Solution.rearrange(arr)
print(arr)

# Example 3
arr = [3,1,-2,-5,2,-4]
Solution.rearrange(arr)
print(arr)

# Example 4
arr = [-1,1]
Solution.rearrange(arr)
print(arr)

# Example 5
arr = [1,2,-4,-5]
Solution.rearrange(arr)
print(arr)

# Example 6
arr = [1,2,-3,-1,-2,3]
Solution.rearrange(arr)
print(arr)
