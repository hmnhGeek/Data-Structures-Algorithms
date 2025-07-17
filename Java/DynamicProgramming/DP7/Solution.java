package DynamicProgramming.DP7;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                RecursiveSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(1, 2, 5),
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(3, 3, 3)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 40, 70),
                                Arrays.asList(20, 50, 80),
                                Arrays.asList(30, 60, 90)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(18, 11, 19),
                                Arrays.asList(4, 13, 7),
                                Arrays.asList(1, 8, 13)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 50, 1),
                                Arrays.asList(5, 100, 11)
                        )
                )
        );
        System.out.println();
        System.out.println(
                MemoizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(1, 2, 5),
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(3, 3, 3)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 40, 70),
                                Arrays.asList(20, 50, 80),
                                Arrays.asList(30, 60, 90)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(18, 11, 19),
                                Arrays.asList(4, 13, 7),
                                Arrays.asList(1, 8, 13)
                        )
                )
        );
        System.out.println(
                MemoizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 50, 1),
                                Arrays.asList(5, 100, 11)
                        )
                )
        );
        System.out.println();
        System.out.println(
                TabulationSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(1, 2, 5),
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(3, 3, 3)
                        )
                )
        );
        System.out.println(
                TabulationSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 40, 70),
                                Arrays.asList(20, 50, 80),
                                Arrays.asList(30, 60, 90)
                        )
                )
        );
        System.out.println(
                TabulationSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(18, 11, 19),
                                Arrays.asList(4, 13, 7),
                                Arrays.asList(1, 8, 13)
                        )
                )
        );
        System.out.println(
                TabulationSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 50, 1),
                                Arrays.asList(5, 100, 11)
                        )
                )
        );
        System.out.println();
        System.out.println(
                SpaceOptimizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(1, 2, 5),
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(3, 3, 3)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 40, 70),
                                Arrays.asList(20, 50, 80),
                                Arrays.asList(30, 60, 90)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(18, 11, 19),
                                Arrays.asList(4, 13, 7),
                                Arrays.asList(1, 8, 13)
                        )
                )
        );
        System.out.println(
                SpaceOptimizedSolution.getMaxPoints(
                        Arrays.asList(
                                Arrays.asList(10, 50, 1),
                                Arrays.asList(5, 100, 11)
                        )
                )
        );
    }
}
