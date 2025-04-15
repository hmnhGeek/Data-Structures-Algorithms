// Problem link - https://www.naukri.com/code360/problems/k-th-element-of-2-sorted-array_1164159
// Solution - https://www.youtube.com/watch?v=D1oDwWCq50g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=24


package BinarySearch;


import java.util.Arrays;
import java.util.List;

class SolutionBS22 {
    private static Integer getKthElement(List<Integer> arr1, List<Integer> arr2, Integer k) {
        /*
            Time complexity is O(log(min(a1, a2))) and space complexity is O(1).
         */

        int n1 = arr1.size(), n2 = arr2.size();
        if (n1 > n2) {
            return getKthElement(arr2, arr1, k);
        }

        // if k < n1, do we need to pick all from arr1? No, we can therefore make high = min(k, n1).
        int high = Math.min(k, n1);

        // if k > n2, then even if we pick all elements from arr2, we would still need elements from arr1. How many from
        // arr1? k - n2. But what if k < n2? In that case we can pick all elements from arr2 and 0 from arr1. Hence, low
        // will be max(k - n2, 0).
        int low = Math.max(k - n2, 0);
        while (low <= high) {
            int mid1 = low + (high - low)/2;
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
                return Math.max(l1, l2);
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(SolutionBS22.getKthElement(Arrays.asList(2, 3, 6, 7, 9), Arrays.asList(1, 4, 8, 10), 4));
        System.out.println(SolutionBS22.getKthElement(Arrays.asList(2, 3, 45), Arrays.asList(4, 6, 7, 8), 4));
        System.out.println(SolutionBS22.getKthElement(Arrays.asList(1, 2, 3, 5, 6), Arrays.asList(4, 7, 8, 9, 100), 6));
        System.out.println(SolutionBS22.getKthElement(Arrays.asList(100, 112, 256, 349, 770), Arrays.asList(72, 86, 113, 119, 265, 445, 892), 7));
    }
}