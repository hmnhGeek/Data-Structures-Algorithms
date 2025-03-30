package Arrays;

import java.util.Arrays;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        System.out.println(getMedian(Arrays.asList(-5, 3, 6, 12, 15), Arrays.asList(-12, -10, -6, -3, 4, 10)));
        System.out.println(getMedian(Arrays.asList(1, 12, 15, 26, 38), Arrays.asList(2, 13, 17, 30, 45, 60)));
        System.out.println(getMedian(List.of(), Arrays.asList(2, 4, 5, 6)));
        System.out.println(getMedian(Arrays.asList(2, 3, 5, 8), Arrays.asList(10, 12, 14, 16, 18, 20)));
        System.out.println(getMedian(Arrays.asList(1, 3), List.of(2)));
        System.out.println(getMedian(Arrays.asList(1, 2), Arrays.asList(3, 4)));
    }

    private static Double getMedian(List<Integer> arr1, List<Integer> arr2) {
        int n1 = arr1.size();
        int n2 = arr2.size();

        // we will run the while loop of the binary search on the smaller array to avoid TLE.
        if(n1 > n2) {
            return getMedian(arr2, arr1);
        }

        // medianIndex denotes the number of elements on the left of the median. In both even and odd cases,
        // we want consistent medianIndex, and hence (n + 1)//2.
        int n = n1 + n2;
        int medianIndex = (n + 1)/2;

        // define the search space
        int low = 0;
        int high = n1;

        while (low <= high) {
            // mid1 denotes the index from arr1 which falls in the right section of the median
            int mid1 = low + (high - low)/2;
            // mid2 denotes the index from arr2 which falls in the right section of the median.
            int mid2 = medianIndex - mid1;

            // compute l1, l2, r1 and r2.
            int l1 = 0 <= mid1 - 1 && mid1 - 1 < n1 ? arr1.get(mid1 - 1) : Integer.MIN_VALUE;
            int l2 = 0 <= mid2 - 1 && mid2 - 1 < n2 ? arr2.get(mid2 - 1) : Integer.MIN_VALUE;
            int r1 = 0 <= mid1 && mid1 < n1 ? arr1.get(mid1) : Integer.MAX_VALUE;
            int r2 = 0 <= mid2 && mid2 < n2 ? arr2.get(mid2) : Integer.MAX_VALUE;

            // if median condition is satisfied, return the median.
            if (l1 > r2) {
                high = mid1 - 1;
            } else if (l2 > r1) {
                low = mid1 + 1;
            } else {
                if (n % 2 == 0) {
                    return ((Math.max(l1, l2) + Math.min(r1, r2))/2.0);
                }
                return (double) Math.max(l1, l2);
            }
        }

        // this shall never execute
        return (double) -1;
    }
}