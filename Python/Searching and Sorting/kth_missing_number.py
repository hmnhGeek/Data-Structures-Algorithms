# Problem link - https://www.naukri.com/code360/problems/kth-missing-element_893215
# Solution video - https://www.youtube.com/watch?v=uZ0N_hZpyps&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17

def trial_solutions():
    def bruteforce(arr, k):
        '''
            This code takes O(n) time and O(n) space (for set).
        '''

        # converting to set so that "not in" operation is amortized O(1).
        set_arr = set(arr)

        # counter to store incremental count till k.
        counter = 0
        last_found = None

        # iterate on the range from 1 to max(arr).
        for i in range(1, max(set_arr)):
            # if counter has become k, return whatever is set in last_found.
            if counter == k:
                return last_found

            # if i is not in set, increase the counter and set last_found.
            if i not in set_arr:
                counter += 1
                last_found = i

        return None


    def get_nums_smaller_than(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = int(low + (high - low)/2)

            if arr[mid] == target:
                # if target is present in the array, return its index and True
                return mid, True

            # otherwise, the idea is to get `low` value, representing the number
            # of missing numbers before mid in the given array arr.
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low, False


    def get_kth_missing_number(arr, k):
        # This will take O(log(max(arr)) * log(n)) time and O(1) space.
        low, high = 1, max(arr)

        while low <= high:
            mid = int(low + (high - low)/2)

            smaller_count, is_in_arr = get_nums_smaller_than(arr, mid)
            if not is_in_arr:
                # if mid is the kth missing number, return mid
                if mid - smaller_count == k:
                    return mid
                elif mid - smaller_count < k:
                    # if mid is a missing number, but it is less than kth missing,
                    # we must increase low so that mid can also increase.
                    low = mid + 1
                else:
                    # if mid is a missing number, but it is more than kth missing,
                    # we must decrease high so that mid can also decrease.
                    high = mid - 1
            else:
                # if mid is present in the array but mid - (number of elements in array
                # which are smaller than mid) is less than equal to k, we must increase
                # low.
                if mid - smaller_count <= k:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


    print(get_kth_missing_number([2, 3, 4, 7, 11], 5))
    print(get_kth_missing_number([2, 4, 5, 7], 3))
    print(get_kth_missing_number([4, 7, 9, 10], 1))
    print(get_kth_missing_number([4, 7, 9, 10], 4))


def main():
    # This approach will take O(log(n)) time and O(1) space.
    def get_missing_kth_number(arr, k):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = int(low + (high - low)/2)

            # the number of missing integers before index mid is
            # arr[mid] - (mid + 1), you can check by dry running.
            missing_count = arr[mid] - (mid + 1)
            if missing_count < k:
                low = mid + 1
            else:
                high = mid - 1

        # high will be at lower range of missing number now, and
        # we need missing amount to add in lower range to obtain
        # k. So we can say, missing kth number = arr[high] + (k - high).
        # Also, arr[high] - high = low, if you verify. Hence, missing
        # number is low + k. We have to eliminate arr[high] from the formula
        # because in certain cases, high might get out of bounds.
        return low + k

    print(get_missing_kth_number([2, 3, 4, 7, 11], 5))
    print(get_missing_kth_number([2, 4, 5, 7], 3))
    print(get_missing_kth_number([4, 7, 9, 10], 1))
    print(get_missing_kth_number([4, 7, 9, 10], 4))

main()