# Problem link - https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=%2Fnumber-of-ways-to-arrive-at-destination
# Solution - https://www.youtube.com/watch?v=_-0mx0SmYxA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=40


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


class Graph:
    @staticmethod
    def _traceback(parents, begin_node, path, paths):
        # if the begin_node is the self parent...
        if len(parents[begin_node]) == 1 and parents[begin_node][0] == begin_node:
            # create a new copy of the path list and append the self parent node.
            final_path = [i for i in path] + [begin_node, ]
            # add the final path into the list of paths (in reversed form).
            paths.append(final_path[-1:-len(final_path) - 1:-1])
            # end the recursion
            return

        # if the node is not self parent, continue with its parents recursively.
        for parent in parents[begin_node]:
            # add the current node to the path
            path.append(begin_node)
            # recurse on its parent
            Graph._traceback(parents, parent, path, paths)
            # while backtracking, remove the node from the path.
            path.remove(begin_node)

    @staticmethod
    def traceback_path(parents, begin_node):
        # if the node from which you're tracing back does not exist, then return
        if begin_node not in parents:
            return []

        # create a list to store all the paths.
        paths = []

        # begin from the starting node.
        for parent in parents[begin_node]:
            # for each parent, create a new path and add the last node
            path = [begin_node, ]
            # traceback from the parent of this node.
            Graph._traceback(parents, parent, path, paths)
        return paths

    @staticmethod
    def num_shortest_paths(graph, source, destination):
        if source not in graph or destination not in graph:
            return

        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        parents = {i: [] for i in graph}
        parents[source].append(source)
        queue = Queue()
        queue.push((distances[source], source))

        while not queue.is_empty():
            distance, node = queue.pop()
            if node == destination:
                continue
            for adj in graph[node]:
                adj_node, edge_wt = adj

                # we will check for equality as well because we want to push the path if it is again the shortest path
                if distances[adj_node] >= distance + edge_wt:
                    distances[adj_node] = distance + edge_wt
                    if node not in parents[adj_node]:
                        parents[adj_node].append(node)
                    queue.push((distances[adj_node], adj_node))

        # once the parents have been populated, start tracing back the path from the destination to the source node.
        all_shortest_paths = Graph.traceback_path(parents, destination)
        return all_shortest_paths


print(
    Graph.num_shortest_paths(
        {
            0: [[1, 2], [4, 5], [6, 7]],
            1: [[0, 2], [2, 3], [3, 3]],
            2: [[1, 3], [5, 1]],
            3: [[1, 3], [6, 3], [5, 1]],
            4: [[0, 5], [6, 2]],
            5: [[2, 1], [3, 1], [6, 1]],
            6: [[0, 7], [3, 3], [4, 2], [5, 1]]
        },
        0,
        6
    )
)

print(
    Graph.num_shortest_paths(
        {
            0: [[1, 1], [2, 2], [5, 8]],
            1: [[0, 1], [2, 3], [3, 3]],
            2: [[1, 3], [0, 2], [5, 6]],
            3: [[1, 3], [4, 2]],
            4: [[3, 2], [5, 2]],
            5: [[2, 6], [4, 2], [0, 8]]
        },
        0,
        5
    )
)
