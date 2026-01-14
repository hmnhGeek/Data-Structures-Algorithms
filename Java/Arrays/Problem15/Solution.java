package Arrays.Problem15;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(Solution.getNextPermutation(Arrays.asList(1, 2, 3)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(1, 1, 5)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(3, 2, 1)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(2, 4, 1, 7, 5, 0)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(3, 4, 2, 5, 1)));
        System.out.println(Solution.getNextPermutation(Arrays.asList(2, 3, 1, 5, 4)));
    }

    public static List<Integer> getNextPermutation(List<Integer> arr) {
        int n = arr.size();
        int breakpointIndex = getBreakpointIndex(arr, n);
        if (breakpointIndex == -1) {
            return arr.reversed();
        }
        Integer justGreaterElementIdx = getJustGreaterElemIdx(arr, breakpointIndex);
        Collections.swap(arr, justGreaterElementIdx, breakpointIndex);
        reversePart(arr, breakpointIndex + 1);
        return arr;
    }

    private static void reversePart(List<Integer> arr, int i) {
        int j = arr.size() - 1;
        while (i < j) {
            Collections.swap(arr, i, j);
            i += 1;
            j -= 1;
        }
    }

    private static Integer getJustGreaterElemIdx(List<Integer> arr, int breakpointIndex) {
        for (int i = arr.size() - 1; i > breakpointIndex; i -= 1) {
            if (arr.get(i) > arr.get(breakpointIndex)) {
                return i;
            }
        }
        return -1;
    }

    private static int getBreakpointIndex(List<Integer> arr, int n) {
        int result = -1;
        for (int i = n - 2; i >= 0; i -= 1) {
            if (arr.get(i) < arr.get(i + 1)) {
                result = i;
                break;
            }
        }
        return result;
    }
}
