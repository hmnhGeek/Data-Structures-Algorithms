package Graphs.G36;

import java.util.ArrayList;
import java.util.List;


class Element {
    public Integer d, x, y;

    public Element(Integer d, Integer x, Integer y) {
        this.d = d;
        this.x = x;
        this.y = y;
    }
}


public class Solution {
    public static Integer getMinDistance(List<List<Integer>> graph, int sourceX, int sourceY, int dstX, int dstY) {
        int n = graph.size(), m = graph.getFirst().size();
        if (cellNotInGraph(sourceX, sourceY, n, m) || cellNotInGraph(dstX, dstY, n, m)) return null;
        List<List<Integer>> distances = getDistancesMatrix(n, m, sourceX, sourceY);
        Queue<Element> queue = new Queue<>();
        queue.push(new Element(0, sourceX, sourceY));
        while (!queue.isEmpty()) {
            Element element = queue.pop();
            Integer wt = element.d, x = element.x, y = element.y;
            List<List<Integer>> neighbours = getValidNeighbours(x, y, n, m, graph);
            for (List<Integer> neighbour : neighbours) {
                int i = neighbour.getFirst(), j = neighbour.getLast();
                if (distances.get(i).get(j) > wt + 1) {
                    distances.get(i).set(j, wt + 1);
                    queue.push(new Element(wt + 1, i, j));
                }
            }
        }
        return distances.get(dstX).get(dstY) != Integer.MAX_VALUE ? distances.get(dstX).get(dstY) : -1;
    }

    private static List<List<Integer>> getValidNeighbours(Integer x, Integer y, int n, int m, List<List<Integer>> graph) {
        List<List<Integer>> neighbours = new ArrayList<>();
        if (0 <= x - 1 && x - 1 < n && graph.get(x - 1).get(y) == 1) {
            neighbours.add(List.of(x - 1, y));
        }
        if (0 <= y + 1 && y + 1 < m && graph.get(x).get(y + 1) == 1) {
            neighbours.add(List.of(x, y + 1));
        }
        if (0 <= x + 1 && x + 1 < n && graph.get(x + 1).get(y) == 1) {
            neighbours.add(List.of(x + 1, y));
        }
        if (0 <= y - 1 && y - 1 < m && graph.get(x).get(y - 1) == 1) {
            neighbours.add(List.of(x, y - 1));
        }
        return neighbours;
    }

    private static List<List<Integer>> getDistancesMatrix(int n, int m, int sourceX, int sourceY) {
        List<List<Integer>> distances = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(Integer.MAX_VALUE);
            }
            distances.add(row);
        }
        distances.get(sourceX).set(sourceY, 0);
        return distances;
    }

    private static boolean cellNotInGraph(int x, int y, int n, int m) {
        return x < 0 || x >= n || y < 0 || y >= m;
    }

    public static void main(String[] args) {

        System.out.println(
                Solution.getMinDistance(
                        List.of(
                                List.of(1, 1, 1, 1),
                                List.of(1, 1, 0, 1),
                                List.of(1, 1, 1, 1),
                                List.of(1, 1, 0, 0),
                                List.of(1, 0, 0, 0)
                        ),
                        0, 1,
                        2, 2
                )
        );

        System.out.println(
                Solution.getMinDistance(
                        List.of(
                                List.of(1, 1, 1, 1, 1),
                                List.of(1, 1, 1, 1, 1),
                                List.of(1, 1, 1, 1, 0),
                                List.of(1, 0, 1, 0, 1)
                        ),
                        0, 0,
                        3, 4
                )
        );

        System.out.println(
                Solution.getMinDistance(
                        List.of(
                                List.of(1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
                                List.of(1, 0, 1, 0, 1, 1, 1, 0, 1, 1),
                                List.of(1, 1, 1, 0, 1, 1, 0, 1, 0, 1),
                                List.of(0, 0, 0, 0, 1, 0, 0, 0, 0, 1),
                                List.of(1, 1, 1, 0, 1, 1, 1, 0, 1, 0),
                                List.of(1, 0, 1, 1, 1, 1, 0, 1, 0, 0),
                                List.of(1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                                List.of(1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
                                List.of(1, 1, 0, 0, 0, 0, 1, 0, 0, 1)
                        ),
                        0, 0,
                        3, 4
                )
        );

        System.out.println(
                Solution.getMinDistance(
                        List.of(
                                List.of(1, 1, 1, 1),
                                List.of(0, 1, 1, 0),
                                List.of(0, 0, 1, 1)
                        ),
                        0, 0,
                        2, 3
                )
        );

        System.out.println(
                Solution.getMinDistance(
                        List.of(
                                List.of(1, 1),
                                List.of(0, 1)
                        ),
                        0, 0,
                        1, 1
                )
        );

        System.out.println(
                Solution.getMinDistance(
                        List.of(
                                List.of(1, 0),
                                List.of(0, 1)
                        ),
                        0, 0,
                        1, 1
                )
        );
    }
}
