# Explanation - https://www.youtube.com/watch?v=mJcZjjKzeqk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=45

class PriorityQueueNode:
    def __init__(self, edge_weight, node, parent):
        self.weight = edge_weight
        self.node = node
        self.parent = parent


class MinimumSpanningTreeEdge:
    def __init__(self, parent, node):
        self.parent = parent
        self.node = node


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci

        min_child_index = lci
        if self.heap[rci].weight < self.heap[min_child_index].weight:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi].weight > self.heap[min_child_index].weight:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)

        if min_child_index is not None:
            if self.heap[pi].weight > self.heap[min_child_index].weight:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x: PriorityQueueNode):
        self.heap.append(x)
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return

        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.min_heapify_down(0)
        return item


class PrimsMinimumSpanningTree:
    def __init__(self, adj_list):
        self.graph = adj_list

    def _get_min_spanning_tree(self, source_node=0):
        visited = {i: False for i in self.graph}
        pq = MinHeap()
        pq.insert(PriorityQueueNode(0, source_node, None))

        minimum_spanning_tree = []
        minimum_spanning_tree_sum = 0

        while not pq.is_empty():
            pq_node = pq.pop()

            if not visited[pq_node.node]:
                visited[pq_node.node] = True
                minimum_spanning_tree_sum += pq_node.weight
                if pq_node.parent is not None:
                    minimum_spanning_tree.append(MinimumSpanningTreeEdge(pq_node.parent, pq_node.node))

                for adj in self.graph[pq_node.node]:
                    adj_node, edge_wt = adj
                    pq.insert(PriorityQueueNode(edge_wt, adj_node, pq_node.node))

        return minimum_spanning_tree, minimum_spanning_tree_sum

    def get_min_spanning_tree(self):
        min_spanning_tree, min_spanning_tree_sum = self._get_min_spanning_tree()
        printable_edges = []
        for mst_edge in min_spanning_tree:
            printable_edges.append((mst_edge.parent, mst_edge.node))
        return printable_edges, min_spanning_tree_sum


graph1 = PrimsMinimumSpanningTree(
    {
        0: [[1, 2], [2, 1]],
        1: [[0, 2], [2, 1]],
        2: [[0, 1], [1, 1], [4, 2], [3, 2]],
        3: [[2, 2], [4, 1]],
        4: [[2, 2], [3, 1]]
    }
)

print(graph1.get_min_spanning_tree())