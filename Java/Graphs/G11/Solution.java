// Problem link - https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
// Solution - https://www.youtube.com/watch?v=BPlrALf1LDU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=11

package Graphs.G11;

import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Element<T> {
    private T node;
    private T parent;

    public Element(T node, T parent) {
        this.node = node;
        this.parent = parent;
    }

    public T getNode() {
        return node;
    }

    public void setNode(T node) {
        this.node = node;
    }

    public T getParent() {
        return parent;
    }

    public void setParent(T parent) {
        this.parent = parent;
    }
}


public class Solution {
    private static <T> Map<T, Boolean> getVisited(Map<T, List<T>> graph) {
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        return visited;
    }

    public static <T> Boolean hasCycle(Map<T, List<T>> graph, T startNode) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */
        Queue<Element<T>> queue = new Queue<>();
        Map<T, Boolean> visited = getVisited(graph);
        queue.push(new Element<>(startNode, null));
        visited.put(startNode, true);
        while (!queue.isEmpty()) {
            Element<T> element = queue.pop();
            T node = element.getNode(), parent = element.getParent();
            for (T adjNode : graph.get(node)) {
                if (adjNode != parent && visited.get(adjNode)) {
                    return true;
                }
                if (adjNode == parent) {
                    continue;
                }
                visited.put(adjNode, true);
                queue.push(new Element<>(adjNode, node));
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph1 = Map.of(
                1, List.of(2, 3),
                2, List.of(1, 5),
                3, List.of(1, 4, 6),
                4, List.of(3),
                5, List.of(2, 7),
                6, List.of(3, 7),
                7, List.of(5, 6)
        );
        System.out.println(Solution.hasCycle(graph1, 1));

        Map<Integer, List<Integer>> graph2 = Map.of(
                1, List.of(2, 3),
                2, List.of(1, 5),
                3, List.of(1, 4, 6),
                4, List.of(3),
                5, List.of(2, 7),
                6, List.of(3),
                7, List.of(5)
        );
        System.out.println(Solution.hasCycle(graph2, 1));

        Map<Integer, List<Integer>> graph3 = Map.of(
                0, List.of(1, 2),
                1, List.of(0, 2),
                2, List.of(0, 1, 3),
                3, List.of(2)
        );
        System.out.println(Solution.hasCycle(graph3, 0));

        Map<Integer, List<Integer>> graph4 = Map.of(
                0, List.of(1),
                1, List.of(0, 2),
                2, List.of(1, 3),
                3, List.of(2)
        );
        System.out.println(Solution.hasCycle(graph4, 0));

        Map<Integer, List<Integer>> graph5 = Map.of(
                0, List.of(),
                1, List.of(2),
                2, List.of(1, 3),
                3, List.of(2)
        );
        System.out.println(Solution.hasCycle(graph5, 1));

        Map<Integer, List<Integer>> graph6 = Map.of(
                0, List.of(1),
                1, List.of(0, 2, 4),
                2, List.of(1, 3),
                3, List.of(2, 4),
                4, List.of(1, 3)
        );
        System.out.println(Solution.hasCycle(graph6, 0));
    }

}
