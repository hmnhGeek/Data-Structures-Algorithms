// Problem link - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
// Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19

package SearchingAndSorting.Problem30;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    private static int getPages(List<Integer> pages, int mid) {
        Integer numStudents = 0;
        Integer pagesSum = 0;
        for (int i = 0; i < pages.size(); i += 1) {
            if (pagesSum + pages.get(i) <= mid) {
                pagesSum += pages.get(i);
            } else {
                numStudents += 1;
                pagesSum = pages.get(i);
            }
        }
        if (pagesSum > 0) numStudents += 1;
        return numStudents;
    }

    public static Integer allocateBooks(List<Integer> pages, Integer numStudents) {
        /*
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
         */

        // if k is <= 0 or number of students is more than the number of books, return -1.
        if (numStudents <= 0 || numStudents > pages.size()) return -1;
        int low = Collections.max(pages), high = pages.stream().mapToInt(Integer::intValue).sum();
        while (low <= high) {
            int mid = (low + (high - low)/2);

            // check if allocation to all k students is possible if each student gets at max mid-number of pages.
            int numStudentsAcquired = getPages(pages, mid);
            if (numStudentsAcquired == numStudents) {
                high = mid - 1;
            } else if (numStudentsAcquired > numStudents) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    public static void main(String[] args) {
        System.out.println(allocateBooks(Arrays.asList(12, 34, 67, 90), 2));
        System.out.println(allocateBooks(Arrays.asList(15, 17, 20), 5));
        System.out.println(allocateBooks(Arrays.asList(22, 23, 67), 1));
        System.out.println(allocateBooks(Arrays.asList(25, 46, 28, 49, 24), 4));
        System.out.println(allocateBooks(Arrays.asList(15, 17, 20), 2));
    }
}
