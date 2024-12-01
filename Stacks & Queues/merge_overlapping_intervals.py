class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class Solution:
    @staticmethod
    def _check_overlap(t1, t2):
        return t1[1] >= t2[0]

    @staticmethod
    def _merge(stack, interval):
        t1 = stack.pop()
        t = []
        t.append(min(t1[0], interval[0]))
        t.append(max(t1[1], interval[1]))
        stack.push(tuple(t))

    @staticmethod
    def merge_intervals(intervals):
        # sort intervals based on their start time.
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        stack = Stack()
        i = 0
        while i < n:
            stack.push(intervals[i])
            low, high = i + 1, n - 1
            while low <= high:
                mid = int(low + (high - low) / 2)
                has_overlap = Solution._check_overlap(stack.top(), intervals[mid])
                if has_overlap:
                    low = mid + 1
                else:
                    high = mid - 1
            # low will point to first non-overlapping interval and high to the last overlapping one.
            Solution._merge(stack, intervals[high])
            i = low

        merged_intervals = []
        while not stack.is_empty():
            merged_intervals.append(stack.pop())
        return merged_intervals[-1:-len(merged_intervals) - 1:-1]


print(
    Solution.merge_intervals(
        [
            (1, 3),
            (2, 6),
            (8, 9),
            (9, 11),
            (8, 10),
            (2, 4),
            (15, 18),
            (16, 17)
        ]
    )
)

print(
    Solution.merge_intervals([[1, 3], [2, 4], [6, 8], [9, 10]])
)

print(
    Solution.merge_intervals([[7, 8], [1, 5], [2, 4], [4, 6]])
)

print(
    Solution.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
)

print(
    Solution.merge_intervals([[1, 4], [4, 5]])
)


def merge_overlap(arr):
    # Sort intervals based on start values
    arr.sort()

    merged = Stack()
    merged.push(arr[0])

    for i in range(1, len(arr)):
        last = merged.top()
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            merged.push(curr)

    result = []
    while not merged.is_empty():
        result.append(merged.pop())
    return result[-1:-len(result)-1:-1]


print("\nOptimal Solution")
print(merge_overlap([
    [1, 3],
    [2, 6],
    [8, 9],
    [9, 11],
    [8, 10],
    [2, 4],
    [15, 18],
    [16, 17]
]))

print(
    merge_overlap([[1, 3], [2, 4], [6, 8], [9, 10]])
)

print(
    merge_overlap([[7, 8], [1, 5], [2, 4], [4, 6]])
)

print(
    merge_overlap([[1, 3], [2, 6], [8, 10], [15, 18]])
)

print(
    merge_overlap([[1, 4], [4, 5]])
)
