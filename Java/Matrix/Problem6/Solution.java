package Matrix.Problem6;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Max area in histogram");
        System.out.println(Utility.getMaxAreaInHistogram(Arrays.asList(60, 20, 50, 40, 10, 50, 60)));
        System.out.println(Utility.getMaxAreaInHistogram(Arrays.asList(3, 5, 1, 7, 5, 9)));
        System.out.println();
        System.out.println("Max Rectangle");
        System.out.println(
                Utility.maxRectangle(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1, 0),
                                Arrays.asList(1, 1, 1, 1),
                                Arrays.asList(1, 1, 1, 1),
                                Arrays.asList(1, 1, 0, 0)
                        )
                )
        );

        System.out.println(
                Utility.maxRectangle(
                        Arrays.asList(
                                Arrays.asList(0, 1, 1),
                                Arrays.asList(1, 1, 1),
                                Arrays.asList(0, 1, 1)
                        )
                )
        );

        System.out.println(
                Utility.maxRectangle(
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
