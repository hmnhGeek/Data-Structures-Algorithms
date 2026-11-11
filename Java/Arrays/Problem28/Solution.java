// Problem link - https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1
// Solution - https://www.youtube.com/watch?v=DhFh8Kw7ymk


package Arrays.Problem28;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getTriplets(Arrays.asList(1, 4, 45, 6, 10, 8), 13));
        System.out.println(getTriplets(Arrays.asList(1, 2, 4, 3, 6, 7), 10));
        System.out.println(getTriplets(Arrays.asList(40, 20, 10, 3, 6, 7), 24));
        System.out.println(getTriplets(Arrays.asList(-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2), 0));
    }

    public static List<List<Integer>> getTriplets(List<Integer> arr, Integer target) {
        /*
            Time complexity is O(n*log(n) + n^2) and space complexity is O(1).
         */
        QuickSort.sort(arr);
        int i = 0, n = arr.size();
        List<List<Integer>> result = new ArrayList<>();
        while (i <= n - 3) {
            while (i > 0 && i <= n - 3 && Objects.equals(arr.get(i), arr.get(i - 1))) {
                i += 1;
            }
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = arr.get(i) + arr.get(j) + arr.get(k);
                if (sum > target) {
                    k -= 1;
                } else if (sum == target) {
                    result.add(List.of(arr.get(i), arr.get(j), arr.get(k)));
                    j += 1;
                    k -= 1;
                    while (j < k && Objects.equals(arr.get(j), arr.get(j - 1))) {
                        j += 1;
                    }
                    while (j < k && Objects.equals(arr.get(k), arr.get(k + 1))) {
                        k -= 1;
                    }
                } else {
                    k -= 1;
                }
            }
            i += 1;
        }
        return result;
    }
}
