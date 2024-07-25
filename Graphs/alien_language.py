class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.head is None:
            return
        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def is_empty(self):
        return self.length == 0

    def front(self):
        return None if self.head is None else self.head.data


def get_indegrees(g):
    # this will take O(k) time as there are k nodes (characters) and O(k) space.
    indegrees = {i: 0 for i in g}

    for node in g:
        for adj_node in g[node]:
            indegrees[adj_node] += 1

    return indegrees

def _topo_sort(g, node, visited, indegrees, queue):
    order = []
    visited[node] = True

    while not queue.is_empty():
        node = queue.dequeue()
        order.append(node)

        for adj_node in g[node]:
            indegrees[adj_node] -= 1
            if indegrees[adj_node] == 0:
                queue.enqueue(adj_node)

    return order


def topological_sort(g):
    q = Queue()

    # O(k) time and space each
    indegrees = get_indegrees(g)
    visited = {i: False for i in g}
    sort_order = []

    for node in [k for k, v in indegrees.items() if v == 0]:
        q.enqueue(node)

    # populating the sort_order takes O(V + E) time and O(E) space.
    # Computing `E` will depend on the strings, however, V = k.
    # Hence, time would be O(k + E) and space = O(E).
    for node in g:
        if not visited[node]:
            sort_order.extend(_topo_sort(g, node, visited, indegrees, q))

    return sort_order

def get_edge_for_graph(graph, string1, string2):
    '''This will take O(n) time to populate the nodes.'''
    n1, n2 = len(string1), len(string2)
    maxi = min(n1, n2)

    for i in range(maxi):
        if string1[i] != string2[i]:
            if string1[i] in graph:
                graph[string1[i]].append(string2[i])
            else:
                graph[string1[i]] = [string2[i]]
            break


''' MAIN FUNCTION
    Assume that we have a m length dictionary of words and in
    the worst case we have all the words of length n. Also,
    assume that distinct character count is k.
    
    Overall time complexity is O(m*n + k + E) and space complexity is O(E).
'''
def get_language_order(dictionary_list):
    dict_length = len(dictionary_list)

    # create a blank graph, this operation will cost
    # O(m*n) time with a space O(E). E = # edges.
    graph = {}
    # for each word in the dictionary
    for word in dictionary_list:
        # for each character in the word
        for char in word:
            # if the character is not present in the graph,
            # add it to the graph as a node.
            if char not in graph:
                graph[char] = []

    # this loop will run m times. Time complexity would become O(m*n)
    for i in range(dict_length - 1):
        # this will take O(n) time to populate the node neighbours
        get_edge_for_graph(graph, dictionary_list[i], dictionary_list[i + 1])

    # Time = O(k + E) and space = O(E)
    order = topological_sort(graph)
    if len(order) == len(graph):
        return order

    return []


print(get_language_order(["baa","abcd","abca","cab","cad"]))
print(get_language_order(["caa","aaa","aab"]))
print(get_language_order(["abc","bat","ade"]))
