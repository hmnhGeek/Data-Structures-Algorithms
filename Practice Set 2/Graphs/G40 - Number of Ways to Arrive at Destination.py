# Problem link - https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1
# Solution - https://www.youtube.com/watch?v=_-0mx0SmYxA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=41


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


class PathsFinder:
    @staticmethod
    def get_num_paths(start_node, parents):
        """
            Time complexity is exponential and space complexity is O(n).
        """

        # if start node is not in parents, return a 0.
        if start_node not in parents:
            return 0

        # if we reached the ultimate parent, return 1 as a count of path.
        if parents[start_node] == [None]:
            return 1

        # count the number of paths for each parent.
        paths = 0
        for i in parents[start_node]:
            paths += PathsFinder.get_num_paths(i, parents)
        return paths

    @staticmethod
    def get_num_paths_memoized(start_node, parents, dp):
        """
            Time complexity is O(n) and space complexity is O(2n).
        """
        if start_node not in parents:
            return 0
        if parents[start_node] == [None]:
            return 1
        if dp[start_node] is not None:
            return dp[start_node]
        paths = 0
        for i in parents[start_node]:
            paths += PathsFinder.get_num_paths(i, parents)
        dp[start_node] = paths
        return dp[start_node]


class Solution:
    @staticmethod
    def _get_graph(edges):
        graph = {}
        for edge in edges:
            src, dst, wt = edge
            if src not in graph:
                graph[src] = [[dst, wt]]
            else:
                graph[src].append([dst, wt])
            if dst not in graph:
                graph[dst] = [[src, wt]]
            else:
                graph[dst].append([src, wt])
        return graph

    @staticmethod
    def _get_all_paths(parents):
        pass

    @staticmethod
    def num_ways(edges, source, destination):
        # get the graph from the edges using O(E) time and O(V + E) space.
        graph = Solution._get_graph(edges)

        # define a queue
        queue = Queue()

        # define distances and parents for this node.
        distances = {i: 1e6 for i in graph}
        parents = {i: [] for i in graph}

        # mark the distance of source as 0.
        distances[source] = 0

        # mark the parent of source as None.
        parents[source] = [None]

        # push the source node into the queue.
        queue.push((source, distances[source]))

        # typical Dijkstra
        while not queue.is_empty():
            # pop the current node.
            node, distance = queue.pop()

            # loop on the adjacent nodes
            for adj in graph[node]:
                adj_node, wt = adj

                # if we were able to find better distance for the adjacent node...
                if distances[adj_node] > distance + wt:
                    # then update the distance
                    distances[adj_node] = distance + wt
                    # also reset the parent with current node.
                    parents[adj_node] = [node, ]
                    # push the adjacent node
                    queue.push((adj_node, distances[adj_node]))

                # if we found another same length path, simple add it in the parents.
                if distances[adj_node] == distance + wt:
                    if node not in parents[adj_node]:
                        parents[adj_node].append(node)

        # return the count of shortest paths using Dynamic Programming (Memoization).
        return PathsFinder.get_num_paths_memoized(destination, parents, {i: None for i in graph})


print(
    Solution.num_ways(
        [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]],
        0, 6
    )
)

print(
    Solution.num_ways(
        [[0, 5, 8], [0, 2, 2], [0, 1, 1], [1, 3, 3], [1, 2, 3], [2, 5, 6], [3, 4, 2], [4, 5, 2]],
        0,
        5
    )
)

print(
    Solution.num_ways(
        [[1, 0, 10]],
        0, 1
    )
)
