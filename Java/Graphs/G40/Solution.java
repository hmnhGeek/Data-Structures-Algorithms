// Problem link - https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=%2Fnumber-of-ways-to-arrive-at-destination
// Solution - https://www.youtube.com/watch?v=_-0mx0SmYxA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=40


package Graphs.G40;


import java.util.*;

public class Solution {
    public static List<List<Integer>> getAllShortestPaths(Map<Integer, List<Edge>> graph, Integer source, Integer destination) {
        if (!graph.containsKey(source) || !graph.containsKey(destination)) return null;
        Queue<Element> queue = new Queue<>();
        Map<Integer, Integer> distances = new HashMap<>();
        Map<Integer, List<Integer>> parents = new HashMap<>();
        for (Integer node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
            parents.put(node, new ArrayList<>());
        }
        distances.put(source, 0);
        queue.enqueue(new Element(0, source));
        while (!queue.isEmpty()) {
            Element element = queue.dequeue();
            Integer distance = element.distance, node = element.node;
            for (Edge edge : graph.get(node)) {
                Integer adjNode = edge.node, wt = edge.distance;
                if (wt + distance < distances.get(adjNode)) {
                    parents.put(adjNode, new ArrayList<>(Arrays.asList(node)));
                    distances.put(adjNode, wt + distance);
                    queue.enqueue(new Element(wt + distance, adjNode));
                } else if (wt + distance == distances.get(adjNode)) {
                    parents.get(adjNode).add(node);
                }
            }
        }
        return constructPaths(parents, destination);
    }

    private static List<List<Integer>> constructPaths(Map<Integer, List<Integer>> parents, Integer destination) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        solve(parents, destination, path, result);
        return result;
    }

    private static void solve(Map<Integer, List<Integer>> parents, Integer node, List<Integer> path, List<List<Integer>> result) {
        if (parents.get(node).isEmpty()) {
            List<Integer> copy = new ArrayList<>(path);
            copy.add(node);
            result.add(copy.reversed());
            return;
        }
        for (Integer parent : parents.get(node)) {
            path.add(node);
            solve(parents, parent, path, result);
            path.remove(node);
        }
    }

    public static void main(String[] args) {

        // First graph
        Map<Integer, List<Edge>> graph1 = new HashMap<>();
        graph1.put(0, Arrays.asList(new Edge(1, 2), new Edge(4, 5), new Edge(6, 7)));
        graph1.put(1, Arrays.asList(new Edge(0, 2), new Edge(2, 3), new Edge(3, 3)));
        graph1.put(2, Arrays.asList(new Edge(1, 3), new Edge(5, 1)));
        graph1.put(3, Arrays.asList(new Edge(1, 3), new Edge(6, 3), new Edge(5, 1)));
        graph1.put(4, Arrays.asList(new Edge(0, 5), new Edge(6, 2)));
        graph1.put(5, Arrays.asList(new Edge(2, 1), new Edge(3, 1), new Edge(6, 1)));
        graph1.put(6, Arrays.asList(new Edge(0, 7), new Edge(3, 3), new Edge(4, 2), new Edge(5, 1)));

        List<List<Integer>> paths1 = getAllShortestPaths(graph1, 0, 6);
        System.out.println(paths1);


        // Second graph
        Map<Integer, List<Edge>> graph2 = new HashMap<>();
        graph2.put(0, Arrays.asList(new Edge(1, 1), new Edge(2, 2), new Edge(5, 8)));
        graph2.put(1, Arrays.asList(new Edge(0, 1), new Edge(2, 3), new Edge(3, 3)));
        graph2.put(2, Arrays.asList(new Edge(1, 3), new Edge(0, 2), new Edge(5, 6)));
        graph2.put(3, Arrays.asList(new Edge(1, 3), new Edge(4, 2)));
        graph2.put(4, Arrays.asList(new Edge(3, 2), new Edge(5, 2)));
        graph2.put(5, Arrays.asList(new Edge(2, 6), new Edge(4, 2), new Edge(0, 8)));

        List<List<Integer>> paths2 = getAllShortestPaths(graph2, 0, 5);
        System.out.println(paths2);
    }
}
