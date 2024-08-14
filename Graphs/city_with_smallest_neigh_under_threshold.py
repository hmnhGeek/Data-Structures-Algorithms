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


class Dijkstra:
    def __init__(self, adj_list):
        self.graph = adj_list

    def _get_shortest_path(self, source):
        queue = Queue()
        queue.enqueue((source, 0))

        distances = {i: float('inf') for i in self.graph}
        distances[source] = 0

        while not queue.is_empty():
            node, distance = queue.dequeue()

            for adj in self.graph[node]:
                adj_node, edge_wt = adj
                if distances[adj_node] > distance + edge_wt:
                    distances[adj_node] = distance + edge_wt
                    queue.enqueue((adj_node, distances[adj_node]))

        return distances

    def get_shortest_distances(self):
        distances = {}
        for node in self.graph:
            distances[node] = self._get_shortest_path(node)
        return distances


def get_city_with_smallest_neighbours(cities_map, threshold_distance):
    adj_list = {}
    for route in cities_map:
        source_city, destination_city, distance = route
        if source_city in adj_list:
            adj_list[source_city].append([destination_city, distance])
        else:
            adj_list[source_city] = [[destination_city, distance]]

        if destination_city in adj_list:
            adj_list[destination_city].append([source_city, distance])
        else:
            adj_list[destination_city] = [[source_city, distance]]

    shortest_paths_between_all_cities = Dijkstra(adj_list).get_shortest_distances()
    min_num_cities_within_threshold = float('inf')
    resultant_source_city = None

    for city in shortest_paths_between_all_cities:
        num_neighbours_within_threshold = len([i for i in shortest_paths_between_all_cities[city].values() if i <= threshold_distance])
        if num_neighbours_within_threshold <= min_num_cities_within_threshold:
            min_num_cities_within_threshold = num_neighbours_within_threshold
            resultant_source_city = city

    return resultant_source_city


print(
    get_city_with_smallest_neighbours(
        [
            [0, 1, 3],
            [1, 2, 1],
            [1, 3, 4],
            [2, 3, 1]
        ],
        4
    )
)

print(
    get_city_with_smallest_neighbours(
        [
            [0, 1, 2],
            [0, 4, 8],
            [1, 2, 3],
            [1, 4, 2],
            [2, 3, 1],
            [3, 4, 1]
        ],
        2
    )
)