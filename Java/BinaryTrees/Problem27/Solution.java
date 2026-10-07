// Problem link - https://www.geeksforgeeks.org/dsa/check-given-graph-tree/#approach-1-check-for-cycle-and-connectivity-ov-e-time-and-ov-space
// Solution - https://www.youtube.com/watch?v=BPlrALf1LDU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=11


package BinaryTrees.Problem27;

import java.util.*;


class Element<T> {
    public T node;
    public T parent;

    public Element(T node, T parent) {
        this.node = node;
        this.parent = parent;
    }
}


public class Solution {
    public static void main(String[] args) {
        System.out.println(
                isGraphTree(
                        Arrays.asList(
                                List.of(0, 1),
                                List.of(0, 2),
                                List.of(1, 2),
                                List.of(2, 3)
                        )
                )
        );

        System.out.println(
                isGraphTree(
                        Arrays.asList(
                                List.of(0, 1),
                                List.of(1, 2),
                                List.of(2, 3)
                        )
                )
        );

        System.out.println(
                isGraphTree(
                        Arrays.asList(
                                List.of(0, 1),
                                List.of(0, 2),
                                List.of(0, 3),
                                List.of(4, 1)
                        )
                )
        );

        System.out.println(
                isGraphTree(
                        Arrays.asList(
                                List.of(0, 1),
                                List.of(1, 2),
                                List.of(1, 4),
                                List.of(2, 3),
                                List.of(1, 3)
                        )
                )
        );
    }

    public static <T> boolean isGraphTree(List<List<T>> edges) {
        int m = edges.size();
        Set<T> nodes = findNodes(edges);
        if (m != nodes.size() - 1) return false;
        Map<T, List<T>> adjacencyList = getAdjacencyList(edges, nodes);
        Queue<Element<T>> queue = new Queue<>();
        T startNode = adjacencyList.keySet().stream().toList().getFirst();
        Map<T, Boolean> visited = getVisitedMap(nodes);
        visited.put(startNode, true);
        queue.push(new Element<>(startNode, null));
        while (!queue.isEmpty()) {
            Element<T> element = queue.pop();
            T node = element.node, parent = element.parent;
            for (T adjNode : adjacencyList.get(node)) {
                if (visited.get(adjNode).equals(Boolean.TRUE) && adjNode.equals(parent)) {
                    continue;
                }
                if (visited.get(adjNode).equals(Boolean.TRUE)) {
                    return false;
                } else {
                    visited.put(adjNode, true);
                    queue.push(new Element<>(adjNode, node));
                }
            }
        }
        return true;
    }

    private static <T> Map<T, Boolean> getVisitedMap(Set<T> nodes) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : nodes) {
            visited.put(node, false);
        }
        return visited;
    }

    private static <T> Map<T, List<T>> getAdjacencyList(List<List<T>> edges, Set<T> nodes) {
        Map<T, List<T>> adjList = new HashMap<>();
        for (T node : nodes) {
            adjList.put(node, new ArrayList<>());
        }
        for (List<T> edge : edges) {
            T node1 = edge.getFirst(), node2 = edge.getLast();
            adjList.get(node1).add(node2);
            adjList.get(node2).add(node1);
        }
        return adjList;
    }

    private static <T> Set<T> findNodes(List<List<T>> edges) {
        Set<T> nodes = new HashSet<>();
        for (List<T> edge : edges) {
            nodes.add(edge.getFirst());
            nodes.add(edge.getLast());
        }
        return nodes;
    }
}
