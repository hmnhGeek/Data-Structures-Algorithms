package Graphs.G35;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Edge<T> {
    public T node;
    public Integer weight;

    public Edge(T node, Integer weight) {
        this.node = node;
        this.weight = weight;
    }
}


class QueueElement<T> {
    public T node;
    public Integer distance;

    public QueueElement(T node, Integer distance) {
        this.node = node;
        this.distance = distance;
    }
}


public class Solution {
    public static <T> List<T> getShortestPath(Map<T, List<Edge<T>>> graph, T source, T destination) {
        if (!graph.containsKey(source) || !graph.containsKey(destination)) return null;
        Queue<QueueElement<T>> queue = new Queue<>();

        // build distances map.
        Map<T, Integer> distances = new HashMap<>();
        for (T node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(source, 0);

        // push source node into queue
        queue.push(new QueueElement<>(source, 0));

        // build path map.
        Map<T, T> pathMap = new HashMap<>();
        for (T node : graph.keySet()) {
            pathMap.put(node, null);
        }

        while (!queue.isEmpty()) {
            QueueElement<T> element = queue.pop();
            T node = element.node;
            Integer distance = element.distance;
            for (Edge<T> edge : graph.get(node)) {
                T adjNode = edge.node;
                Integer weight = edge.weight;
                if (distances.get(adjNode) > weight + distance) {
                    distances.put(adjNode, weight + distance);
                    pathMap.put(adjNode, node);
                    queue.push(new QueueElement<>(adjNode, weight + distance));
                }
            }
        }

        List<T> shortestPath = new ArrayList<>();
        shortestPath.add(destination);
        T startNode = destination;
        while (pathMap.get(startNode) != null) {
            shortestPath.add(pathMap.get(startNode));
            startNode = pathMap.get(startNode);
        }
        return shortestPath.reversed();
    }

    public static void main(String[] args) {

        System.out.println(
                Solution.getShortestPath(
                        Map.of(
                                1, List.of(new Edge<>(2, 2), new Edge<>(4, 1)),
                                2, List.of(new Edge<>(1, 2), new Edge<>(3, 4), new Edge<>(5, 5)),
                                3, List.of(new Edge<>(2, 4), new Edge<>(4, 3), new Edge<>(5, 1)),
                                4, List.of(new Edge<>(1, 1), new Edge<>(3, 3)),
                                5, List.of(new Edge<>(2, 5), new Edge<>(3, 1))
                        ),
                        1,
                        5
                )
        );

        System.out.println(
                Solution.getShortestPath(
                        Map.of(
                                0, List.of(new Edge<>(1, 1), new Edge<>(2, 1)),
                                1, List.of(new Edge<>(0, 1), new Edge<>(4, 1)),
                                2, List.of(new Edge<>(0, 1), new Edge<>(3, 1)),
                                3, List.of(new Edge<>(2, 1), new Edge<>(5, 1)),
                                4, List.of(new Edge<>(1, 1), new Edge<>(5, 1)),
                                5, List.of(new Edge<>(3, 1), new Edge<>(4, 1))
                        ),
                        0,
                        4
                )
        );

        System.out.println(
                Solution.getShortestPath(
                        Map.of(
                                0, List.of(new Edge<>(1, 1), new Edge<>(2, 1)),
                                1, List.of(new Edge<>(0, 1), new Edge<>(4, 1), new Edge<>(3, 1)),
                                2, List.of(new Edge<>(0, 1), new Edge<>(3, 1)),
                                3, List.of(new Edge<>(2, 1), new Edge<>(5, 1), new Edge<>(1, 1)),
                                4, List.of(new Edge<>(1, 1), new Edge<>(5, 1)),
                                5, List.of(new Edge<>(3, 1), new Edge<>(4, 1))
                        ),
                        0,
                        5
                )
        );

        System.out.println(
                Solution.getShortestPath(
                        Map.of(
                                0, List.of(new Edge<>(1, 4), new Edge<>(7, 8)),
                                1, List.of(new Edge<>(0, 4), new Edge<>(2, 8), new Edge<>(7, 11)),
                                2, List.of(new Edge<>(1, 8), new Edge<>(8, 2), new Edge<>(5, 4), new Edge<>(3, 7)),
                                3, List.of(new Edge<>(2, 7), new Edge<>(5, 14), new Edge<>(4, 9)),
                                4, List.of(new Edge<>(3, 9), new Edge<>(5, 10)),
                                5, List.of(new Edge<>(6, 2), new Edge<>(2, 4), new Edge<>(3, 14), new Edge<>(4, 10)),
                                6, List.of(new Edge<>(7, 1), new Edge<>(8, 6), new Edge<>(5, 2)),
                                7, List.of(new Edge<>(0, 8), new Edge<>(1, 11), new Edge<>(8, 7), new Edge<>(6, 1)),
                                8, List.of(new Edge<>(2, 2), new Edge<>(7, 7), new Edge<>(6, 6))
                        ),
                        0,
                        4
                )
        );

        System.out.println(
                Solution.getShortestPath(
                        Map.of(
                                0, List.of(new Edge<>(1, 4), new Edge<>(7, 8)),
                                1, List.of(new Edge<>(0, 4), new Edge<>(2, 8), new Edge<>(7, 11)),
                                2, List.of(new Edge<>(1, 8), new Edge<>(8, 2), new Edge<>(5, 4), new Edge<>(3, 7)),
                                3, List.of(new Edge<>(2, 7), new Edge<>(5, 14), new Edge<>(4, 9)),
                                4, List.of(new Edge<>(3, 9), new Edge<>(5, 10)),
                                5, List.of(new Edge<>(6, 2), new Edge<>(2, 4), new Edge<>(3, 14), new Edge<>(4, 10)),
                                6, List.of(new Edge<>(7, 1), new Edge<>(8, 6), new Edge<>(5, 2)),
                                7, List.of(new Edge<>(0, 8), new Edge<>(1, 11), new Edge<>(8, 7), new Edge<>(6, 1)),
                                8, List.of(new Edge<>(2, 2), new Edge<>(7, 7), new Edge<>(6, 6))
                        ),
                        0,
                        8
                )
        );
    }
}
