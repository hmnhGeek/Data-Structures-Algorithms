def is_on_edge(x, y, R, C):
    return x in [0, C - 1] or y in [0, R - 1]


def dfs(mtx, start_node, visited, R, C):
    x, y = start_node

    # visit the node first
    visited[x][y] = 1

    # extract all possible adjacent indices
    adj_nodes = []
    if x - 1 in range(R): adj_nodes.append((x - 1, y))
    if y + 1 in range(C): adj_nodes.append((x, y + 1))
    if x + 1 in range(R): adj_nodes.append((x + 1, y))
    if y - 1 in range(C): adj_nodes.append((x, y - 1))

    for node in adj_nodes:
        # check if the adjacent node has not been visited, and it is a valid node or not.
        # if yes, then recursively call dfs() on this node
        if visited[node[0]][node[1]] == 0 and mtx[node[0]][node[1]] == 1:
            dfs(mtx, node, visited, R, C)


def remove_islands(mtx):
    # initialize important variables like R, C and visited
    R, C = len(mtx), len(mtx[0])
    visited = [[0] * C for _ in range(R)]

    # the idea is to start the DFS traversal from edge nodes.
    # start traversals from top edge, then from down, left and finally
    # the right edge. In this way, you will fill up the visited array
    # in such a manner that all the nodes connected with the edge of the matrix
    # are visited.
    # The leftover nodes (which are 1 in the matrix but not visited) will be the
    # isolated islands. We can now either return the visited array (representing
    # the removed islands) or simply modify the starting matrix itself by replacing
    # it with the visited matrix.

    # cover top edge
    for node in range(C):
        if visited[0][node] == 0 and mtx[0][node] == 1:
            dfs(mtx, (0, node), visited, R, C)

    # cover down edge
    for node in range(C):
        if visited[R - 1][node] == 0 and mtx[R - 1][node] == 1:
            dfs(mtx, (R - 1, node), visited, R, C)

    # cover left edge
    for node in range(R):
        if visited[node][0] == 0 and mtx[node][0] == 1:
            dfs(mtx, (node, 0), visited, R, C)

    # cover right edge
    for node in range(R):
        if visited[node][C - 1] == 0 and mtx[node][C - 1] == 1:
            dfs(mtx, (node, C - 1), visited, R, C)

    return visited


mtx = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

mtx = remove_islands(mtx)
print()
for i in mtx:
    print(i)

mtx2 = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

mtx2 = remove_islands(mtx2)
print()
for i in mtx2:
    print(i)

mtx3 = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]
print()
for i in mtx3:
    print(i)
