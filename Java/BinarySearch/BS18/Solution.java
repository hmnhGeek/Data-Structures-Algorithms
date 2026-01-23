// Problem link - https://www.naukri.com/code360/problems/allocate-books_1090540
// Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


package BinarySearch.BS18;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(allocateBooks(Arrays.asList(25, 46, 28, 49, 24), 4));
        System.out.println(allocateBooks(Arrays.asList(12, 34, 67, 90), 2));
        System.out.println(allocateBooks(Arrays.asList(15, 17, 20), 2));
        System.out.println(allocateBooks(Arrays.asList(22, 23, 67), 1));
        System.out.println(allocateBooks(Arrays.asList(15, 17, 20), 5));

    }

    public static Integer allocateBooks(List<Integer> pages, Integer numStudents) {
        /*
            Time complexity is O(n*log(sum - max)) and space complexity is O(1).
         */
        if (numStudents > pages.size()) return -1;
        int n = pages.size();
        int low = Collections.max(pages);
        int high = pages.stream().mapToInt(Integer::intValue).sum();
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int allocatedStudents = Solution.getCountOfStudentsAllocated(pages, mid);
            if (allocatedStudents > numStudents) {
                low = mid + 1;
            } else if (allocatedStudents < numStudents) {
                high = mid - 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private static int getCountOfStudentsAllocated(List<Integer> pages, int mid) {
        int allocatedStudents = 0;
        int allocatedPages = 0;
        for (int i = 0; i < pages.size(); i += 1) {
            allocatedPages += pages.get(i);
            if (allocatedPages > mid) {
                allocatedPages = pages.get(i);
                allocatedStudents += 1;
            }
        }
        if (allocatedPages != 0) {
            allocatedStudents += 1;
        }
        return allocatedStudents;
    }
}
