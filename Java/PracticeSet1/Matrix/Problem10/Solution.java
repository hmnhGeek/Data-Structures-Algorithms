package PracticeSet1.Matrix.Problem10;

import java.util.*;

public class Solution {
    public static Set<Integer> findCommonElements(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Set<Integer> result = new HashSet<>(mtx.getFirst());
        Map<Integer, Boolean> visited = new HashMap<>();
        for (Integer i : mtx.getFirst()) {
            visited.put(i, false);
        }
        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                Integer elem = mtx.get(i).get(j);
                if (result.contains(elem)) {
                    visited.put(elem, true);
                }
            }

            for (Integer e : visited.keySet()) {
                if (visited.get(e).equals(false)) {
                    result.remove(e);
                }
            }

            visited.entrySet().removeIf(entry -> !entry.getValue());

            visited.replaceAll((k, v) -> false);
        }
        return visited.keySet();
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.findCommonElements(
                        Arrays.asList(
                                Arrays.asList(1, 2, 1, 4, 8),
                                Arrays.asList(3, 7, 8, 5, 1),
                                Arrays.asList(8, 7, 7, 3, 1),
                                Arrays.asList(8, 1, 2, 7, 9)
                        )
                )
        );

        System.out.println(
                Solution.findCommonElements(
                        Arrays.asList(
                                Arrays.asList(1, 4, 5, 6),
                                Arrays.asList(3, 4, 5, 6),
                                Arrays.asList(5, 6, 7, 2)
                        )
                )
        );

        System.out.println(
                Solution.findCommonElements(
                        Arrays.asList(
                                Arrays.asList(4, 6),
                                Arrays.asList(6, 4),
                                Arrays.asList(2, 6)
                        )
                )
        );

        System.out.println(
                Solution.findCommonElements(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(2, 2, 3),
                                Arrays.asList(2, 3, 1),
                                Arrays.asList(2, 3, 4)
                        )
                )
        );

        System.out.println(
                Solution.findCommonElements(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(0, 6, 0),
                                Arrays.asList(4, 6, 1)
                        )
                )
        );
    }
}
