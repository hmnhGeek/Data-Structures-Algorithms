// Problem link - https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
// Solution - https://www.youtube.com/watch?v=n7uwj04E0I4


package SearchingAndSorting.Problem14;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void mergeSortedArrays(List<Integer> a, List<Integer> b) {
        /*
            Time complexity is O(min(n, m) + nlog(n) + mlog(m)) and space complexity is O(1).
         */
        int n = a.size(), m = b.size();
        int i = n - 1, j = 0;
        while (i >= 0 && j < m) {
            if (a.get(i) > b.get(j)) {
                Integer temp = b.get(j);
                b.set(j, a.get(i));
                a.set(i, temp);
                i -= 1;
                j += 1;
            } else {
                break;
            }
        }
        QuickSort.sort(a);
        QuickSort.sort(b);
        System.out.println(a);
        System.out.println(b);
        System.out.println();
    }

    public static void main(String[] args) {
        mergeSortedArrays(Arrays.asList(2, 4, 7, 10), Arrays.asList(2, 3));
        mergeSortedArrays(Arrays.asList(1, 5, 9, 10, 15, 20), Arrays.asList(2, 3, 8, 13));
        mergeSortedArrays(Arrays.asList(0, 1), Arrays.asList(2, 3));
    }
}
