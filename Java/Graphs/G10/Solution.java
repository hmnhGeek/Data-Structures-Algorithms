package Graphs.G10;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Coordinate {
    public int x;
    public int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Element {
    public Coordinate coordinate;
    public Integer t;

    public Element(Coordinate coordinate, Integer t) {
        this.coordinate = coordinate;
        this.t = t;
    }
}

public class Solution {
    public static int rot(List<List<Integer>> matrix) {
        int n = matrix.size(), m = matrix.getFirst().size();
        List<Coordinate> rottenOranges = getRottenOranges(matrix, n, m);
        Queue<Element> queue = new Queue<>();
        List<List<Boolean>> visited = new ArrayList<>();
        getBlankVisitedMatrix(visited, n, m);
        int timeTaken = 0;
        for (Coordinate coordinate : rottenOranges) {
            visited.get(coordinate.x).set(coordinate.y, true);
            queue.push(new Element(coordinate, 0));
        }
        while (!queue.isEmpty()) {
            Element element = queue.pop();
            int i = element.coordinate.x, j = element.coordinate.y;
            timeTaken = Math.max(timeTaken, element.t);
            List<Coordinate> neighbours = getNeighbours(matrix, element.coordinate, n, m, visited);
            for (Coordinate neighbour : neighbours) {
                matrix.get(neighbour.x).set(neighbour.y, 2);
                visited.get(neighbour.x).set(neighbour.y, true);
                queue.push(new Element(neighbour, element.t + 1));
            }
        }

        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (matrix.get(i).get(j) == 1) {
                    return -1;
                }
            }
        }

        return timeTaken;
    }

    private static List<Coordinate> getNeighbours(List<List<Integer>> matrix, Coordinate coordinate, int n, int m, List<List<Boolean>> visited) {
        List<Coordinate> neighbours = new ArrayList<>();
        int i = coordinate.x, j = coordinate.y;
        if (0 <= i - 1 && i - 1 < n && !visited.get(i - 1).get(j) && matrix.get(i - 1).get(j) == 1) {
            neighbours.add(new Coordinate(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m && !visited.get(i).get(j + 1) && matrix.get(i).get(j + 1) == 1) {
            neighbours.add(new Coordinate(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n && !visited.get(i + 1).get(j) && matrix.get(i + 1).get(j) == 1) {
            neighbours.add(new Coordinate(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m && !visited.get(i).get(j - 1) && matrix.get(i).get(j - 1) == 1) {
            neighbours.add(new Coordinate(i, j - 1));
        }
        return neighbours;
    }

    private static void getBlankVisitedMatrix(List<List<Boolean>> visited, int n, int m) {
        for (int i = 0; i < n; i += 1) {
            List<Boolean> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(false);
            }
            visited.add(row);
        }
    }

    private static List<Coordinate> getRottenOranges(List<List<Integer>> matrix, int n, int m) {
        List<Coordinate> result = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (matrix.get(i).get(j) == 2) {
                    result.add(new Coordinate(i, j));
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(0, 1, 2),
                                Arrays.asList(0, 1, 2),
                                Arrays.asList(2, 1, 1)
                        )
                )
        );

        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(2, 2, 0, 1)
                        )
                )
        );

        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(2, 2, 2),
                                Arrays.asList(0, 2, 0)
                        )
                )
        );

        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(2, 1, 1),
                                Arrays.asList(1, 1, 0),
                                Arrays.asList(0, 1, 1)
                        )
                )
        );

        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(0, 2)
                        )
                )
        );

        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(2, 1, 0, 2, 1),
                                Arrays.asList(1, 0, 1, 2, 1),
                                Arrays.asList(1, 0, 0, 2, 1)
                        )
                )
        );

        System.out.println(
                Solution.rot(
                        Arrays.asList(
                                Arrays.asList(2, 1, 0, 2, 1),
                                Arrays.asList(0, 0, 1, 2, 1),
                                Arrays.asList(1, 0, 0, 2, 1)
                        )
                )
        );

    }
}
