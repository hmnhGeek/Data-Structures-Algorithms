// Problem link - https://www.geeksforgeeks.org/problems/number-of-provinces/1
// Solution - https://www.youtube.com/watch?v=ACzkVtewUYA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=7

package Graphs.G7;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> void dfs(Map<T, List<T>> graph, T node, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                dfs(graph, adjNode, visited);
            }
        }
    }

    public static <T> Integer getNumberOfProvinces(Map<T, List<T>> graph) {
        /*
            Time complexity is O(V + E) and space complexity is O(V).
         */
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.putIfAbsent(node, false);
        }
        int numComponents = 0;
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                numComponents += 1;
                dfs(graph, node, visited);
            }
        }
        return numComponents;
    }

    public static void main(String[] args) {
        System.out.println(
            Solution.getNumberOfProvinces(
                Map.of(
                    0, Arrays.asList(2),
                    1, Arrays.asList(),
                    2, Arrays.asList(0)
                )
            )
        );

        System.out.println(
                Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(1),
                                1, Arrays.asList(0)
                        )
                )
        );

        System.out.println(
                Solution.getNumberOfProvinces(
                        Map.of(
                                0, Arrays.asList(),
                                1, Arrays.asList(),
                                2, Arrays.asList()
                        )
                )
        );
    }
}
