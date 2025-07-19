package BinarySearch.BS1;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Lower Bound");
        System.out.println(getLowerBound(Arrays.asList(3, 5, 8, 15, 19), 10));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3), 0));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3, 3, 5), 0));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3, 3, 5), 2));
        System.out.println(getLowerBound(Arrays.asList(1, 2, 2, 3, 3, 5), 7));
    }

    public static <T extends Comparable<T>> Integer getLowerBound(List<T> arr, T n) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid).compareTo(n) >= 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
