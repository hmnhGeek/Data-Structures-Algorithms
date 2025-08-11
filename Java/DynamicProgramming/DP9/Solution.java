package DynamicProgramming.DP9;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
    }

    private static void recursive() {
        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0, 0),
                                Arrays.asList(0, -1, 0),
                                Arrays.asList(0, 0, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, 0),
                                Arrays.asList(0, 0)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getPathCount(
                        Arrays.asList(
                                Arrays.asList(0, -1),
                                Arrays.asList(-1, 0)
                        )
                )
        );

        System.out.println();
    }
}
