package BinaryTrees.Problem27;

import java.util.List;
import java.util.Map;


class Element<T> {
    public T node;
    public T parent;

    public Element(T node, T parent) {
        this.node = node;
        this.parent = parent;
    }
}


public class Solution {
    public static <T> boolean isGraphTree(List<List<T>> edges, int n, int m) {
        if (m != n - 1) return false;
        Map<T, List<T>> adjacencyList = getAdjacencyList(edges, n);
        Queue<Element<T>> queue = new Queue<>();
        T startNode = adjacencyList.keySet().stream().toList().getFirst();
        Map<T, Boolean> visited = getVisitedMap(adjacencyList);
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
}
