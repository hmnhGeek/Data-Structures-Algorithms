package Graphs.G17;

import java.util.*;

public class Solution {
    private static int toggleColor(int color) {
        if (color == 0) return 1;
        return 0;
    }

    public static <T> Boolean isBipartite(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        getBlankVisitedArray(visited, graph);

        Map<T, Integer> colors = new HashMap<>();
        getBlankColorsArray(colors, graph);

        Queue<T> queue = new Queue<>();
        T startNode = graph.keySet().stream().toList().getFirst();
        queue.push(startNode);
        visited.put(startNode, true);
        int initialColor = 0;
        colors.put(startNode, initialColor);

        while (!queue.isEmpty()) {
            T node = queue.pop();
            for (T adjNode : graph.get(node)) {
                if (!visited.get(adjNode)) {
                    visited.put(adjNode, true);
                    colors.put(adjNode, toggleColor(colors.get(node)));
                    queue.push(adjNode);
                } else {
                    if (colors.get(node) == colors.get(adjNode)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private static <T> void getBlankVisitedArray(Map<T, Boolean> visited, Map<T, List<T>> graph) {
        for (T node : graph.keySet()) {
            visited.putIfAbsent(node, false);
        }
    }

    private static <T> void getBlankColorsArray(Map<T, Integer> colors, Map<T, List<T>> graph) {
        for (T node : graph.keySet()) {
            colors.putIfAbsent(node, null);
        }
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
            System.out.println(isBipartite(graph));
        }
    }
}
