package BinarySearch.BS21;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(Solution1.getMedian(Arrays.asList(1, 3, 4, 7, 10, 12), Arrays.asList(2, 3, 6, 15)));
        System.out.println(Solution1.getMedian(Arrays.asList(2, 3, 4), Arrays.asList(1, 3)));
        System.out.println(Solution1.getMedian(Arrays.asList(-5, 3, 6, 12, 15), Arrays.asList(-12, -10, -6, -3, 4, 10)));
        System.out.println(Solution1.getMedian(Arrays.asList(1, 12, 15, 26, 38), Arrays.asList(2, 13, 17, 30, 45, 60)));
        System.out.println(Solution1.getMedian(Arrays.asList(), Arrays.asList(2, 4, 5, 6)));
        System.out.println(Solution1.getMedian(Arrays.asList(1, 3), Arrays.asList(2)));
        System.out.println(Solution1.getMedian(Arrays.asList(1, 2), Arrays.asList(3, 4)));
        System.out.println(Solution1.getMedian(Arrays.asList(2, 4, 6), Arrays.asList(1, 3, 5)));
    }
}
