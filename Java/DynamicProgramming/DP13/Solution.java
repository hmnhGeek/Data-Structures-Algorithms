package DynamicProgramming.DP13;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        System.out.println();
        memoized();
        System.out.println();
        tabulation();
        System.out.println();
        spaceOptimized();
        System.out.println();
    }

    public static void recursive() {
        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 3, 1, 2),
                                Arrays.asList(3, 4, 2, 2),
                                Arrays.asList(5, 6, 3, 5)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(1, 1),
                                Arrays.asList(1, 2)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 7),
                                Arrays.asList(7, 6)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 5),
                                Arrays.asList(3, 7),
                                Arrays.asList(4, 2)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(2, 5, 1),
                                Arrays.asList(1, 5, 5),
                                Arrays.asList(2, 1, 1)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 1, 2),
                                Arrays.asList(3, 6, 1),
                                Arrays.asList(1, 6, 6),
                                Arrays.asList(3, 1, 2)
                        )
                )
        );

        System.out.println(
                RecursiveSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 0, 0, 0, 0, 0, 2),
                                Arrays.asList(2, 1, 0, 0, 0, 4, 0),
                                Arrays.asList(2, 0, 10, 0, 1, 0, 0),
                                Arrays.asList(0, 3, 0, 6, 5, 0, 0),
                                Arrays.asList(1, 0, 3, 4, 0, 0, 6)
                        )
                )
        );
    }

    public static void memoized() {
        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 3, 1, 2),
                                Arrays.asList(3, 4, 2, 2),
                                Arrays.asList(5, 6, 3, 5)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(1, 1),
                                Arrays.asList(1, 2)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 7),
                                Arrays.asList(7, 6)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 5),
                                Arrays.asList(3, 7),
                                Arrays.asList(4, 2)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(2, 5, 1),
                                Arrays.asList(1, 5, 5),
                                Arrays.asList(2, 1, 1)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 1, 2),
                                Arrays.asList(3, 6, 1),
                                Arrays.asList(1, 6, 6),
                                Arrays.asList(3, 1, 2)
                        )
                )
        );

        System.out.println(
                MemoizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 0, 0, 0, 0, 0, 2),
                                Arrays.asList(2, 1, 0, 0, 0, 4, 0),
                                Arrays.asList(2, 0, 10, 0, 1, 0, 0),
                                Arrays.asList(0, 3, 0, 6, 5, 0, 0),
                                Arrays.asList(1, 0, 3, 4, 0, 0, 6)
                        )
                )
        );
    }

    public static void tabulation() {
        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 3, 1, 2),
                                Arrays.asList(3, 4, 2, 2),
                                Arrays.asList(5, 6, 3, 5)
                        )
                )
        );

        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(1, 1),
                                Arrays.asList(1, 2)
                        )
                )
        );

        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 7),
                                Arrays.asList(7, 6)
                        )
                )
        );

        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 5),
                                Arrays.asList(3, 7),
                                Arrays.asList(4, 2)
                        )
                )
        );

        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(2, 5, 1),
                                Arrays.asList(1, 5, 5),
                                Arrays.asList(2, 1, 1)
                        )
                )
        );

        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 1, 2),
                                Arrays.asList(3, 6, 1),
                                Arrays.asList(1, 6, 6),
                                Arrays.asList(3, 1, 2)
                        )
                )
        );

        System.out.println(
                TabulationSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 0, 0, 0, 0, 0, 2),
                                Arrays.asList(2, 1, 0, 0, 0, 4, 0),
                                Arrays.asList(2, 0, 10, 0, 1, 0, 0),
                                Arrays.asList(0, 3, 0, 6, 5, 0, 0),
                                Arrays.asList(1, 0, 3, 4, 0, 0, 6)
                        )
                )
        );
    }

    public static void spaceOptimized() {
        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 3, 1, 2),
                                Arrays.asList(3, 4, 2, 2),
                                Arrays.asList(5, 6, 3, 5)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(1, 1),
                                Arrays.asList(1, 2)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 7),
                                Arrays.asList(7, 6)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 5),
                                Arrays.asList(3, 7),
                                Arrays.asList(4, 2)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(3, 1, 1),
                                Arrays.asList(2, 5, 1),
                                Arrays.asList(1, 5, 5),
                                Arrays.asList(2, 1, 1)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(4, 1, 2),
                                Arrays.asList(3, 6, 1),
                                Arrays.asList(1, 6, 6),
                                Arrays.asList(3, 1, 2)
                        )
                )
        );

        System.out.println(
                SpaceOptimizedSolution.cherryPickup(
                        Arrays.asList(
                                Arrays.asList(2, 0, 0, 0, 0, 0, 2),
                                Arrays.asList(2, 1, 0, 0, 0, 4, 0),
                                Arrays.asList(2, 0, 10, 0, 1, 0, 0),
                                Arrays.asList(0, 3, 0, 6, 5, 0, 0),
                                Arrays.asList(1, 0, 3, 4, 0, 0, 6)
                        )
                )
        );
    }
}
