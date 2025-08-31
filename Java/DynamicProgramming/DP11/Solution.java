package DynamicProgramming.DP11;

import java.util.Arrays;

public class Solution {
    private static void recursive() {
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(1),
                                Arrays.asList(2, 3),
                                Arrays.asList(3, 6, 7),
                                Arrays.asList(8, 9, 6, 10)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(2),
                                Arrays.asList(3, 4),
                                Arrays.asList(6, 5, 7),
                                Arrays.asList(4, 1, 8, 3)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(-10)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(1),
                                Arrays.asList(2, 3),
                                Arrays.asList(4, 5, 6),
                                Arrays.asList(7, 8, 9, 10)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(5),
                                Arrays.asList(-1, 3),
                                Arrays.asList(22, 1, -9)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(2),
                                Arrays.asList(3, 7),
                                Arrays.asList(8, 5, 6),
                                Arrays.asList(6, 1, 9, 3)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(3),
                                Arrays.asList(6, 9),
                                Arrays.asList(8, 7, 1),
                                Arrays.asList(9, 6, 8, 2)
                        )
                )
        );
    }

    private static void memoized() {
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(1),
                                Arrays.asList(2, 3),
                                Arrays.asList(3, 6, 7),
                                Arrays.asList(8, 9, 6, 10)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(2),
                                Arrays.asList(3, 4),
                                Arrays.asList(6, 5, 7),
                                Arrays.asList(4, 1, 8, 3)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(-10)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(1),
                                Arrays.asList(2, 3),
                                Arrays.asList(4, 5, 6),
                                Arrays.asList(7, 8, 9, 10)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(5),
                                Arrays.asList(-1, 3),
                                Arrays.asList(22, 1, -9)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(2),
                                Arrays.asList(3, 7),
                                Arrays.asList(8, 5, 6),
                                Arrays.asList(6, 1, 9, 3)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMinPathSum(
                        Arrays.asList(
                                Arrays.asList(3),
                                Arrays.asList(6, 9),
                                Arrays.asList(8, 7, 1),
                                Arrays.asList(9, 6, 8, 2)
                        )
                )
        );
    }

    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        recursive();
        System.out.println();
        System.out.println("Memoized Solution");
        memoized();
        System.out.println();
    }
}
