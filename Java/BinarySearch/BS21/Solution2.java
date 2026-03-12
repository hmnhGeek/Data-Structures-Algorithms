package BinarySearch.BS21;

import java.util.Arrays;
import java.util.List;

public class Solution2 {
    public static Double getMedian(List<Integer> arr1, List<Integer> arr2) {
        if (arr2.size() < arr1.size()) return getMedian(arr2, arr1);
        int low = 0, high = arr1.size();
        int n1 = arr1.size(), n2 = arr2.size();
        int k = (arr1.size() + arr2.size() + 1)/2;
        while (low <= high) {
            int mid1 = (low + high)/2;
            int mid2 = k - mid1;
            int l1 = 0 <= mid1 - 1 && mid1 - 1 < n1 ? arr1.get(mid1 - 1) : Integer.MIN_VALUE;
            int l2 = 0 <= mid2 - 1 && mid2 - 1 < n2 ? arr2.get(mid2 - 1) : Integer.MIN_VALUE;
            int r1 = 0 <= mid1 && mid1 < n1 ? arr1.get(mid1) : Integer.MAX_VALUE;
            int r2 = 0 <= mid2 && mid2 < n2 ? arr2.get(mid2) : Integer.MAX_VALUE;
            if (l1 > r2) {
                high = mid1 - 1;
            } else if (l2 > r1) {
                low = mid1 + 1;
            } else {
                if ((n1 + n2) % 2 == 0) {
                    return (Math.max(l1, l2) + Math.min(r1, r2))/2.0;
                }
                return (double) Math.max(l1, l2);
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(Solution2.getMedian(Arrays.asList(1, 3, 4, 7, 10, 12), Arrays.asList(2, 3, 6, 15)));
        System.out.println(Solution2.getMedian(Arrays.asList(1, 3, 4), Arrays.asList(2, 6)));
        System.out.println(Solution2.getMedian(Arrays.asList(1, 3), Arrays.asList(2)));
        System.out.println(Solution2.getMedian(Arrays.asList(1, 2), Arrays.asList(3, 4)));
    }
}
