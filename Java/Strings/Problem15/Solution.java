// Problem link - https://leetcode.com/problems/next-permutation/description/
// Solution - https://www.youtube.com/watch?v=JDOXKqF60RQ&t=976s


package Strings.Problem15;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static List<Integer> getNextPermutation(List<Integer> list) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        List<Integer> arr = new ArrayList<>(list);
        int n = arr.size();
        arr.addFirst(Integer.MIN_VALUE);
        int breakpointIndex = getBreakpointIndex(n, arr);
        if (breakpointIndex == 1) {
            arr.removeFirst();
            return arr.reversed();
        }
        Integer breakpointElement = arr.get(breakpointIndex - 1);
        int swapToIndex = getSwapWithIndex(arr, breakpointElement, breakpointIndex, n);
        Collections.swap(arr, breakpointIndex - 1, swapToIndex);
        reversePart(arr, breakpointIndex, n);
        arr.removeFirst();
        return arr;
    }

    private static void reversePart(List<Integer> arr, int breakpointIndex, int n) {
        int i = breakpointIndex, j = n;
        while (i < j) {
            Collections.swap(arr, i, j);
            i += 1;
            j -= 1;
        }
    }

    private static int getSwapWithIndex(List<Integer> arr, Integer breakpointElement, Integer breakpointIndex, int n) {
        for (int i = n; i >= breakpointIndex; i -= 1) {
            if (arr.get(i) > breakpointElement) {
                return i;
            }
        }
        return -1;
    }

    private static int getBreakpointIndex(int n, List<Integer> arr) {
        for (int i = n; i >= 1; i -= 1) {
            if (arr.get(i - 1) < arr.get(i)) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(Solution.getNextPermutation(Arrays.asList(1, 2, 3)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(1, 1, 5)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(3, 2, 1)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(2, 4, 1, 7, 5, 0)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(3, 4, 2, 5, 1)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(2, 3, 1, 5, 4)));
    }
}
