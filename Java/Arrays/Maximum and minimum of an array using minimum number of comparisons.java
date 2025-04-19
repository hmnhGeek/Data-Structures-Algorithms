// Problem link - https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

package Arrays;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution2 {
    public static Map<String, Integer> getMaxMin(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */

        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int i = 0; i < arr.size(); i += 1) {
            min = Math.min(min, arr.get(i));
            max = Math.max(max, arr.get(i));
        }
        Map<String, Integer> map = new HashMap<>();
        map.put("min", min);
        map.put("max", max);
        return map;
    }

    public static void main(String[] args) {
        System.out.println(Solution2.getMaxMin(Arrays.asList(3, 5, 4, 1, 9)));
        System.out.println(Solution2.getMaxMin(Arrays.asList(22, 14, 8, 17, 35, 3)));
        System.out.println(Solution2.getMaxMin(Arrays.asList(2, 1, 4, 6, 8, 8, 6)));
    }
}