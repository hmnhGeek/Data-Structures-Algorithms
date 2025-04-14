// Problem link - https://leetcode.com/problems/critical-connections-in-a-network/description/
// Solution - https://www.youtube.com/watch?v=qrAub5z8FeA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=55


package Graphs;


import java.util.*;

class SolutionG56 {
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

    private static <T> void dfs(Map<T, List<T>> graph, T node, T parent, Map<T, Integer> tin, Map<T, Integer> low, Map<T, Boolean> visited, Map<T, Boolean> articulationPoints) {
        // mark the node as visited.
        visited.put(node, true);

        // update the insertion and lower time with timer value.
        tin.put(node, timer);
        low.put(node, timer);

        // increment the global timer.
        timer += 1;

        int childCount = 0;

        // loop on the adjacent nodes of this node
        for (T adjNode : graph.get(node)) {
            // if the adjacent node itself is the parent node, nothing needs to be done.
            if (parent == adjNode) continue;

            // if the adjacent node is not visited, start a DFS on it.
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, node, tin, low, visited, articulationPoints);

                // after backtracking, update the low time of this node with the low time of the adjacent node update
                // just now.
                low.put(node, Math.min(low.get(node), low.get(adjNode)));

                // if low time of adjacent node is more than low time of node, then it means we cannot reach this
                // adjacent node except via node. Thus, this edge is a bridge.
                if (low.get(adjNode) >= tin.get(node) && parent != null) {
                    articulationPoints.put(node, true);
                }
                childCount += 1;
            } else {
                // if the adjacent node is already visited, simply update the low time of the node.
                low.put(node, Math.min(low.get(node), tin.get(adjNode)));
            }
        }
        if (childCount > 1 && parent == null) {
            articulationPoints.put(node, true);
        }
    }

    private static <T> List<T> getArticulationPoints(Map<T, List<T>> graph) {
        /*
         Time complexity is O(V + E) and space complexity is O(V).
         */

        // reset the global timer to 1.
        timer = 1;

        // get the visited map in O(V + E) time.
        Map<T, Boolean> visited = getNewVisitedMap(graph);

        // define the tin and low times for the graph nodes in O(V + E) time.
        Map<T, Integer> tin = getTimerMap(graph);
        Map<T, Integer> low = getTimerMap(graph);

        // define the articulation points.
        Map<T, Boolean> articulationPoint = new HashMap<>();
        for (T node : graph.keySet()) {
            articulationPoint.put(node, false);
        }

        // loop on the graph nodes
        for (T node : graph.keySet()) {
            // and if the node is not visited, start a DFS from it. It will take O(V + E) time.
            if (!visited.get(node)) {
                dfs(graph, node, null, tin, low, visited, articulationPoint);
            }
        }

        return articulationPoint.entrySet().stream()
                .filter(Map.Entry::getValue)
                .map(Map.Entry::getKey)
                .toList();
    }

    public static void main(String[] args) {
        // Example 1
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(0, Arrays.asList(1, 2, 3));
        graph1.put(1, Arrays.asList(0));
        graph1.put(2, Arrays.asList(0, 3, 4, 5));
        graph1.put(3, Arrays.asList(0, 2));
        graph1.put(4, Arrays.asList(2, 6));
        graph1.put(5, Arrays.asList(2, 6));
        graph1.put(6, Arrays.asList(4, 5));
        System.out.println(getArticulationPoints(graph1));

        // Example 2
        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(1, Arrays.asList(2, 3));
        graph2.put(2, Arrays.asList(1, 3));
        graph2.put(3, Arrays.asList(1, 2, 4));
        graph2.put(4, Arrays.asList(3, 5));
        graph2.put(5, Arrays.asList(4));
        System.out.println(getArticulationPoints(graph2));

        // Example 3
        Map<Character, List<Character>> graph3 = new HashMap<>();
        graph3.put('A', Arrays.asList('B', 'C'));
        graph3.put('B', Arrays.asList('A', 'D'));
        graph3.put('C', Arrays.asList('A', 'D', 'E'));
        graph3.put('D', Arrays.asList('B', 'C', 'E'));
        graph3.put('E', Arrays.asList('C', 'D', 'F', 'G'));
        graph3.put('F', Arrays.asList('E', 'G'));
        graph3.put('G', Arrays.asList('E', 'F'));
        System.out.println(getArticulationPoints(graph3));

        // Example 4
        Map<Integer, List<Integer>> graph4 = new HashMap<>();
        graph4.put(1, Arrays.asList(2));
        graph4.put(2, Arrays.asList(3));
        graph4.put(3, Arrays.asList(4));
        graph4.put(4, Arrays.asList(5));
        graph4.put(5, Arrays.asList());
        System.out.println(getArticulationPoints(graph4));
    }
}