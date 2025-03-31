// Problem link - https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
// Solution - https://www.youtube.com/watch?v=C2rRzz-JDk8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=23

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

class BetterSolutionBS21 {
    private static Double computeMedian(Integer prevElement, List<Integer> a, List<Integer> b, Integer n, Integer i, Integer j) {
        // if the length of the merged array is odd, simply return the current element as the median.
        if (n % 2 == 1) {
            int x = i < a.size() ? a.get(i) : Integer.MAX_VALUE;
            int y = j < b.size() ? b.get(j) : Integer.MAX_VALUE;
            return (double) Math.min(x, y);
        } else {
            // if the merged array length is even, first get the current element.
            int x = i < a.size() ? a.get(i) : Integer.MAX_VALUE;
            int y = j < b.size() ? b.get(j) : Integer.MAX_VALUE;
            int current = Math.min(x, y);

            // then take the average of current element and the previous element and return it as median.
            return ((prevElement != null ? prevElement : 0) + current) / 2.0;
        }
    }

    public static Double getMedian(List<Integer> a, List<Integer> b) {
        /**
         * Overall time complexity is O(n) and space complexity is O(1).
         */

        // define pointer indices
        int i = 0, j = 0;

        // define the total size of the hypothetical merged array.
        int n = a.size() + b.size();

        // define the upper limit of the counter (the variable which will be used to break the while loops).
        int medianIndex = n/2;
        int counter = 0;

        // store the prevElement while traversing. This will be useful when the length of the array is even.
        Integer prevElement = null;

        // Typical merged array code from merge sort; but we will not actually merge.
        while (i < a.size() && j < b.size()) {
            if (a.get(i) <= b.get(j)) {
                prevElement = a.get(i);
                i += 1;
            } else {
                prevElement = b.get(j);
                j += 1;
            }

            // if the counter value reaches the medianIndex.
            counter += 1;
            if (counter == medianIndex) {
                // compute the median and return in O(1) time.
                return computeMedian(prevElement, a, b, n, i, j);
            }
        }

        // same logic when `j` is exhausted.
        while (i < a.size()) {
            prevElement = a.get(i);
            i += 1;
            counter += 1;
            if (counter == medianIndex) {
                return computeMedian(prevElement, a, b, n, i, j);
            }
        }

        // same logic when `i` is exhausted.
        while (j < b.size()) {
            prevElement = b.get(j);
            j += 1;
            counter += 1;
            if (counter == medianIndex) {
                return computeMedian(prevElement, a, b, n, i, j);
            }
        }
        return -1.0;
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println("Naive Solution.");
        System.out.println(NaiveSolution.getMedian(Arrays.asList(-5, 3, 6, 12, 15), Arrays.asList(-12, -10, -6, -3, 4, 10)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(1, 12, 15, 26, 38), Arrays.asList(2, 13, 17, 30, 45, 60)));
        System.out.println(NaiveSolution.getMedian(List.of(), Arrays.asList(2, 4, 5, 6)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(2, 3, 5, 8), Arrays.asList(10, 12, 14, 16, 18, 20)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(1, 3), List.of(2)));
        System.out.println(NaiveSolution.getMedian(Arrays.asList(1, 2), Arrays.asList(3, 4)));

        System.out.println("Better Solution.");
        System.out.println(BetterSolutionBS21.getMedian(Arrays.asList(-5, 3, 6, 12, 15), Arrays.asList(-12, -10, -6, -3, 4, 10)));
        System.out.println(BetterSolutionBS21.getMedian(Arrays.asList(1, 12, 15, 26, 38), Arrays.asList(2, 13, 17, 30, 45, 60)));
        System.out.println(BetterSolutionBS21.getMedian(List.of(), Arrays.asList(2, 4, 5, 6)));
        System.out.println(BetterSolutionBS21.getMedian(Arrays.asList(2, 3, 5, 8), Arrays.asList(10, 12, 14, 16, 18, 20)));
        System.out.println(BetterSolutionBS21.getMedian(Arrays.asList(1, 3), List.of(2)));
        System.out.println(BetterSolutionBS21.getMedian(Arrays.asList(1, 2), Arrays.asList(3, 4)));
    }
}