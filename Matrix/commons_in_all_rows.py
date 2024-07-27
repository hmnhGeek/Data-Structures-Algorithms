# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/

def commons_in_all(mtx):
    '''
        Overall time complexity is O(n*m).
        Overall space complexity is O(m).
    '''

    # takes O(m) space
    hash_set = set(mtx[0])
    # takes another O(m) space in worst case
    non_answer = set()

    n, m = len(mtx), len(mtx[0])

    # Overall this will take O(n*m) time.
    for i in range(1, n):
        # takes O(m) time to iterate in hash_set
        for val in hash_set:
            # if the value is not in the ith row, add it to non_answer set
            if val not in mtx[i]:
                # amortized O(1) time
                non_answer.add(val)

    # finally return only those elements from hash_set which are not in non_answer.
    # This will take O(m) time.
    return hash_set.difference(non_answer)

print(
    commons_in_all(
        [[1, 2, 1, 4, 8],
         [3, 7, 8, 5, 1],
         [8, 7, 7, 3, 1],
         [8, 1, 2, 7, 9]]
    )
)