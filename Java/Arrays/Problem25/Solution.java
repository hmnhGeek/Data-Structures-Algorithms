package Arrays.Problem25;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Integer countFrequentElement(List<Integer> arr, Integer k) {
        int n = arr.size();
        int threshold = n / k;
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer i : arr) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        int count = 0;
        for (Integer i : map.keySet()) {
            if (map.get(i) > threshold) {
                count += 1;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countFrequentElement(Arrays.asList(3, 4, 2, 2, 1, 2, 3, 3), 4));
        System.out.println(countFrequentElement(Arrays.asList(9, 10, 7, 9, 2, 9, 10), 3));
    }
}
