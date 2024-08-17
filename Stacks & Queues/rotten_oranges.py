# Problem link - https://www.geeksforgeeks.org/problems/rotten-oranges2536/1


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

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return

        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class RottenOranges:
    def __init__(self, oranges):
        self.oranges = oranges
        self.r = len(oranges)
        self.c = len(oranges[0])
        self.initial_rotten_oranges = self._find_initial_rotten_oranges()

    def _find_initial_rotten_oranges(self):
        initial_rotten_oranges = []
        for row in range(self.r):
            for col in range(self.c):
                if self.oranges[row][col] == 2:
                    initial_rotten_oranges.append((row, col, 0))
        return initial_rotten_oranges

    def _get_adjacent_nodes(self, x, y):
        adjacent_nodes = []
        if 0 <= x - 1 < self.r and self.oranges[x - 1][y] == 1:
            adjacent_nodes.append((x - 1, y))
        if 0 <= y + 1 < self.c and self.oranges[x][y + 1] == 1:
            adjacent_nodes.append((x, y + 1))
        if 0 <= x + 1 < self.r and self.oranges[x + 1][y] == 1:
            adjacent_nodes.append((x + 1, y))
        if 0 <= y - 1 < self.r and self.oranges[x][y - 1] == 1:
            adjacent_nodes.append((x, y - 1))
        return adjacent_nodes

    def _all_have_rotten(self, visited):
        for i in range(self.r):
            for j in range(self.c):
                # if there is an orange which is not yet visited, return False
                if (self.oranges[i][j] == 1 or self.oranges[i][j] == 2) and not visited[i][j]:
                    return False
        # all oranges have rotten, return True.
        return True

    def find_time_taken_to_rot(self):
        # Time complexity is O(m*n) and space is also O(m*n) for the visited matrix and the number of nodes that the
        # queue will store in the worst case.

        # we would need a visited array to mark the nodes visited in BFS traversal
        visited = [[False for _ in range(self.c)] for _ in range(self.r)]

        # initialize a queue and push all the initially rotten oranges into it, as these will act as the starting
        # nodes for the BFS traversal.
        queue = Queue()
        for rotten_orange in self.initial_rotten_oranges:
            queue.enqueue(rotten_orange)

        # assume that the time taken to rot all the oranges is -inf to handle max() function.
        min_time_to_rot_all = float('-inf')

        # typical BFS approach; traversing all m*n nodes.
        while not queue.is_empty():
            node_x, node_y, time = queue.dequeue()

            # mark the popped node as visited (no need to rot, that will modify the original matrix which is not a
            # good approach).
            visited[node_x][node_y] = True

            # update the min time taken to rot this orange
            min_time_to_rot_all = max(min_time_to_rot_all, time)

            # find all the adjacent oranges which are not yet rotten.
            adjacent_nodes = self._get_adjacent_nodes(node_x, node_y)

            # loop on the fresh adjacent oranges and push those oranges into the queue which are not yet visited.
            # while pushing ensure that you increase the time by one unit.
            for adjacent_node in adjacent_nodes:
                adj_x, adj_y = adjacent_node
                if not visited[adj_x][adj_y]:
                    queue.enqueue((adj_x, adj_y, time + 1))

        # return the time taken to rot all the oranges if all of them have rotten else return -1 meaning that there is
        # at least one orange which cannot get rotten.
        return min_time_to_rot_all if self._all_have_rotten(visited) else -1


print(RottenOranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]).find_time_taken_to_rot())
print(RottenOranges([[2, 2, 0, 1]]).find_time_taken_to_rot())
print(RottenOranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]).find_time_taken_to_rot())
print(RottenOranges([[0, 2]]).find_time_taken_to_rot())
print(RottenOranges([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]).find_time_taken_to_rot())