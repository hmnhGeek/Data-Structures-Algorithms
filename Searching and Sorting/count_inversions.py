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

bruteforce()