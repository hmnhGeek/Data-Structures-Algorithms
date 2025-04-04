package DynamicProgramming;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

class DP50Recursive {
    private static Integer solve(List<Integer> arr, Integer i, Integer j) {
        if (i > j) {
            return 0;
        }
        int minCost = Integer.MAX_VALUE;
        for (int k = i; k <= j; k += 1) {
            int cost = arr.get(j + 1) - arr.get(i - 1) + solve(arr, i, k - 1) + solve(arr, k + 1, j);
            minCost = Math.min(cost, minCost);
        }
        return minCost;
    }

    public static Integer getMinCostToCutRod(List<Integer> arr, Integer length) {
        int n = arr.size();
        arr.sort(null);
        List<Integer> rod = Stream.of(List.of(0), arr, List.of(length)).flatMap(List::stream).toList();
        return DP50Recursive.solve(rod, 1, n);
    }
}

class Solution {
    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3), 4));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3, 4), 5));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3), 10));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(5, 6, 1, 4, 2), 9));
    }
}