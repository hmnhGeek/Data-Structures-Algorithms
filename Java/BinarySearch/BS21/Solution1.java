package BinarySearch.BS21;

import java.util.List;

public class Solution1 {
    private static Integer getMinFromArrays(List<Integer> arr1, int i, List<Integer> arr2, int j, int n, int m) {
        if (i < n && j < m) {
            return Math.min(arr1.get(i), arr2.get(j));
        } else if (i < n) {
            return arr1.get(i);
        } else if (j < m) {
            return arr2.get(j);
        }
        return null;
    }

    public static Double getMedian(List<Integer> arr1, List<Integer> arr2) {
        /*
            Time complexity is O(m + n) and space complexity is O(1).
         */
        int n1 = arr1.size(), n2 = arr2.size();
        if (n1 == 0) return getMedian(arr2);
        if (n2 == 0) return getMedian(arr1);
        int n = n1 + n2;
        int i1 = (n/2) - 1, i2 = n/2;
        Integer e1 = null, e2 = null;
        int counter = 0;
        int i = 0, j = 0;
        while (e2 == null) {
            if (i1 == counter) {
                e1 = getMinFromArrays(arr1, i, arr2, j, n1, n2);
            }
            if (i2 == counter) {
                e2 = getMinFromArrays(arr1, i, arr2, j, n1, n2);
            }

            if (i < arr1.size() && j < arr2.size()) {
                if (arr1.get(i) <= arr2.get(j)) {
                    i += 1;
                } else {
                    j += 1;
                }
            } else if (i < arr1.size()) {
                i += 1;
            } else if (j < arr2.size()) {
                j += 1;
            } else {
                break;
            }
            counter += 1;
        }
        if (n % 2 == 0) {
            return (e1 + e2)/2.0;
        }
        return (double) e2;
    }

    private static Double getMedian(List<Integer> arr) {
        if (arr.isEmpty()) return null;
        int n = arr.size();
        if (n % 2 == 0) {
            return (arr.get(n / 2) + arr.get((n /2) - 1))/2.0;
        }
        return (double) arr.get(n / 2);
    }
}
