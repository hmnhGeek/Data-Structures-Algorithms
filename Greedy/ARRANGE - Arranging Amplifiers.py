class Solution:
    @staticmethod
    def arrange(arr):
        ones = 0
        n = len(arr)
        for i in range(n):
            if arr[i] == 1:
                ones += 1
        arr.sort(reverse=True)
        result = [1]*ones
        if n - ones == 2 and arr[0] == 3 and arr[1] == 2:
            result.append(2)
            result.append(3)
        else:
            for i in range(n - ones):
                result.append(arr[i])
        return result


print(Solution.arrange([5, 6, 4]))
print(Solution.arrange([2, 3]))
