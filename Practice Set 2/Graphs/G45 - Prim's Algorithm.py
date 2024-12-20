# Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# Solution - https://www.youtube.com/watch?v=mJcZjjKzeqk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=45


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2 * pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2 * pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1) / 2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci][0] < self.heap[min_child_index][0]:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi][0] > self.heap[min_child_index][0]:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.min_heapify_down(0)
        return item


class Solution:
    @staticmethod
    def get_mst(graph, source):
        """
            Time complexity is O(E log(E)) and space complexity is O(V + E).
        """

        # if the source node is not present in the graph, return.
        if source not in graph:
            return

        # define a min heap and push the source node with parent as None and distance to reach source as 0.
        pq = MinHeap()
        pq.insert((0, source, None))

        # define a visited array
        visited = {i: False for i in graph}

        # define MST
        mst = set()
        mst_wt = 0

        # typical Prim's Algorithm, which will run for E times.
        while not pq.is_empty():
            # pop the current node in log(E) time.
            distance, node, parent = pq.pop()

            # if the current node is not visited and its parent is also not None, add it to MST.
            if not visited[node] and parent is not None:
                mst.add((node, parent))
                mst_wt += distance

            # now mark the current node as visited.
            visited[node] = True

            # loop on the adjacent nodes of this current node.
            for adj in graph[node]:
                adj_node, wt = adj
                # if the adjacent node is not visited, add it to the PQ. This will take log(E) time.
                if not visited[adj_node]:
                    pq.insert((wt, adj_node, node))

        # finally, return the MST.
        return mst, mst_wt


print(
    Solution.get_mst(
        {
            0: [[1, 2], [2, 1]],
            1: [[0, 2], [2, 1]],
            2: [[0, 1], [1, 1], [4, 2], [3, 2]],
            3: [[2, 2], [4, 1]],
            4: [[2, 2], [3, 1]]
        },
        0
    )
)

print(
    Solution.get_mst(
        {
            0: [[1, 5], [2, 1]],
            1: [[0, 5], [2, 3]],
            2: [[0, 1], [1, 3]]
        },
        0
    )
)

print(
    Solution.get_mst(
        {
            0: [[1, 1], [2, 3], [3, 4]],
            1: [[0, 1], [2, 2]],
            2: [[1, 2], [0, 3], [3, 5]],
            3: [[0, 4], [2, 5]]
        },
        0
    )
)
