// Problem link - https://leetcode.com/problems/critical-connections-in-a-network/description/
// Solution - https://www.youtube.com/watch?v=qrAub5z8FeA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=55


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
        // mark the node as visited.
        visited.put(node, true);

        // update the insertion and lower time with timer value.
        tin.put(node, timer);
        low.put(node, timer);

        // increment the global timer.
        timer += 1;

        // loop on the adjacent nodes of this node
        for (T adjNode : graph.get(node)) {
            // if the adjacent node itself is the parent node, nothing needs to be done.
            if (parent == adjNode) continue;

            // if the adjacent node is not visited, start a DFS on it.
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, node, tin, low, visited, bridges);

                // after backtracking, update the low time of this node with the low time of the adjacent node update
                // just now.
                low.put(node, Math.min(low.get(node), low.get(adjNode)));

                // if low time of adjacent node is more than low time of node, then it means we cannot reach this
                // adjacent node except via node. Thus, this edge is a bridge.
                if (low.get(node) < low.get(adjNode)) {
                    bridges.add(List.of(node, adjNode));
                }
            } else {
                // if the adjacent node is already visited, simply update the low time of the node.
                low.put(node, Math.min(low.get(node), low.get(adjNode)));
            }
        }
    }

    private static <T> List<List<T>> getBridges(Map<T, List<T>> graph) {
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

        // define the bridges list.
        List<List<T>> bridges = new ArrayList<>();

        // loop on the graph nodes
        for (T node : graph.keySet()) {
            // and if the node is not visited, start a DFS from it. It will take O(V + E) time.
            if (!visited.get(node)) {
                dfs(graph, node, null, tin, low, visited, bridges);
            }
        }

        // return the bridges
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

        // Example 2
        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, Arrays.asList(1, 2));
        graph2.put(1, Arrays.asList(0, 2, 3));
        graph2.put(2, Arrays.asList(1, 0));
        graph2.put(3, Arrays.asList(1));
        System.out.println(getBridges(graph2));

        // Example 3
        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, Arrays.asList(1, 2, 3));
        graph3.put(1, Arrays.asList(0, 2));
        graph3.put(2, Arrays.asList(1, 0));
        graph3.put(3, Arrays.asList(0, 4));
        graph3.put(4, Arrays.asList(3));
        System.out.println(getBridges(graph3));

        // Example 4
        Map<Integer, List<Integer>> graph4 = new HashMap<>();
        graph4.put(0, Arrays.asList(1, 2));
        graph4.put(1, Arrays.asList(0, 2, 6, 4, 3));
        graph4.put(2, Arrays.asList(0, 1));
        graph4.put(3, Arrays.asList(1, 5));
        graph4.put(4, Arrays.asList(1, 5));
        graph4.put(5, Arrays.asList(3, 4));
        graph4.put(6, Arrays.asList(1));
        System.out.println(getBridges(graph4));

        // Example 5
        Map<Integer, List<Integer>> graph5 = new HashMap<>();
        graph5.put(0, Arrays.asList(1));
        graph5.put(1, Arrays.asList(0, 2));
        graph5.put(2, Arrays.asList(1, 3));
        graph5.put(3, Arrays.asList(2));
        System.out.println(getBridges(graph5));
    }
}