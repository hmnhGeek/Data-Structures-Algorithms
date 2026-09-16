// Problem link - https://www.geeksforgeeks.org/problems/max-rectangle/1
// Solution -

package PracticeSet2.Matrix.Problem6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer maxRectangle(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(m).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> prev = getBlankPrevRow(m);
        Integer maxArea = 0;
        for (int i = 0; i < n; i += 1) {
            List<Integer> currRow = mtx.get(i);
            List<Integer> histogram = getHistogram(prev, currRow, m);
            Integer area = Utils.maxAreaInHistogram(histogram);
            maxArea = Math.max(maxArea, area);
            prev = histogram;
        }
        return maxArea;
    }

    private static List<Integer> getHistogram(List<Integer> prev, List<Integer> currRow, int m) {
        for (int j = 0; j < m; j += 1) {
            if (currRow.get(j) == 0) {
                prev.set(j, 0);
                continue;
            }
            prev.set(j, prev.get(j) + currRow.get(j));
        }
        return prev;
    }

    private static List<Integer> getBlankPrevRow(int m) {
        List<Integer> prev = new ArrayList<>();
        for (int j = 0; j < m; j += 1) {
            prev.add(0);
        }
        return prev;
    }

    public static void main(String[] args) {
        System.out.println("Max area in histogram");
        System.out.println(Utils.maxAreaInHistogram(Arrays.asList(60, 20, 50, 40, 10, 50, 60)));
        System.out.println(Utils.maxAreaInHistogram(Arrays.asList(3, 5, 1, 7, 5, 9)));
        System.out.println();
        System.out.println("Max Rectangle");
        System.out.println(
                maxRectangle(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(1, 1, 1, 1),
                                Arrays.asList(1, 1, 1, 1),
                                Arrays.asList(1, 1, 0, 0)
                        )
                )
        );

        System.out.println(
                maxRectangle(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1),
                                Arrays.asList(1, 1, 1),
                                Arrays.asList(0, 1, 1)
                        )
                )
        );

        System.out.println(
                maxRectangle(
                        Arrays.asList(
                                Arrays.asList(1, 0, 1, 0, 0),
                                Arrays.asList(1, 0, 1, 1, 1),
                                Arrays.asList(1, 1, 1, 1, 1),
                                Arrays.asList(1, 0, 0, 1, 0)
                        )
                )
        );
    }
}
