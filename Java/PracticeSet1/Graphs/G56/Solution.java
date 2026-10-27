// Problem link - https://leetcode.com/problems/critical-connections-in-a-network/description/
// Solution - https://www.youtube.com/watch?v=qrAub5z8FeA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=55


package PracticeSet1.Graphs.G56;

import java.util.*;

public class Solution {
    public static <T> List<T> getArticulationPoints(Map<T, List<T>> graph) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */
        Map<T, Boolean> visited = getBlankVisitedArray(graph);
        Map<T, Integer> tin = new HashMap<>();
        Map<T, Integer> low = new HashMap<>();
        Map<T, Boolean> markedForArticulationPoint = getBlankVisitedArray(graph);
        for (T node : graph.keySet()) {
            tin.put(node, 0);
            low.put(node, 0);
        }

        List<Integer> timer = Arrays.asList(1);
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(node, null, tin, low, visited, markedForArticulationPoint, timer, graph);
            }
        }

        List<T> articulationPoints = new ArrayList<>();
        for (T node : graph.keySet()) {
            if (markedForArticulationPoint.get(node)) {
                articulationPoints.add(node);
            }
        }
        return articulationPoints;
    }

    private static <T> void dfs(T node, T parent, Map<T, Integer> tin, Map<T, Integer> low, Map<T, Boolean> visited, Map<T, Boolean> marked, List<Integer> timer, Map<T, List<T>> graph) {
        visited.put(node, true);
        tin.put(node, timer.getFirst());
        low.put(node, timer.getFirst());
        timer.set(0, timer.getFirst() + 1);
        int childCount = 0;
        for (T adjNode : graph.get(node)) {
            if (adjNode == parent) continue;
            if (!visited.get(adjNode)) {
                dfs(adjNode, node, tin, low, visited, marked, timer, graph);
                low.put(node, Math.min(low.get(node), low.get(adjNode)));
                if (low.get(adjNode) >= tin.get(node) && parent != null) {
                    marked.put(node, true);
                }
                childCount += 1;
            } else {
                low.put(node, Math.min(low.get(node), tin.get(adjNode)));
            }
        }
        if (childCount > 1 && parent == null) {
            marked.put(node, true);
        }
    }

    private static <T> Map<T, Boolean> getBlankVisitedArray(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }


    public static void main(String[] args) {
        System.out.println(Solution.getArticulationPoints(
                Map.of(
                        0, List.of(1, 2, 3),
                        1, List.of(0),
                        2, List.of(0, 3, 4, 5),
                        3, List.of(0, 2),
                        4, List.of(2, 6),
                        5, List.of(2, 6),
                        6, List.of(4, 5)
                )
        ));

        System.out.println(Solution.getArticulationPoints(
                Map.of(
                        1, List.of(2, 3),
                        2, List.of(1, 3),
                        3, List.of(1, 2, 4),
                        4, List.of(3, 5),
                        5, List.of(4)
                )
        ));

        System.out.println(Solution.getArticulationPoints(
                Map.of(
                        "A", List.of("B", "C"),
                        "B", List.of("A", "D"),
                        "C", List.of("A", "D", "E"),
                        "D", List.of("B", "C", "E"),
                        "E", List.of("C", "D", "F", "G"),
                        "F", List.of("E", "G"),
                        "G", List.of("E", "F")
                )
        ));

        System.out.println(Solution.getArticulationPoints(
                Map.of(
                        1, List.of(2),
                        2, List.of(1, 3),
                        3, List.of(2, 4),
                        4, List.of(3, 5),
                        5, List.of(4)
                )
        ));
    }

}
