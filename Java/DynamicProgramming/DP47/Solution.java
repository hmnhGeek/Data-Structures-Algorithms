package DynamicProgramming.DP47;

import java.util.*;

public class Solution {
    public static Integer getLISCount(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.putIfAbsent(i, 1);
            count.putIfAbsent(i, 1);
        }
        for (int i = 0; i < n; i += 1) {
            for (int prev = 0; prev < i; prev += 1) {
                if (arr.get(prev) < arr.get(i) && 1 + dp.get(prev) > dp.get(i)) {
                    dp.put(i, 1 + dp.get(prev));
                    count.put(i, count.get(prev));
                } else if (arr.get(prev) < arr.get(i) && 1 + dp.get(prev) == dp.get(i)) {
                    count.put(i, count.get(i) + count.get(prev));
                }
            }
        }
        Integer lisLength = Collections.max(dp.values());
        int countOfLis = 0;
        for (Integer i : dp.keySet()) {
            if (Objects.equals(dp.get(i), lisLength)) {
                countOfLis += count.get(i)  ;
            }
        }
        return countOfLis;
    }

    public static void main(String[] args) {
        System.out.println(getLISCount(List.of(1, 3, 5, 4, 7)));
        System.out.println(getLISCount(List.of(50, 3, 90, 60, 80)));
        System.out.println(getLISCount(List.of(3, 7, 4, 6)));
        System.out.println(getLISCount(List.of(5, 7, 2, 3)));
        System.out.println(getLISCount(List.of(2, 2, 2, 2, 2)));
        System.out.println(getLISCount(List.of(1, 5, 4, 3, 2, 6, 7, 10, 8, 9)));
    }
}
