def restoreIpAddresses(s: str):
    '''
        Given the constraints, the worst-case number of recursive calls can be approximated as O(3^4)
        per valid segment, where each segment can be processed in O(1) time. Since the maximum length
        of the string is n (12 in worst case), overall complexity considering all recursions is O(n*3^4)
        which is O(n).

        At each level of recursion, the current path (which stores up to 4 segments) is passed.
        The space required for this path is O(4) = O(1); The result list stores all valid IP addresses.
        In the worst case, there can be several valid IP addresses, but this storage is required for the final output.

        Overall time complexity is O(n).
        Overall space complexity is O(len(result)) + O(1).
    '''


    def is_valid(segment):
        # Check if the segment is a valid IP segment.
        # A segment is valid if it is of length = 1 (even 0 is acceptable in this case)
        # or if the length is > 1 there should be no leading zeroes and the number
        # should be less than 255.
        return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

    def backtrack(start=0, path=[]):
        # If we have 4 segments, and we are at the end of the string, add the path to results
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return

        # If we have 4 segments, and we are not at the end of the string, return
        # because if we did not, then it means there will be a 5th part, which
        # will not be a valid IP address.
        if len(path) == 4:
            return

        # Try all possible splits. This will be achieved by starting from the
        # next index from `start`. Whichever `end` index comes first, i.e.,
        # start + 4 or len(s) + 1, use that as the end index.
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            # extract the segment and validate if it is a valid segment or not,
            # if yes, then the next segment to check will start from end index.
            # Call the `backtrack()` function with end index (as the new start
            # index) and append the segment to the collected valid paths till now.
            segment = s[start:end]
            if is_valid(segment):
                backtrack(end, path + [segment])

    result = []
    backtrack()
    return result


print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("101023"))