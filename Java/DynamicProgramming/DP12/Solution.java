package DynamicProgramming.DP12;

import java.util.List;

public class Solution {
    public static void recursive() {
        System.out.println(
                RecursiveSolution.getMaxFallingSum(
                        List.of(
                                List.of(1, 2, 10, 4),
                                List.of(100, 3, 2, 1),
                                List.of(1, 1, 20, 2),
                                List.of(1, 2, 2, 1)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getMaxFallingSum(
                        List.of(
                                List.of(10, 2, 3),
                                List.of(3, 7, 2),
                                List.of(8, 1, 5)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getMaxFallingSum(
                        List.of(
                                List.of(1, 2, 3),
                                List.of(9, 8, 7),
                                List.of(4, 5, 6)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.getMaxFallingSum(
                        List.of(
                                List.of(10, 10, 2, -13, 20, 4),
                                List.of(1, -9, -81, 30, 2, 5),
                                List.of(0, 10, 4, -79, 2, -10),
                                List.of(1, -5, 2, 20, -11, 4)
                        )
                )
        );
    }

    public static void memoized() {
        System.out.println(
                MemoizedSolution.getMaxFallingSum(
                        List.of(
                                List.of(1, 2, 10, 4),
                                List.of(100, 3, 2, 1),
                                List.of(1, 1, 20, 2),
                                List.of(1, 2, 2, 1)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getMaxFallingSum(
                        List.of(
                                List.of(10, 2, 3),
                                List.of(3, 7, 2),
                                List.of(8, 1, 5)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getMaxFallingSum(
                        List.of(
                                List.of(1, 2, 3),
                                List.of(9, 8, 7),
                                List.of(4, 5, 6)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.getMaxFallingSum(
                        List.of(
                                List.of(10, 10, 2, -13, 20, 4),
                                List.of(1, -9, -81, 30, 2, 5),
                                List.of(0, 10, 4, -79, 2, -10),
                                List.of(1, -5, 2, 20, -11, 4)
                        )
                )
        );
    }

    public static void main(String[] args) {
        recursive();
        System.out.println();
        memoized();
    }
}
