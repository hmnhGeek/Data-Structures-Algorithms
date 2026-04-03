package Arrays.Problem18;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getPairs(Arrays.asList(-1, 0, 1, 2, -1, -4), 0));
        System.out.println(getPairs(Arrays.asList(6, 1, 8, 0, 4, -9, -1, -10, -6, -5), 0));
    }

    public static List<List<Integer>> getPairs(List<Integer> arr, Integer target) {
        int i = 0, j = arr.size() - 1;
        QuickSort.sort(arr);
        List<List<Integer>> pairs = new ArrayList<>();
        while (i < j) {
            Integer sum = arr.get(i) + arr.get(j);
            if (sum == target) {
                pairs.add(List.of(arr.get(i), arr.get(j)));
                i += 1;
                j -= 1;
            } else if (sum > target) {
                j -= 1;
            } else {
                i += 1;
            }
        }
        return pairs;
    }
}
