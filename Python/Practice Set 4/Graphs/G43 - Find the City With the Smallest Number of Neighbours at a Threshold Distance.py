class Solution:
    @staticmethod
    def find_city(edges, threshold, n):
        mtx = Solution._get_graph_matrix(edges, n)

    @staticmethod
    def _get_graph_matrix(edges, n):
        mtx = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(0)
                else:
                    row.append(1e6)
            mtx.append(row)

        for edge in edges:
            src, dest, wt = edge
            mtx[src][dest] = wt
        return mtx
