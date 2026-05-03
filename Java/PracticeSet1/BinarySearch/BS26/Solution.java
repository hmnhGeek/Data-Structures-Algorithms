// Problem link - https://www.geeksforgeeks.org/find-peak-element-2d-array/
// Solution - https://www.youtube.com/watch?v=nGGp5XBzC4g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=28


package PracticeSet1.BinarySearch.BS26;

import java.util.List;

public class Solution {
    public static List<Integer> getPeak(List<List<Integer>> mtx) {
        /*
            Time complexity is O(n * log(m)) and space complexity is O(1).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        int low = 0, high = m - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int row = getPossiblePeakRow(mtx, n, m, mid);
            Integer possiblePeak = mtx.get(row).get(mid);
            Integer left = mid - 1 >= 0 ? mtx.get(row).get(mid - 1) : Integer.MIN_VALUE;
            Integer right = mid + 1 < m ? mtx.get(row).get(mid + 1) : Integer.MIN_VALUE;
            if (left < possiblePeak && possiblePeak > right) {
                return List.of(row, mid);
            }
            if (left > possiblePeak) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return null;
    }

    private static int getPossiblePeakRow(List<List<Integer>> mtx, int n, int m, int mid) {
        Integer maxVal = Integer.MIN_VALUE;
        Integer row = -1;
        for (int i = 0; i < n; i += 1) {
            if (mtx.get(i).get(mid) > maxVal) {
                maxVal = mtx.get(i).get(mid);
                row = i;
            }
        }
        return row;
    }

    public static void main(String[] args) {

        System.out.println(
                Solution.getPeak(
                        List.of(
                                List.of(8, 6),
                                List.of(10, 1)
                        )
                )
        );

        System.out.println(
                Solution.getPeak(
                        List.of(
                                List.of(1, 2, 3),
                                List.of(4, 5, 6),
                                List.of(7, 8, 9)
                        )
                )
        );

        System.out.println(
                Solution.getPeak(
                        List.of(
                                List.of(1, 4),
                                List.of(3, 2)
                        )
                )
        );

        System.out.println(
                Solution.getPeak(
                        List.of(
                                List.of(10, 20, 15),
                                List.of(21, 30, 14),
                                List.of(7, 16, 32)
                        )
                )
        );
    }
}
