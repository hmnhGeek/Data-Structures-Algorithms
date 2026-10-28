package PracticeSet1.Graphs.G5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> bfs(Map<T, List<T>> graph, T startNode) {
        Map<T, Boolean> visited = getBlankVisitedArray(graph);
        Queue<T> queue = new Queue<>();
        queue.enqueue(startNode);
        visited.put(startNode, true);
        List<T> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            T node = queue.dequeue();
            res.add(node);
            for (T adjNode : graph.get(node)) {
                if (!visited.get(adjNode)) {
                    queue.enqueue(adjNode);
                    visited.put(adjNode, true);
                }
            }
        }
        return res;
    }

    private static <T> Map<T, Boolean> getBlankVisitedArray(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
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
        System.out.println(Graphs.G5.Solution.bfs(graph2, 0));

        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, List.of(1, 2));
        graph3.put(1, List.of(0, 2));
        graph3.put(2, List.of(1, 0, 3, 4));
        graph3.put(3, List.of(2));
        graph3.put(4, List.of(2));
        System.out.println(Graphs.G5.Solution.bfs(graph3, 0));
    }
}
