package PracticeSet1.Matrix.Problem6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer maxRectangle(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm) and space complexity is O(m).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        List<Integer> prevRow = new ArrayList<>();
        Integer maxArea = 0;
        for (int j = 0; j < m; j += 1) {
            prevRow.add(0);
        }
        for (int i = 0; i < n; i += 1) {
            List<Integer> histogram = new ArrayList<>();
            for (int j = 0; j < m; j += 1) {
                if (mtx.get(i).get(j) == 0) {
                    histogram.add(0);
                } else {
                    histogram.add(prevRow.get(j) + mtx.get(i).get(j));
                }
            }
            Integer area = Utils.getMaxAreaHistogram(histogram);
            maxArea = Math.max(area, maxArea);
            prevRow = histogram;
        }
        return maxArea;
    }

    public static void main(String[] args) {
        System.out.println("Max area in histogram");
        System.out.println(Utils.getMaxAreaHistogram(Arrays.asList(60, 20, 50, 40, 10, 50, 60)));
        System.out.println(Utils.getMaxAreaHistogram(Arrays.asList(3, 5, 1, 7, 5, 9)));
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
