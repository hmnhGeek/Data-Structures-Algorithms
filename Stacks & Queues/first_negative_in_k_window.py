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
    n = len(arr)
    result = []
    queue = Queue()
    for i in range(k):
        if arr[i] < 0:
            queue.enqueue(arr[i])

    for i in range(n - k + 1):
        result.append(0 if queue.front() is None else queue.front())
        if arr[i] < 0:
            queue.dequeue()
        if i + k < n and arr[i + k] < 0:
            queue.enqueue(arr[i + k])
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
