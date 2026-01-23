// Problem link - https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557
// Solution - https://www.youtube.com/watch?v=thUd_WJn6wk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=20


package BinarySearch.BS19;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getPaintersPartition(Arrays.asList(2, 1, 5, 6, 2, 3), 2));
        System.out.println(getPaintersPartition(Arrays.asList(10, 20, 30, 40), 2));
        System.out.println(getPaintersPartition(Arrays.asList(48, 90), 2));
        System.out.println(getPaintersPartition(Arrays.asList(5, 10, 30, 20, 15), 2));
        System.out.println(getPaintersPartition(Arrays.asList(5, 5, 5, 5), 2));

    }

    public static Integer getPaintersPartition(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
         */
        if (k > arr.size()) return -1;
        int low = Collections.max(arr);
        int high = arr.stream().mapToInt(Integer::intValue).sum();
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int paintersUsed = Solution.getPaintersCount(arr, mid);
            if (paintersUsed <= k) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static int getPaintersCount(List<Integer> arr, int mid) {
        int allocatedPainters = 0;
        int areaCovered = 0;
        for (Integer integer : arr) {
            areaCovered += integer;
            if (areaCovered > mid) {
                areaCovered = integer;
                allocatedPainters += 1;
            }
        }
        if (areaCovered != 0) {
            allocatedPainters += 1;
        }
        return allocatedPainters;
    }
}
