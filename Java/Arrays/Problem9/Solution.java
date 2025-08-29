package Arrays.Problem9;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer minimizeHeights(List<Integer> arr, Integer k) {
        if (k <= 0) return null;
        QuickSort.sort(arr);
        Integer ans = arr.getLast() - arr.getFirst();
        Integer smallest = arr.getFirst() + k, largest = arr.getLast() - k;
        Integer mi = 0, mx = 0;
        for (int i = 0; i < arr.size() - 1; i += 1) {
            mi = Math.min(smallest, arr.get(i + 1) - k);
            mx = Math.max(largest, arr.get(i) + k);
            if (mi < 0) continue;
            ans = Math.min(ans, mx - mi);
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(minimizeHeights(Arrays.asList(1, 5, 8, 10), 2));
        System.out.println(minimizeHeights(Arrays.asList(3, 9, 12, 16, 20), 3));
    }
}
