// Problem link - https://www.geeksforgeeks.org/dsa/merge-two-sorted-arrays-o1-extra-space/#better-approach-1-using-nth-smallest-in-the-two-sorted-on-logn-m-logm-time-and-o1-space
// Solution - https://www.youtube.com/watch?v=n7uwj04E0I4


package Arrays.Problem12;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static void swapIfGreater(List<Integer> a, List<Integer> b, int i, int j) {
        if (a.get(i) > b.get(j)) {
            Integer temp = b.get(j);
            b.set(j, a.get(i));
            a.set(i, temp);
        }
    }

    public static void merge(List<Integer> a, List<Integer> b) {
        /*
            Time complexity is O({n + m} * log(n + m)) and space complexity is O(1).
         */
        int n = a.size(), m = b.size();
        int totalLength = n + m;
        int gap = (totalLength / 2) + (totalLength % 2);
        while (gap > 0) {
            int left = 0;
            int right = left + gap;
            while (right < totalLength) {
                if (left < n && right >= n) {
                    // left is on a and right is on b.
                    swapIfGreater(a, b, left, right - n);
                } else if (left >= n) {
                    // left and right both are on b.
                    swapIfGreater(b, b, left - n, right - n);
                } else {
                    // left and right both are on a.
                    swapIfGreater(a, a, left, right);
                }
                left += 1;
                right += 1;
            }
            if (gap == 1) break;
            gap = (gap / 2) + (gap % 2);
        }
    }

    private static void test(List<Integer> a, List<Integer> b) {
        System.out.println("Previously");
        System.out.println(a);
        System.out.println(b);
        merge(a, b);
        System.out.println("Now");
        System.out.println(a);
        System.out.println(b);
        System.out.println();
    }

    public static void main(String[] args) {
        test(
                Arrays.asList(2, 4, 7, 10),
                Arrays.asList(2, 3)
        );
        test(
                Arrays.asList(1, 5, 9, 10, 15, 20),
                Arrays.asList(2, 3, 8, 13)
        );
        test(
                Arrays.asList(0, 1),
                Arrays.asList(2, 3)
        );
    }
}
