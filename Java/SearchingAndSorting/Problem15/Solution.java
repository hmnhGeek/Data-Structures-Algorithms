package SearchingAndSorting.Problem15;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static Integer countSumSubArrays(List<Integer> arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int sum = 0, count = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            sum += arr.get(i);
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
                map.put(sum - k, map.get(sum - k) + 1);
            } else {
                map.put(sum - k, 1);
            }
        }
        return count;
    }

    public static Integer getZeroSumSubArrays(List<Integer> arr) {
        return countSumSubArrays(arr, 0);
    }

    public static void main(String[] args) {
        System.out.println(getZeroSumSubArrays(Arrays.asList(0, 0, 5, 5, 0, 0)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(6, -1, -3, 4, -2, 2, 4, 6, -12, -7)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(0)));
    }
}
