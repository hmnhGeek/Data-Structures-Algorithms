# Problem - https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1
# Solution - https://www.youtube.com/watch?v=PwMVNSJ5SLI

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
    # refer to the code of Dijkstra's algorithm for better understanding of this class.
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
    '''

    :param cities_map: List[List[int]] of the form [[source, destination, distance], ...]
    :param threshold_distance: int representing the threshold distance.
    :return: int representing the city which satisfies the condition.

    This function takes O(VE * log(V)) time and O(V^2) space.

    We will use Dijkstra's algorithm and not Floyd-Warshall because the graphs used will have
    positive weights and therefore, we can reduce the time and space complexity a lot.
    '''

    # The first task is to create an adjacency list from the given edge list (i.e., cities_map).
    adj_list = {}
    for route in cities_map:
        # create an edge in the list from source city to destination city.
        source_city, destination_city, distance = route
        if source_city in adj_list:
            adj_list[source_city].append([destination_city, distance])
        else:
            adj_list[source_city] = [[destination_city, distance]]

        # create an edge in the list from destination city to source city because it is an
        # undirected graph.
        if destination_city in adj_list:
            adj_list[destination_city].append([source_city, distance])
        else:
            adj_list[destination_city] = [[source_city, distance]]

    # finally, one last time check if there are any nodes which are not connected to any other
    # nodes in the cities_map.
    for route in cities_map:
        source_city, destination_city, _ = route
        if source_city not in adj_list:
            adj_list[source_city] = []
        if destination_city not in adj_list:
            adj_list[destination_city] = []

    # Once we have the adjacency list, we can use Dijkstra's algorithm to compute the shortest
    # distances from every node to every other node. This will take O(V*E*log(V)) time and O(V^2) space.
    # Floyd Warshall would have taken O(V^3) time.
    shortest_paths_between_all_cities = Dijkstra(adj_list).get_shortest_distances()

    # initialize the number of neighbours which lie within threshold of a source city as infinite.
    min_num_cities_within_threshold = float('inf')
    # initialize a resultant source city which the problem is asking us to find.
    resultant_source_city = None

    # loop among all the cities from the shortest paths given by Dijkstra
    for city in shortest_paths_between_all_cities:
        # for this city, find the number of neighbours which lie within threshold distance
        num_neighbours_within_threshold = len([i for i in shortest_paths_between_all_cities[city].values() if i <= threshold_distance])

        # if the number of such neighbours is less than or equal to min neighbours till now, update it
        # and set the resultant city to this city as this city could be our answer. We are using "=" also
        # in the condition just to take the largest number city, otherwise, "<" would have been fine too.
        if num_neighbours_within_threshold <= min_num_cities_within_threshold:
            min_num_cities_within_threshold = num_neighbours_within_threshold
            resultant_source_city = city

    # return the resultant city.
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

print(
    get_city_with_smallest_neighbours(
        [
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 3],
            [3, 4, 1],
            [0, 3, 3]
        ],
        3
    )
)

print(
    get_city_with_smallest_neighbours(
        [
            [0, 1, 2],
            [1, 2, 2],
            [2, 0, 1]
        ],
        4
    )
)