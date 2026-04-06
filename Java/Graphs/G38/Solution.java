package Graphs.G38;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public class Solution {
    public static Integer getCheapestFlight(Map<Integer, List<List<Integer>>> graph,
                                           Integer source, Integer destination, Integer k) {
        if (!(graph.containsKey(source) && graph.containsKey(destination))) return null;
        MinHeap<HeapElement<Integer>> pq = new MinHeap<>();
        Map<Integer, Integer> distances = new HashMap<>();
        for (Integer node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(source, 0);
        pq.insert(new HeapElement<>(0, 0, source));
        while (!pq.isEmpty()) {
            HeapElement<Integer> heapElement = pq.pop();
            Integer distance = heapElement.distance, stops = heapElement.intermediateStops, node = heapElement.node;
            if (stops > k) continue;
            if (Objects.equals(node, destination)) return distance;
            List<List<Integer>> neighbours = graph.get(node);
            for (List<Integer> stop : neighbours) {
                Integer adjNode = stop.getFirst(), cost = stop.getLast();
                if (Objects.equals(adjNode, destination) && distance + cost < distances.get(adjNode)) {
                    pq.insert(new HeapElement<>(distance + cost, stops, adjNode));
                    distances.put(adjNode, distance + cost);
                } else if (distance + cost < distances.get(adjNode) && stops + 1 <= k) {
                    pq.insert(new HeapElement<>(distance + cost, stops + 1, adjNode));
                }
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getCheapestFlight(
                        Map.of(
                                0, List.of(List.of(1, 5), List.of(3, 2)),
                                1, List.of(List.of(2, 5), List.of(4, 1)),
                                2, List.of(),
                                3, List.of(List.of(1, 2)),
                                4, List.of(List.of(2, 1))
                        ),
                        0,
                        2,
                        2
                )
        );

        System.out.println(
                Solution.getCheapestFlight(
                        Map.of(
                                0, List.of(List.of(1, 100)),
                                1, List.of(List.of(2, 100), List.of(3, 600)),
                                2, List.of(List.of(0, 100), List.of(3, 200)),
                                3, List.of()
                        ),
                        0,
                        3,
                        1
                )
        );

        System.out.println(
                Solution.getCheapestFlight(
                        Map.of(
                                0, List.of(List.of(1, 100), List.of(2, 500)),
                                1, List.of(List.of(2, 100)),
                                2, List.of()
                        ),
                        0,
                        2,
                        0
                )
        );
    }
}
