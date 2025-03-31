package BinarySearch;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class NaiveSolution {
    private static List<Integer> getMergedArray(List<Integer> a, List<Integer> b) {
        List<Integer> mergedArray = new ArrayList<>();
        int i = 0, j = 0;
        while (i < a.size() && j < b.size()) {
            if (a.get(i) <= b.get(j)) {
                mergedArray.add(a.get(i));
                i += 1;
            } else {
                mergedArray.add(b.get(j));
                j += 1;
            }
        }
        while (i < a.size()) {
            mergedArray.add(a.get(i));
            i += 1;
        }
        while (j < b.size()) {
            mergedArray.add(b.get(j));
            j += 1;
        }
        return mergedArray;
    }

    public static Double getMedian(List<Integer> a, List<Integer> b) {
        /**
         * Time complexity is O(n) and space complexity is O(n).
         */

        // This will take O(n) time and O(n) space.
        List<Integer> mergedArray = getMergedArray(a, b);
        int n = mergedArray.size();
        if (n % 2 == 1) {
            return (double) mergedArray.get(n/2);
        }
        return (mergedArray.get(n/2 - 1) + mergedArray.get(n/2))/2.0;
    }
}


class Main {
    public static void main(String[] args) {
        System.out.println(NaiveSolution.getMedian(Arrays.asList(-5, 3, 6, 12, 15), Arrays.asList(-12, -10, -6, -3, 4, 10)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(1, 12, 15, 26, 38), Arrays.asList(2, 13, 17, 30, 45, 60)));
        System.out.println(NaiveSolution.getMedian(List.of(), Arrays.asList(2, 4, 5, 6)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(2, 3, 5, 8), Arrays.asList(10, 12, 14, 16, 18, 20)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(1, 3), List.of(2)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(1, 2), Arrays.asList(3, 4)));
    }
}