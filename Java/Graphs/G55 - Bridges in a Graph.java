package Graphs;


import java.util.*;

class SolutionG55 {
    private static  Integer timer = 1;

    private static <T> Map<T, Boolean> getNewVisitedMap(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }

    private static <T> Map<T, Integer> getTimerMap(Map<T, List<T>> graph) {
        Map<T, Integer> t = new HashMap<>();
        for (T node : graph.keySet()) {
            t.put(node, null);
        }
        return t;
    }

    private static <T> void dfs(Map<T, List<T>> graph, T node, T parent, Map<T, Integer> tin, Map<T, Integer> low, Map<T, Boolean> visited, List<List<T>> bridges) {
        visited.put(node, true);
        tin.put(node, timer);
        low.put(node, timer);
        timer += 1;
        for (T adjNode : graph.get(node)) {
            if (parent == adjNode) continue;
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, node, tin, low, visited, bridges);
                low.put(node, Math.min(low.get(node), low.get(adjNode)));
                if (low.get(node) < low.get(adjNode)) {
                    bridges.add(List.of(node, adjNode));
                }
            } else {
                low.put(node, Math.min(low.get(node), low.get(adjNode)));
            }
        }
    }

    private static <T> List<List<T>> getBridges(Map<T, List<T>> graph) {
        timer = 1;
        Map<T, Boolean> visited = getNewVisitedMap(graph);
        Map<T, Integer> tin = getTimerMap(graph);
        Map<T, Integer> low = getTimerMap(graph);
        List<List<T>> bridges = new ArrayList<>();
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                dfs(graph, node, null, tin, low, visited, bridges);
            }
        }
        return bridges;
    }

    public static void main(String[] args) {
        // Example 1
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(1, Arrays.asList(2, 4));
        graph1.put(2, Arrays.asList(1, 3));
        graph1.put(3, Arrays.asList(2, 4));
        graph1.put(4, Arrays.asList(1, 3, 5));
        graph1.put(5, Arrays.asList(4, 6));
        graph1.put(6, Arrays.asList(5, 7, 9));
        graph1.put(7, Arrays.asList(6, 8));
        graph1.put(8, Arrays.asList(7, 9, 10));
        graph1.put(9, Arrays.asList(6, 8));
        graph1.put(10, Arrays.asList(8, 11));
        graph1.put(11, Arrays.asList(10, 12));
        graph1.put(12, Arrays.asList(10, 11));
        System.out.println(getBridges(graph1));
    }
}