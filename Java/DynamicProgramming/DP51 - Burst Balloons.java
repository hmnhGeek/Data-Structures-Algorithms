package DynamicProgramming;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class RecursiveDP51 {
    /**
     * Time complexity is exponential and space complexity is O(n).
     */
    private static Integer solve(List<Integer> arr, Integer i, Integer j) {
        if (i > j) {
            return 0;
        }
        Integer maxCoins = Integer.MIN_VALUE;
        for (int index = i; index <= j; index += 1) {
            Integer coins = arr.get(i - 1) * arr.get(index) * arr.get(j + 1) + solve(arr, i, index - 1) + solve(arr, index + 1, j);
            maxCoins = Math.max(coins, maxCoins);
        }
        return maxCoins;
    }

    public static Integer getMaximumCoins(List<Integer> balloons) {
        int n = balloons.size();
        List<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.addAll(balloons);
        arr.add(1);
        return solve(arr, 1, n);
    }

    public static void main(String[] args) {
        System.out.println(getMaximumCoins(Arrays.asList(3, 1, 5, 8)));
        System.out.println(getMaximumCoins(Arrays.asList(7, 1, 8)));
        System.out.println(getMaximumCoins(Arrays.asList(9, 1)));
        System.out.println(getMaximumCoins(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(getMaximumCoins(Arrays.asList(1, 5, 2, 8)));
        System.out.println(getMaximumCoins(Arrays.asList(5, 10)));
        System.out.println(getMaximumCoins(Arrays.asList(1, 5)));
    }
}