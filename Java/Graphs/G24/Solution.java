// # Problem link - https://www.geeksforgeeks.org/problems/course-schedule/1
//# Solution - https://www.youtube.com/watch?v=WAOfKpxYHR8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=24


package Graphs.G24;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static <T> List<T> courseSchedule(List<List<T>> courses) {
        /*
            Overall time complexity is O(V + E) and space complexity is O(V).
         */
        return getOrder(formulateGraph(courses));
    }

    private static <T> List<T> getOrder(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = getIndegrees(graph);
        Queue<T> queue = new Queue<>();
        List<T> order = new ArrayList<>();
        for (T node : indegrees.keySet()) {
            if (indegrees.get(node) == 0) {
                queue.push(node);
            }
        }
        while (!queue.isEmpty()) {
            T node = queue.pop();
            order.add(node);
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) - 1);
                if (indegrees.get(adjNode) == 0) {
                    queue.push(adjNode);
                }
            }
        }
        if (order.size() == graph.size()) return order;
        return null;
    }

    private static <T> Map<T, Integer> getIndegrees(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = new HashMap<>();
        for (T node : graph.keySet()) {
            indegrees.put(node, 0);
        }
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) + 1);
            }
        }
        return indegrees;
    }

    private static <T> Map<T, List<T>> formulateGraph(List<List<T>> courses) {
        Map<T, List<T>> graph = new HashMap<>();
        for (List<T> courseLink : courses) {
            for (T course : courseLink) {
                graph.putIfAbsent(course, new ArrayList<>());
            }
        }
        for (List<T> courseLink : courses) {
            T course = courseLink.getFirst(), dependency = courseLink.getLast();
            graph.get(dependency).add(course);
        }
        return graph;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.courseSchedule(
                        List.of(
                                List.of(1, 0)
                        )
                )
        );

        System.out.println(
                Solution.courseSchedule(
                        List.of(
                                List.of(1, 0),
                                List.of(2, 0),
                                List.of(3, 1),
                                List.of(3, 2)
                        )
                )
        );

        System.out.println(
                Solution.courseSchedule(
                        List.of(
                                List.of(0, 1),
                                List.of(1, 0)
                        )
                )
        );

        System.out.println(
                Solution.courseSchedule(
                        List.of(
                                List.of(1, 2),
                                List.of(2, 3),
                                List.of(2, 4),
                                List.of(3, 4),
                                List.of(4, 3)
                        )
                )
        );
    }
}
