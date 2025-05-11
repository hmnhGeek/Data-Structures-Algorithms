package Graphs.G8;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class QueueElement {
    private Integer row;
    private Integer col;

    public QueueElement(Integer r, Integer c) {
        this.col = c;
        this.row = r;
    }

    public Integer getRow() {
        return row;
    }

    public Integer getCol() {
        return col;
    }
}

public class Solution {
    public static Integer getNumberOfIslands(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        Integer numComponents = 0;
        List<List<Boolean>> visited = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Boolean> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(false);
            }
            visited.add(row);
        }
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (matrix.get(i).get(j) == 1 && !visited.get(i).get(j)) {
                    numComponents += 1;
                    Queue<QueueElement> queue = new Queue<>();
                    visited.get(i).set(j, true);
                    queue.push(new QueueElement(i, j));
                    while (!queue.isEmpty()) {
                        QueueElement queueElement = queue.pop();
                        int x = queueElement.getRow(), y = queueElement.getCol();
                        List<List<Integer>> neighbours = getNeighbours(matrix, x, y, n, m, visited);
                        for (List<Integer> neighbour : neighbours) {
                            int x0 = neighbour.getFirst(), y0 = neighbour.getLast();
                            visited.get(x0).set(y0, true);
                            queue.push(new QueueElement(x0, y0));
                        }
                    }
                }
            }
        }
        return numComponents;
    }

    private static List<List<Integer>> getNeighbours(List<List<Integer>> matrix, int x, int y, int n, int m, List<List<Boolean>> visited) {
        List<List<Integer>> result = new ArrayList<>();
        if (0 <= x - 1 && x - 1 < n && !visited.get(x - 1).get(y) && matrix.get(x - 1).get(y) == 1) {
            result.add(List.of(x - 1, y));
        }
        if (0 <= y + 1 && y + 1 < m && !visited.get(x).get(y + 1) && matrix.get(x).get(y + 1) == 1) {
            result.add(List.of(x, y + 1));
        }
        if (0 <= x + 1 && x + 1 < n && !visited.get(x + 1).get(y) && matrix.get(x + 1).get(y) == 1) {
            result.add(List.of(x + 1, y));
        }
        if (0 <= y - 1 && y - 1 < m && !visited.get(x).get(y - 1) && matrix.get(x).get(y - 1) == 1) {
            result.add(List.of(x, y - 1));
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(0, 1, 1, 0),
                                List.of(0, 1, 1, 0),
                                List.of(0, 0, 1, 0),
                                List.of(0, 0, 0, 0),
                                List.of(1, 1, 0, 1)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(0, 1),
                                List.of(1, 0),
                                List.of(1, 1),
                                List.of(1, 0)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(0, 1, 1, 1, 0, 0, 0),
                                List.of(0, 0, 1, 1, 0, 1, 0)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(1, 1, 0, 0, 0),
                                List.of(1, 1, 0, 0, 0),
                                List.of(0, 0, 1, 0, 0),
                                List.of(0, 0, 0, 1, 1)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(1, 1, 0, 0, 0),
                                List.of(0, 1, 0, 0, 1),
                                List.of(1, 0, 0, 1, 1),
                                List.of(0, 0, 0, 0, 0),
                                List.of(1, 0, 1, 1, 0)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(0, 0),
                                List.of(0, 0)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfIslands(
                        List.of(
                                List.of(1, 1),
                                List.of(1, 1)
                        )
                )
        );
    }
}
