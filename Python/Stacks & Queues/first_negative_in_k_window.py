# Problem link - https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def enqueue(self, x):
        node = Node(x)

        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return
        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        if self.is_empty():
            return
        return self.head.data


def first_negative(arr, k):
    # Overall time complexity is O(n - k) and space complexity is O(n - k + 1 + k) {+k for queue}.
    # And n - k + 1 for the result array - O(n).

    n = len(arr)

    # if window size is more than the array length, return -1.
    if k >= n:
        return -1

    result = []

    # define a blank queue
    queue = Queue()
    # push negative integers from first window into the queue.
    for i in range(k):
        if arr[i] < 0:
            queue.enqueue(arr[i])

    # now iterate on all the windows
    for i in range(n - k + 1):
        # append the front element from the queue in O(1) time.
        result.append(0 if queue.front() is None else queue.front())

        # for the next iteration, if the starting element of current window is negative,
        # then basically in the next window, a negative integer is being removed, so it
        # is not needed in the queue; pop it from the queue. This will take O(1) time.
        if arr[i] < 0:
            queue.dequeue()

        # if the first element from the next window is negative, then a negative element
        # is being pushed in to the window in next iteration; and so, push this element
        # into the queue as well. This will take O(1) time.
        if i + k < n and arr[i + k] < 0:
            queue.enqueue(arr[i + k])

    # finally return the result.
    return result


def bruteforce(arr, k):
    # Time complexity is O({n - k + 1}*k) and space complexity is O(n - k + 1) for storing result.
    result = []
    n = len(arr)

    # iterate on each window
    for i in range(n - k + 1):
        # assume that no negative value is found
        negative_found = False
        # iterate on each element in the window
        for j in range(i, i + k):
            if arr[j] < 0:
                # if the element is negative, add it to result, set negative_found to True and
                # break out of this nested loop.
                result.append(arr[j])
                negative_found = True
                break

        # if no negative value was found in this window, add a 0.
        if not negative_found:
            result.append(0)

    # return result list
    return result


print(bruteforce([-8, 2, 3, -6, 10], 2))
print(bruteforce([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(first_negative([-8, 2, 3, -6, 10], 2))
print(first_negative([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(first_negative([4, 0, 3, -12, 1], 3))
print(first_negative([45, 12, -6], 1))
print(first_negative([4, -7, 4, 6, 7, -11, 2, 4], 2))
print(first_negative([1, 2, 3], 10))
