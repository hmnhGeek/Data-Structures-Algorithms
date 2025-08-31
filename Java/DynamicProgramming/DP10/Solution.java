package DynamicProgramming.DP10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 9, 6),
                                Arrays.asList(11, 5, 2)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        List.of(List.of(5))
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 4),
                                Arrays.asList(7, 5, 9)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(5, 6),
                                Arrays.asList(1, 2)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 3, 1),
                                Arrays.asList(1, 5, 1),
                                Arrays.asList(4, 2, 1)
                        )
                )
        );
        System.out.println(
                RecursiveSolution.minPathSum(
                        Arrays.asList(
                                Arrays.asList(1, 2, 3),
                                Arrays.asList(4, 5, 6)
                        )
                )
        );
    }
}
