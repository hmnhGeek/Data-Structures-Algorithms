# Problem link - https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
# Solution - https://www.youtube.com/watch?v=YbY8cVwWAvw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42&t=1s


class Graph:
    @staticmethod
    def floyd_warshall(graph):
        n = len(graph)
        distances = [[graph[i][j] for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if distances[i][j] == -1:
                    distances[i][j] = 1e6

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        for i in range(n):
            if distances[i][i] < 0:
                return "Negative Cycle Detected!!"

        return distances


print(Graph.floyd_warshall([[0, 25], [-1, 0]]))
print(Graph.floyd_warshall([[0, 1, 43],[1, 0, 6], [-1, -1, 0]]))