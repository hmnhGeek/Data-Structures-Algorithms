package DynamicProgramming.DP55;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Max area in histogram");
        System.out.println(Utils.getMaxAreaInHistogram(Arrays.asList(60, 20, 50, 40, 10, 50, 60)));
        System.out.println(Utils.getMaxAreaInHistogram(Arrays.asList(3, 5, 1, 7, 5, 9)));

        System.out.println("Max rectangle");
        System.out.println(
                maxAreaRectangle(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(1, 1, 1, 1),
                                Arrays.asList(1, 1, 1, 1),
                                Arrays.asList(1, 1, 0, 0)
                        )
                )
        );

        System.out.println(
                Solution.maxAreaRectangle(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1),
                                Arrays.asList(1, 1, 1),
                                Arrays.asList(0, 1, 1)
                        )
                )
        );

        System.out.println(
                Solution.maxAreaRectangle(
                        Arrays.asList(
                                Arrays.asList(1, 0, 1, 0, 0),
                                Arrays.asList(1, 0, 1, 1, 1),
                                Arrays.asList(1, 1, 1, 1, 1),
                                Arrays.asList(1, 0, 0, 1, 0)
                        )
                )
        );
    }

    public static Integer maxAreaRectangle(List<List<Integer>> matrix) {
        /*
            Time complexity is O(nm) and space complexity is O(m).
         */

        Integer maxArea = 0;
        int n = matrix.size(), m = matrix.getFirst().size();

        // create a previous row. It will take O(m) extra space.
        List<Integer> prevRow = new ArrayList<>(Collections.nCopies(m, 0));
        for (int i = 0; i < n; i += 1) {
            List<Integer> currRow = matrix.get(i);

            // create a histogram with another O(m) space and update the max area.
            List<Integer> histogram = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                if (currRow.get(j).equals(0)) {
                    histogram.add(0);
                } else {
                    histogram.add(currRow.get(j) + prevRow.get(j));
                }
            }

            // get the max area in O(m) time and O(m) space.
            Integer area = Utils.getMaxAreaInHistogram(histogram);
            maxArea = Math.max(maxArea, area);

            // remember to update previous row.
            prevRow = histogram;
        }
        return maxArea;
    }
}
