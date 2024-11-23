def solve(arr, index, current_sum, count):
    # Base case: If we've gone through all elements, return
    if index >= len(arr):
        return

    # Update the current sum
    current_sum += arr[index]

    # If the current sum is 0, we've found a subarray
    if current_sum == 0:
        count[0] += 1

    # Recurse for the next element
    solve(arr, index + 1, current_sum, count)


def zero_sum_subarray_count(arr):
    """
        Finds the total count of subarrays with a sum equal to 0 using recursion.

        Time Complexity:
            - Outer Loop: O(n)
              The outer loop iterates through each index of the array, starting a new subarray from every index.
            - Recursive Calls: O(n^2)
              For a given starting index, the recursion explores all subarrays extending to the end of the array.
              The total number of recursive calls is the sum of the first `n` natural numbers:
              n + (n-1) + (n-2) + ... + 1 = n(n+1)/2, which is O(n^2).
            - Overall Time Complexity: O(n^2)

        Space Complexity:
            - Recursive Stack: O(n)
              The maximum depth of the recursive stack occurs when processing the longest subarray (starting at index 0).
            - Auxiliary Space: O(1)
              Apart from the recursion stack, no additional space is used except for variables like `current_sum` and the `count` list.
            - Overall Space Complexity: O(n)

        Args:
            arr (List[int]): The input array of integers.

        Returns:
            int: The total count of subarrays with a sum equal to 0.
        """
    n = len(arr)
    count = [0]

    # Start a new subarray from every index
    for i in range(n):
        solve(arr, i, 0, count)

    return count[0]


# Test cases
print(zero_sum_subarray_count([6, -1, -3, 4, -2, 2, 4, 6, -12, -7]))  # Output: 4
print(zero_sum_subarray_count([0, 0, 5, 5, 0, 0]))  # Output: 6
