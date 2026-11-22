package PracticeSet1.BinarySearch.BS18;

import java.util.Arrays;
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
        if (numStudents <= 0 || pages.size() < numStudents) return null;
        int low = 0, high = pages.stream().mapToInt(Integer::intValue).sum();
        while (low <= high) {
            int mid = (low + (high - low)/2);
            Integer numStudentsAllocated = getAllocatedNumbers(pages, mid);
            if (numStudentsAllocated <= numStudents) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static Integer getAllocatedNumbers(List<Integer> pages, int mid) {
        int allocatedStudents = 0;
        int n = pages.size();
        int pagesUsed = 0;
        int i = 0;
        while (i < n) {
            pagesUsed += pages.get(i);
            if (pagesUsed > mid) {
                allocatedStudents += 1;
                pagesUsed = pages.get(i);
            }
            i += 1;
        }
        if (pagesUsed > 0) {
            allocatedStudents += 1;
            pagesUsed = 0;
        }
        return allocatedStudents;
    }
}
