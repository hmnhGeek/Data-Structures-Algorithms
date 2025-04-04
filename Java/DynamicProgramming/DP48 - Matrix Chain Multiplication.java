package DynamicProgramming;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class MCMRecursive {
    /**
     * Time complexity is exponential and space complexity is O(n).
     */

    private static Integer solve(List<Integer> arr, Integer i, Integer j) {
        if (i.equals(j)) {
            return 0;
        }
        int minValue = Integer.MAX_VALUE;
        for (int k = i; k < j; k += 1) {
            int cost = (arr.get(i - 1) * arr.get(k) * arr.get(j)) + MCMRecursive.solve(arr, i, k) + MCMRecursive.solve(arr, k + 1, j);
            minValue = Math.min(minValue, cost);
        }
        return minValue;
    }

    public static Integer getMinCostForMultiplication(List<Integer> dimensions) {
        int n = dimensions.size();
        return MCMRecursive.solve(dimensions, 1, n - 1);
    }
}

class MCMMemoized {
    /**
     * Time complexity is O(n^3) and space complexity is O(n + n^2).
     */

    private static Integer solve(List<Integer> arr, Integer i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i.equals(j)) {
            return 0;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        int minValue = Integer.MAX_VALUE;
        for (int k = i; k < j; k += 1) {
            int cost = (arr.get(i - 1) * arr.get(k) * arr.get(j)) + MCMMemoized.solve(arr, i, k, dp) + MCMMemoized.solve(arr, k + 1, j, dp);
            minValue = Math.min(minValue, cost);
        }
        Map<Integer, Integer> v = dp.get(i);
        v.put(j, minValue);
        dp.put(i, v);
        return dp.get(i).get(j);
    }

    public static Integer getMinCostForMultiplication(List<Integer> dimensions) {
        int n = dimensions.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> v = new HashMap<>();
            for (int j = 1; j < n; j += 1) {
                v.put(j, null);
            }
            dp.put(i, v);
        }
        return MCMMemoized.solve(dimensions, 1, n - 1, dp);
    }
}

class MCMTabulation {
    /**
     * Time complexity is O(n^3) and space complexity is O(n^2).
     */

    public static Integer getMinCostForMultiplication(List<Integer> dimensions) {
        int n = dimensions.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> v = new HashMap<>();
            for (int j = 1; j < n; j += 1) {
                v.put(j, 0);
            }
            dp.put(i, v);
        }
        for (int i = n - 1; i >= 1; i -= 1) {
            for (int j = 1; j <= n - 1; j += 1) {
                if (i >= j) {
                    continue;
                }
                int minValue = Integer.MAX_VALUE;
                for (int k = i; k < j; k += 1) {
                    int cost = (dimensions.get(i - 1) * dimensions.get(k) * dimensions.get(j)) + dp.get(i).get(k) + dp.get(k + 1).get(j);
                    minValue = Math.min(minValue, cost);
                }
                Map<Integer, Integer> v = dp.get(i);
                v.put(j, minValue);
                dp.put(i, v);
            }
        }
        return dp.get(1).get(n - 1);
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40, 50)));
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40)));
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(4, 5, 3, 2)));
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(10, 15, 20, 25)));
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(1, 4, 3, 2)));
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(2, 1, 3, 4)));
        System.out.println(MCMRecursive.getMinCostForMultiplication(Arrays.asList(1, 2, 3, 4, 3)));

        System.out.println("Memoized Solution");
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40, 50)));
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40)));
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(4, 5, 3, 2)));
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(10, 15, 20, 25)));
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(1, 4, 3, 2)));
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(2, 1, 3, 4)));
        System.out.println(MCMMemoized.getMinCostForMultiplication(Arrays.asList(1, 2, 3, 4, 3)));

        System.out.println("Tabulation Solution");
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40, 50)));
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40)));
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(4, 5, 3, 2)));
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(10, 15, 20, 25)));
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(1, 4, 3, 2)));
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(2, 1, 3, 4)));
        System.out.println(MCMTabulation.getMinCostForMultiplication(Arrays.asList(1, 2, 3, 4, 3)));
    }
}