package SearchingAndSorting.Problem13;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getTriplets(Arrays.asList(-2, 0, 1, 3), 2));
        System.out.println(getTriplets(Arrays.asList(5, 1, 3, 4, 7), 12));
    }

    public static List<List<Integer>> getTriplets(List<Integer> arr, int sum) {
        QuickSort.sort(arr);
        int i = 0, n = arr.size();
        List<List<Integer>> result = new ArrayList<>();
        while (i < n - 2) {
            int j = i + 1, k = n - 1;
            while (j < k) {
                int _sum = arr.get(i) + arr.get(j) + arr.get(k);
                if (_sum < sum) {
                    result.add(List.of(arr.get(i), arr.get(j), arr.get(k)));
                }
                k -= 1;
                if (j >= k) {
                    j += 1;
                    k = n - 1;
                }
            }
            i += 1;
        }
        return result;
    }
}
