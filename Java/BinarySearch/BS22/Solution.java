// Problem link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
// Solution - https://www.youtube.com/watch?v=F9c7LpRZWVQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=23


package BinarySearch.BS22;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Double getMedian(List<Integer> arr1, List<Integer> arr2, Integer k) {
        /*
            Overall time complexity is O(log(n1)) and space complexity is O(1).
         */
        if (arr2.size() < arr1.size()) return getMedian(arr2, arr1, k);
        int n1 = arr1.size(), n2 = arr2.size();
        int low = Math.max(0, k - n2), high = Math.min(k, n1);
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
                return (double) Math.max(l1, l2);
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(Solution.getMedian(Arrays.asList(2, 3, 6, 7, 9), Arrays.asList(1, 4, 8, 10), 4));
        System.out.println(Solution.getMedian(Arrays.asList(2, 3, 45), Arrays.asList(4, 6, 7, 8), 4));
        System.out.println(Solution.getMedian(Arrays.asList(1, 2, 3, 5, 6), Arrays.asList(4, 7, 8, 9, 100), 6));
        System.out.println(Solution.getMedian(Arrays.asList(100, 112, 256, 349, 770), Arrays.asList(72, 86, 113, 119, 265, 445, 892), 7));
    }
}
