# Problem link - https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
# Solution - https://www.youtube.com/watch?v=edXdVwkYHF8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=13


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

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
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


class DistanceCalculator:
    @staticmethod
    def _get_nearest_1(mtx, i, j, n, m):
        # This method will return the nearest 1 distance of this cell (i, j).

        # push the (i, j) cell with distance 0 into the queue.
        queue = Queue()
        queue.push((i, j, 0))

        # standard BFS algorithm...
        while not queue.is_empty():
            # pop the node.
            x, y, d = queue.pop()

            if 0 <= x - 1 < n:
                if mtx[x - 1][y] == 0:
                    # if the (x - 1, y) cell is also 0, push it back into the queue with +1 distance.
                    queue.push((x - 1, y, d + 1))
                else:
                    # if the (x - 1, y) cell is 1, we have found the nearest one, return current distance + 1 as answer.
                    return d + 1
            if 0 <= y + 1 < m:
                if mtx[x][y + 1] == 0:
                    # if the (x, y + 1) cell is also 0, push it back into the queue with +1 distance.
                    queue.push((x, y + 1, d + 1))
                else:
                    # if the (x, y + 1) cell is 1, we have found the nearest one, return current distance + 1 as answer.
                    return d + 1
            if 0 <= x + 1 < n:
                if mtx[x + 1][y] == 0:
                    # if the (x + 1, y) cell is also 0, push it back into the queue with +1 distance.
                    queue.push((x + 1, y, d + 1))
                else:
                    # if the (x + 1, y) cell is 1, we have found the nearest one, return current distance + 1 as answer.
                    return d + 1
            if 0 <= y - 1 < m:
                if mtx[x][y - 1] == 0:
                    # if the (x, y - 1) cell is also 0, push it back into the queue with +1 distance.
                    queue.push((x, y - 1, d + 1))
                else:
                    # if the (x, y - 1) cell is 1, we have found the nearest one, return current distance + 1 as answer.
                    return d + 1

    @staticmethod
    def calc(mtx):
        """
            Time complexity is O(nm) and space complexity is O(n + m + nm) in worst case when queue will hold
            n + m nodes when nearest 1 is diagonally extreme.
        """

        # create a result matrix with same dimension as the original matrix.
        n, m = len(mtx), len(mtx[0])
        result = [[None for _ in range(m)] for _ in range(n)]
        # loop on each element of the matrix.
        for i in range(n):
            for j in range(m):
                # if the (i, j) element is 1, set the nearest distance of this cell in result to be 0.
                # A 1-valued cell is nearest to itself.
                if mtx[i][j] == 1:
                    result[i][j] = 0
                else:
                    # if the cell value is 0 however, find the distance of nearest 1 using BFS algorithm.
                    nearest_1_distance = DistanceCalculator._get_nearest_1(mtx, i, j, n, m)
                    # set that distance for this cell in result matrix.
                    result[i][j] = nearest_1_distance
        # return the result matrix.
        return result


print(
    DistanceCalculator.calc(
        [
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 0]
        ]
    )
)

print(
    DistanceCalculator.calc(
        [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1]
        ]
    )
)

print(
    DistanceCalculator.calc(
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(DistanceCalculator.calc([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]))
print(DistanceCalculator.calc([[1, 0, 0], [0, 0, 1], [0, 1, 1]]))
print(DistanceCalculator.calc([[0, 0], [1, 0]]))