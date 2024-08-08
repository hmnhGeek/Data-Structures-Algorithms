# Problem link - https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1

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


def shortest_path_with_k_stops(graph, source, destination, max_allowed_stops):
    # Time complexity is O(V + E) = O(n^2) and space is O(V) = O(n).

    # Initialize an empty queue and push the start node with following structure:
    # (number_of_stops_used_till_now, source_node, cost_incurred_to_reach_source_node).
    queue = Queue()
    queue.enqueue((0, source, 0))

    # initialize costs from source node to all the other nodes
    costs = {i: float('inf') for i in graph}
    # cost to reach node 0 from node 0 is 0.
    costs[source] = 0

    while not queue.is_empty():
        # pop the current node
        stops_used, node, cost_incurred = queue.dequeue()

        # Had this node been the destination node, we would not push anything to queue,
        # because there is no point travelling from destination to another node. If the
        # queue is still non-empty, the while loop will run again. However, if the node
        # is not the destination node, let's check if we can travel to its adjacent nodes.
        if node != destination:
            for adj in graph[node]:
                # store the adjacent node and the cost to travel between current node and adj_node.
                adj_node, individual_cost = adj

                # if the cost stored previously for this adjacent node from the source node is higher
                # than the path from current node to this adjacent node, then let's check further.
                if costs[adj_node] > individual_cost + cost_incurred:
                    # if this adjacent node is destination node, simply push it to queue without
                    # increasing the number of stops, as source and destination nodes are not
                    # considered as stops. Also, update the cost for adj_node (or destination).
                    if adj_node == destination:
                        costs[adj_node] = individual_cost + cost_incurred
                        queue.enqueue((stops_used, adj_node, costs[adj_node]))
                    else:
                        # if the adj_node is not the destination node, we need to additionally
                        # check if we have not crossed the limit of number of stops allowed during
                        # the journey. If we are within limits, we can push the adj_node into the
                        # queue and update the cost for adj_node.
                        if stops_used + 1 <= max_allowed_stops:
                            costs[adj_node] = individual_cost + cost_incurred
                            queue.enqueue((stops_used + 1, adj_node, costs[adj_node]))

    # finally, we return the minimum cost that can be spent to reach from source to destination
    # by stopping at most max_allowed_stops.
    return costs[destination]


def convert_to_graph(flights):
    # If there are n cities, and in the worst case all of them are connected with each other,
    # then the overall time complexity is O(n*(n - 1)) = O(n^2) because for each city, we will
    # need to create an edge with n - 1 cities. Space consumed will be O(n*(n - 1)) = O(n^2),
    # because for each city, we will have to create a list storing (n - 1) cities information.

    # Create a directed weighted graph from flights array.
    graph = {}

    # fill up the graph with source nodes.
    for flight in flights:
        source, dest, cost = flight
        if source not in graph:
            graph[source] = [[dest, cost]]
        else:
            graph[source].append([dest, cost])

    # there could be some nodes which are never a source, hence fill them up
    # in the graph with blank destinations.
    for flight in flights:
        source, dest, cost = flight
        if dest not in graph:
            graph[dest] = []

    return graph


def get_shortest_path_with_k_stops(flights, source, destination, max_allowed_stops):
    # Time complexity is O(n^2) and space O(n^2) to store graphical representation.

    # First convert the flights into a graphical representation. Each flight is of type: [source, dest, cost].
    graphical_flights_representation = convert_to_graph(flights)

    # use BFS to find the minimum distance by first checking on number of stops and then on the cost incurred.
    # Dijkstra could be used via a PQ but since stops will increase by a constant amount of 1 stop per unit,
    # we can use standard BFS with a queue. PQ would have costed extra log() but Queue will cost constant time.
    return shortest_path_with_k_stops(graphical_flights_representation, source, destination, max_allowed_stops)


print(
    get_shortest_path_with_k_stops(
        [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
        0,
        3,
        1
    )
)

print(
    get_shortest_path_with_k_stops(
        [[0,1,100],[1,2,100],[0,2,500]],
        0,
        2,
        1
    )
)

print(
    get_shortest_path_with_k_stops(
        [[0,1,100],[1,2,100],[0,2,500]],
        0,
        2,
        0
    )
)

print(
    get_shortest_path_with_k_stops(
        [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]],
        0,
        2,
        1
    )
)

print(
    get_shortest_path_with_k_stops(
        [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]],
        0,
        2,
        2
    )
)