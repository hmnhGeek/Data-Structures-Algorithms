package SearchingAndSorting.Problem1;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getLeftmostOccurrence(Arrays.asList(1, 3, 5, 5, 5, 5, 67, 123, 125), 5));

    }

    private static int getLeftmostOccurrence(List<Integer> arr, Integer x) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) >= x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
