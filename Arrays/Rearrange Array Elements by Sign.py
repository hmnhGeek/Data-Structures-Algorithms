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
        positives = []
        negatives = []
        Solution._segregate_positives_negatives(arr, positives, negatives)
        i = 0
        insert_positives = True
        x, y = 0, 0
        while i < len(arr):
            if insert_positives:
                if x in range(len(positives)):
                    arr[i] = positives[x]
                    x += 1
                    i += 1
            else:
                if y in range(len(negatives)):
                    arr[i] = negatives[y]
                    y += 1
                    i += 1
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
