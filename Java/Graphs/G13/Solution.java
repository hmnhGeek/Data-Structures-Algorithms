// Problem link - https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
// Solution - https://www.youtube.com/watch?v=edXdVwkYHF8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=13


package Graphs.G13;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                getDistanceOfNearestOnes(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(1, 1, 0, 0),
                                Arrays.asList(0, 0, 1, 1)
                        )
                )
        );
        System.out.println(
                getDistanceOfNearestOnes(
                        Arrays.asList(
                                Arrays.asList(1, 0, 1),
                                Arrays.asList(1, 1, 0),
                                Arrays.asList(1, 0, 0)
                        )
                )
        );
        System.out.println(
                getDistanceOfNearestOnes(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0, 1),
                                Arrays.asList(0, 0, 1, 1),
                                Arrays.asList(0, 1, 1, 0)
                        )
                )
        );
    }

    public static List<List<Integer>> getDistanceOfNearestOnes(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(nm).
         */

        // get visited and distance matrices in O(nm) time and O(nm) space.
        List<List<Boolean>> visited = getVisited(mtx);
        List<List<Integer>> distances = getDistances(mtx);

        // initialize a queue to perform BFS.
        Queue<List<Integer>> queue = new Queue<>();
        int n = mtx.size(), m = mtx.getFirst().size();

        // push the 1s into queue with distance 0 and mark them as visited.
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j).equals(1)) {
                    visited.get(i).set(j, true);
                    queue.push(List.of(i, j, 0));
                }
            }
        }

        // typical BFS
        while (!queue.isEmpty()) {
            List<Integer> cell = queue.pop();
            int i = cell.getFirst(), j = cell.get(1);
            distances
                    .get(i)
                    .set(
                            j,
                            Math.min(
                                    cell.getLast(),
                                    distances.get(i).get(j)
                            )
                    );

            // get the unvisited neighbour cells.
            List<List<Integer>> neighbours = getNeighbours(mtx, i, j, n, m, visited);

            // push them into queue and mark them as visited.
            for (List<Integer> neighbour : neighbours) {
                visited.get(neighbour.getFirst()).set(neighbour.getLast(), true);
                queue.push(List.of(neighbour.getFirst(), neighbour.getLast(), cell.getLast() + 1));
            }
        }
        return distances;
    }

    private static List<List<Integer>> getNeighbours(List<List<Integer>> mtx, int i, int j, int n, int m, List<List<Boolean>> visited) {
        List<List<Integer>> result = new ArrayList<>();
        if (0 <= i - 1 && i - 1 < n && !visited.get(i - 1).get(j)) {
            result.add(List.of(i - 1, j));
        }
        if (0 <= j + 1 && j + 1 < m && !visited.get(i).get(j + 1)) {
            result.add(List.of(i, j + 1));
        }
        if (0 <= i + 1 && i + 1 < n && !visited.get(i + 1).get(j)) {
            result.add(List.of(i + 1, j));
        }
        if (0 <= j - 1 && j - 1 < m && !visited.get(i).get(j - 1)) {
            result.add(List.of(i, j - 1));
        }
        return result;
    }

    private static List<List<Integer>> getDistances(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        List<List<Integer>> distances = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(Integer.MAX_VALUE);
            }
            distances.add(row);
        }
        return distances;
    }

    private static List<List<Boolean>> getVisited(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        List<List<Boolean>> visited = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<Boolean> row = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                row.add(false);
            }
            visited.add(row);
        }
        return visited;
    }
}
