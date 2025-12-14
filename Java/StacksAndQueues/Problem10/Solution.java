// Problem link - https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
// Solution - https://www.youtube.com/watch?v=cEadsbTeze4


package StacksAndQueues.Problem10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getCelebrity(List<List<Integer>> mtx) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = mtx.size();
        int top = 0, down = n - 1;
        while (top < down) {
            if (mtx.get(top).get(down) == 1) {
                top += 1;
            } else if (mtx.get(down).get(top) == 1) {
                down -= 1;
            } else {
                top += 1;
                down -= 1;
            }
        }
        if (top > down) return -1;
        for (int i = 0; i < n; i += 1) {
            if (i != top && !(mtx.get(top).get(i) == 0 && mtx.get(i).get(top) == 1)) {
                return -1;
            }
        }
        return top;
    }

    public static void main(String[] args) {
        System.out.println(
                Solution.getCelebrity(Arrays.asList(
                        Arrays.asList(0, 0, 1, 0),
                        Arrays.asList(0, 0, 1, 0),
                        Arrays.asList(0, 0, 0, 0),
                        Arrays.asList(0, 0, 1, 0)
                ))
        );

        System.out.println(
                Solution.getCelebrity(Arrays.asList(
                        Arrays.asList(0, 1),
                        Arrays.asList(1, 0)
                ))
        );

        System.out.println(
                Solution.getCelebrity(Arrays.asList(
                        Arrays.asList(0)
                ))
        );

        System.out.println(
                Solution.getCelebrity(Arrays.asList(
                        Arrays.asList(0, 0, 1, 0),
                        Arrays.asList(0, 0, 1, 0),
                        Arrays.asList(0, 1, 0, 0),
                        Arrays.asList(0, 0, 1, 0)
                ))
        );
    }
}
