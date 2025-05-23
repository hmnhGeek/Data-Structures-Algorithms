// Problem link - https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
// Solution - https://www.youtube.com/watch?v=-tgVpUgsQ5k&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

package Graphs.G5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> bfs(Map<T, List<T>> graph, T startNode) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */

        // if the starting node is not present in the graph, return null.
        if (!graph.containsKey(startNode)) return null;

        // create a visited map. It will take O(V) space.
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }

        // create a queue and push the starting node inside it.
        Queue<T> queue = new Queue<>();
        queue.push(startNode);

        // mark the starting node as visited now.
        visited.put(startNode, true);

        // create a result list.
        List<T> result = new ArrayList<>();

        // typical BFS, this will run in O(V + E) time.
        while (!queue.isEmpty()) {
            // pop the current node and add it to the result list.
            T node = queue.pop();
            result.add(node);

            // loop on the adjacent nodes of this node in O(E) time.
            for (T adjNode : graph.get(node)) {
                // if the adjacent node is not yet visited, then mark it visited and push it to the queue.
                if (!visited.get(adjNode)) {
                    queue.push(adjNode);
                    visited.put(adjNode, true);
                }
            }
        }

        // finally, return the result.
        return result;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(1, List.of(2, 6));
        graph1.put(2, List.of(1, 3, 4));
        graph1.put(3, List.of(2));
        graph1.put(4, List.of(2, 5));
        graph1.put(5, List.of(4, 7));
        graph1.put(6, List.of(1, 7, 8));
        graph1.put(7, List.of(5, 6));
        graph1.put(8, List.of(6));
        System.out.println(bfs(graph1, 1));

        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, List.of(1, 2, 3));
        graph2.put(1, List.of(0));
        graph2.put(2, List.of(0, 4));
        graph2.put(3, List.of(0));
        graph2.put(4, List.of(2));
        System.out.println(Solution.bfs(graph2, 0));

        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, List.of(1, 2));
        graph3.put(1, List.of(0, 2));
        graph3.put(2, List.of(1, 0, 3, 4));
        graph3.put(3, List.of(2));
        graph3.put(4, List.of(2));
        System.out.println(Solution.bfs(graph3, 0));
    }
}
