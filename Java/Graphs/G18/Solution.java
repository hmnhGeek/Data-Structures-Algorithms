// Problem link - https://leetcode.com/problems/is-graph-bipartite/description/
// Solution - https://www.youtube.com/watch?v=9twcmtQj4DU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=19&pp=iAQB


package Graphs.G18;

import java.util.*;

public class Solution {
    public static <T> Boolean isComponentBipartite(Map<T, List<T>> graph, T startNode, T parentNode, Map<T, Integer> nodeColors, Integer color) {
        nodeColors.put(startNode, color);
        for (T adjNode : graph.get(startNode)) {
            if (adjNode == parentNode) {
                continue;
            } else if (nodeColors.get(adjNode) == null) {
                if (!isComponentBipartite(graph, adjNode, startNode, nodeColors, toggleColor(color))) {
                    return false;
                }
            } else {
                if (nodeColors.get(adjNode) == nodeColors.get(startNode)) {
                    return false;
                }
            }
        }
        return true;
    }

    private static int toggleColor(int color) {
        return color == 0 ? 1 : 0;
    }

    private static <T> Map<T, Integer> getColorsMap(Map<T, List<T>> graph) {
        Map<T, Integer> d = new HashMap<>();
        for (T node : graph.keySet()) {
            d.put(node, null);
        }
        return d;
    }

    public static <T> Boolean isGraphBipartite(Map<T, List<T>> graph) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */
        Map<T, Integer> nodeColors = getColorsMap(graph);
        for (T node : graph.keySet()) {
            if (nodeColors.get(node) == null) {
                int color = 0;
                if (!isComponentBipartite(graph, node, null, nodeColors, color)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<Map<Integer, List<Integer>>> graphs = new ArrayList<>();

        graphs.add(new HashMap<>(Map.of(
                1, Arrays.asList(2),
                2, Arrays.asList(3, 6),
                3, Arrays.asList(2, 4),
                4, Arrays.asList(3, 5, 7),
                5, Arrays.asList(4, 6),
                6, Arrays.asList(2, 5),
                7, Arrays.asList(4, 8),
                8, Arrays.asList(7)
        )));

        graphs.add(new HashMap<>(Map.of(
                1, Arrays.asList(2),
                2, Arrays.asList(1, 3, 5),
                3, Arrays.asList(2, 4),
                4, Arrays.asList(3, 5, 6),
                5, Arrays.asList(2, 4),
                6, Arrays.asList(4)
        )));

        graphs.add(new HashMap<>(Map.of(
                0, Arrays.asList(1),
                1, Arrays.asList(0, 2),
                2, Arrays.asList(1)
        )));

        graphs.add(new HashMap<>(Map.of(
                0, Arrays.asList(2, 3),
                1, Arrays.asList(2),
                2, Arrays.asList(0, 1, 3),
                3, Arrays.asList(0, 2)
        )));

        graphs.add(new HashMap<>(Map.of(
                0, Arrays.asList(1, 2, 3),
                1, Arrays.asList(0, 2),
                2, Arrays.asList(0, 1, 3),
                3, Arrays.asList(0, 2)
        )));

        graphs.add(new HashMap<>(Map.of(
                0, Arrays.asList(1, 3),
                1, Arrays.asList(0, 2),
                2, Arrays.asList(1, 3),
                3, Arrays.asList(0, 2)
        )));

        for (Map<Integer, List<Integer>> graph : graphs) {
            System.out.println(isGraphBipartite(graph));
        }
    }
}
