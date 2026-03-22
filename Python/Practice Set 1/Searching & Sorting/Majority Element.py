class Solution:
    @staticmethod
    def find_majority_element(arr):
        count = 0
        elem = None
        possible_count = 0
        for i in range(len(arr)):
            if count == 0:
                elem = arr[i]
                count = 1
                continue
            if elem == arr[i]:
                count += 1
            else:
                count -= 1
        for i in range(len(arr)):
            if arr[i] == elem:
                possible_count += 1
        if possible_count > len(arr) // 2:
            return elem
        return None


print(Solution.find_majority_element([3, 1, 3, 3, 2]))
print(Solution.find_majority_element([7]))
print(Solution.find_majority_element([2, 13]))
print(Solution.find_majority_element([3, 2, 3]))
print(Solution.find_majority_element([2, 2, 1, 1, 1, 2, 2]))
