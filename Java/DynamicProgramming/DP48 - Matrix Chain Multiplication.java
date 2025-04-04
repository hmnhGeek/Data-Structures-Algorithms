package DynamicProgramming;

import java.util.Arrays;
import java.util.List;

class MCMRecursive {
    /**
     * Time complexity is exponential and space complexity is O(n).
     */

    private static Integer solve(List<Integer> arr, Integer i, Integer j) {
        if (i.equals(j)) {
            return 0;
        }
        Integer minValue = Integer.MAX_VALUE;
        for (int k = i; k < j; k += 1) {
            Integer cost = (arr.get(i - 1) * arr.get(k) * arr.get(j)) + MCMRecursive.solve(arr, i, k) + MCMRecursive.solve(arr, k + 1, j);
            minValue = Math.min(minValue, cost);
        }
        return minValue;
    }

    public static Integer getMinCostForMultiplication(List<Integer> dimensions) {
        int n = dimensions.size();
        return MCMRecursive.solve(dimensions, 1, n - 1);
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
    }
}