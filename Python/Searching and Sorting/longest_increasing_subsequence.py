# Problem link - https://leetcode.com/problems/longest-increasing-subsequence/description/
# Solution - https://www.youtube.com/watch?v=on2hvxBXJH4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=44


def binary_search(arr, elem):
    """

    :param arr: array in which the element is to be searched
    :param elem: integer that needs to be searched in the array
    :return: the index from the array of that element which is either equal to or just greater than this element
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] >= elem:
            high = mid - 1
        else:
            low = mid + 1
    return low


def get_longest_increasing_subsequence(arr):
    """
    Overall time complexity is O(nlog(n)) and space complexity is O(n).
    :param arr: A list of integers in any order.
    :return: The length of the longest increasing subsequence from the list.
    """

    # create a blank list to store elements while traversing the list. It will occupy O(n) space in worst case.
    result = []

    # traverse in the list - This will take O(n) time; thus it will take O(nlog(n)) time.
    for elem in arr:
        # in the result list, get the index of the element that is equal to or just greater than the element from this
        # array. In the worst case, the result array will store all the elements from the array `arr` if `arr` is
        # already sorted. Hence, we can assume O(log(n)) time here.
        index_to_insert_at = binary_search(result, elem)

        # if the index is just out of bounds, append the element
        if index_to_insert_at == len(result):
            result.append(elem)
        else:
            # else update the index value in the result array with this element.
            result[index_to_insert_at] = elem

    # finally, return the length of this result array.
    return len(result)


print(get_longest_increasing_subsequence([1, 7, 8, 4, 5, 6, -1, 9]))
print(get_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
print(get_longest_increasing_subsequence([1, 2, 2]))
print(get_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(get_longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))
print(get_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
