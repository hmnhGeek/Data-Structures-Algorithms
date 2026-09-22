// Problem link - https://www.naukri.com/code360/problems/printing-longest-increasing-subsequence_8360670
// Solution - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43


package DynamicProgramming.DP42;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static List<Integer> getLIS(List<Integer> arr) {
        /*
            Time complexity is O(n^2) and space complexity is O(2n).
         */
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            dp.put(i, 1);
        }
        Map<Integer, Integer> parents = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            parents.put(i, i);
        }
        for (int i = 0; i < arr.size(); i += 1) {
            for (int prev = 0; prev < i; prev += 1) {
                if (arr.get(prev) < arr.get(i) && dp.get(i) < 1 + dp.get(prev)) {
                    dp.put(i, 1 + dp.get(prev));
                    parents.put(i, prev);
                }
            }
        }
        int idxOfLis = getIdxOfLis(dp);
        List<Integer> result = new ArrayList<>();
        int start = idxOfLis;
        while (parents.get(start) != start) {
            result.add(arr.get(start));
            start = parents.get(start);
        }
        result.add(arr.get(start));
        List<Integer> lis = result.reversed();
        return lis;
    }

    private static Integer getIdxOfLis(Map<Integer, Integer> dp) {
        int maxVal = Integer.MIN_VALUE;
        Integer idx = null;
        for (Integer i : dp.keySet()) {
            if (dp.get(i) > maxVal) {
                maxVal = dp.get(i);
                idx = i;
            }
        }
        return idx;
    }

    public static void main(String[] args) {
        System.out.println(getLIS(List.of(5, 4, 11, 1, 16, 8)));
        System.out.println(getLIS(List.of(1, 2, 2)));
        System.out.println(getLIS(List.of(10, 20, 3, 40)));
        System.out.println(getLIS(List.of(10, 22, 9, 33, 21, 50, 41, 60, 80)));
        System.out.println(getLIS(List.of(0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15)));
        System.out.println(getLIS(List.of(1)));
        System.out.println(getLIS(List.of(5, 6, 3, 4, 7, 6)));
        System.out.println(getLIS(List.of(1, 2, 3, 4, 5)));
    }
}
