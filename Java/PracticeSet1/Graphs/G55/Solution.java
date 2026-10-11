// Problem link - https://leetcode.com/problems/critical-connections-in-a-network/description/
// Solution - https://www.youtube.com/watch?v=qrAub5z8FeA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=55


package PracticeSet1.Graphs.G55;

import java.util.*;

public class Solution {
    public static <T> List<List<T>> getBridges(Map<T, List<T>> graph) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */
        Map<T, Boolean> visited = getBlankVisitedArray(graph);
        Map<T, Integer> tin = new HashMap<>();
        Map<T, Integer> low = new HashMap<>();
        for (T node : graph.keySet()) {
            tin.put(node, 0);
            low.put(node, 0);
        }

        List<Integer> timer = Arrays.asList(1);
        List<List<T>> bridges = new ArrayList<>();
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(node, null, tin, low, visited, bridges, timer, graph);
            }
        }
        return bridges;
    }

    private static <T> void dfs(T node, T parent, Map<T, Integer> tin, Map<T, Integer> low, Map<T, Boolean> visited, List<List<T>> bridges, List<Integer> timer, Map<T, List<T>> graph) {
        visited.put(node, true);
        tin.put(node, timer.getFirst());
        low.put(node, timer.getFirst());
        timer.set(0, timer.getFirst() + 1);
        for (T adjNode : graph.get(node)) {
            if (adjNode == parent) continue;
            if (!visited.get(adjNode)) {
                dfs(adjNode, node, tin, low, visited, bridges, timer, graph);
                low.put(node, Math.min(low.get(node), low.get(adjNode)));
                if (low.get(adjNode) > tin.get(node)) {
                    bridges.add(List.of(node, adjNode));
                }
            } else {
                low.put(node, Math.min(low.get(node), low.get(adjNode)));
            }
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
        System.out.println(getBridges(Map.ofEntries(
                Map.entry(1, List.of(2, 4)),
                Map.entry(2, List.of(1, 3)),
                Map.entry(3, List.of(2, 4)),
                Map.entry(4, List.of(1, 3, 5)),
                Map.entry(5, List.of(4, 6)),
                Map.entry(6, List.of(5, 7, 9)),
                Map.entry(7, List.of(6, 8)),
                Map.entry(8, List.of(7, 9, 10)),
                Map.entry(9, List.of(6, 8)),
                Map.entry(10, List.of(8, 11)),
                Map.entry(11, List.of(10, 12)),
                Map.entry(12, List.of(10, 11))
        )));

        System.out.println(getBridges(Map.of(
                0, List.of(1, 2),
                1, List.of(0, 2, 3),
                2, List.of(1, 0),
                3, List.of(1)
        )));

        System.out.println(getBridges(Map.of(
                0, List.of(1, 2, 3),
                1, List.of(0, 2),
                2, List.of(1, 0),
                3, List.of(0, 4),
                4, List.of(3)
        )));

        System.out.println(getBridges(Map.of(
                0, List.of(1, 2),
                1, List.of(0, 2, 6, 4, 3),
                2, List.of(0, 1),
                3, List.of(1, 5),
                4, List.of(1, 5),
                5, List.of(3, 4),
                6, List.of(1)
        )));

        System.out.println(getBridges(Map.of(
                0, List.of(1),
                1, List.of(0, 2),
                2, List.of(1, 3),
                3, List.of(2)
        )));
    }
}
