package DynamicProgramming;


import java.util.*;


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

class MemoizedDP51 {
    /**
     * Time complexity is O(n^3) and space complexity is O(n + n^2).
     */
    private static Integer solve(List<Integer> arr, Integer i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i > j) {
            return 0;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer maxCoins = Integer.MIN_VALUE;
        for (int index = i; index <= j; index += 1) {
            Integer coins = arr.get(i - 1) * arr.get(index) * arr.get(j + 1) + solve(arr, i, index - 1, dp) + solve(arr, index + 1, j, dp);
            maxCoins = Math.max(coins, maxCoins);
        }
        Map<Integer, Integer> mp = dp.get(i);
        mp.put(j, maxCoins);
        dp.put(i, mp);
        return dp.get(i).get(j);
    }

    public static Integer getMaximumCoins(List<Integer> balloons) {
        int n = balloons.size();
        List<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.addAll(balloons);
        arr.add(1);

        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 1; i <= n; i += 1) {
            Map<Integer, Integer> submap = new HashMap<>();
            for (int j = 1; j <= n; j += 1) {
                submap.put(j, null);
            }
            dp.put(i, submap);
        }

        return solve(arr, 1, n, dp);
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

class TabulationDP51 {
    /**
     * Time complexity is O(n^3) and space complexity is O(n^2).
     */
    public static Integer getMaximumCoins(List<Integer> balloons) {
        int n = balloons.size();
        List<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.addAll(balloons);
        arr.add(1);

        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n + 1; i += 1) {
            Map<Integer, Integer> submap = new HashMap<>();
            for (int j = 0; j <= n + 1; j += 1) {
                if (i > j) {
                    submap.put(j, 0);
                } else {
                    submap.put(j, Integer.MIN_VALUE);
                }
            }
            dp.put(i, submap);
        }

        for (int i = n; i >= 1; i -= 1) {
            for (int j = 1; j <= n; j += 1) {
                if (i > j) {
                    continue;
                }
                Integer maxCoins = Integer.MIN_VALUE;
                for (int index = i; index <= j; index += 1) {
                    Integer coins = arr.get(i - 1) * arr.get(index) * arr.get(j + 1) + dp.get(i).get(index - 1) + dp.get(index + 1).get(j);
                    maxCoins = Math.max(coins, maxCoins);
                }
                Map<Integer, Integer> mp = dp.get(i);
                mp.put(j, maxCoins);
                dp.put(i, mp);
            }
        }

        return dp.get(1).get(n);
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