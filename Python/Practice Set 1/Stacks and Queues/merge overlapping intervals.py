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
        self.head = self.head.next
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class QuickSort:
    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Solution:
    @staticmethod
    def merge_overlapping_intervals(arr):
        QuickSort.sort(arr)
        merged_intervals = []
        stack = Stack()
        stack.push(arr[0])
        n = len(arr)
        for i in range(1, n):
            current_interval = arr[i]
            last_interval = stack.top()
            if current_interval[0] <= last_interval[1]:
                new_last_interval = (
                    min(last_interval[0], current_interval[0]),
                    max(last_interval[1], current_interval[1])
                )
                stack.pop()
                stack.push(new_last_interval)
            else:
                stack.push(current_interval)
        while not stack.is_empty():
            merged_intervals.append(stack.pop())
        return merged_intervals[-1:-len(merged_intervals)-1:-1]


print(Solution.merge_overlapping_intervals([
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
    Solution.merge_overlapping_intervals([[1, 3], [2, 4], [6, 8], [9, 10]])
)

print(
    Solution.merge_overlapping_intervals([[7, 8], [1, 5], [2, 4], [4, 6]])
)

print(
    Solution.merge_overlapping_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
)

print(
    Solution.merge_overlapping_intervals([[1, 4], [4, 5]])
)
