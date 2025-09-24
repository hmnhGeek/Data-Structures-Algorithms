package DynamicProgramming.DP13;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(m + n).
     */
    public static Integer cherryPickup(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Integer maxChocolates = 0;
        for (int alice = 0; alice < m; alice += 1) {
            for (int bob = 0; bob < m; bob += 1) {
                Integer chocolatesCollected = solve(mtx, n - 1, alice, bob, m);
                maxChocolates = Math.max(chocolatesCollected, maxChocolates);
            }
        }
        return maxChocolates;
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int alice, int bob, int m) {
        if (i == 0) {
            if (alice == 0 && bob == m - 1) {
                return mtx.getFirst().getFirst() + mtx.getFirst().getLast();
            }
            return 0;
        }
        int maxChocolates = 0;
        for (int da = -1; da <= 1; da += 1) {
            for (int db = -1; db <= 1; db += 1) {
                if (0 <= alice + da && alice + da < m && 0 <= bob + db && bob + db < m) {
                    int chocolates = solve(mtx, i - 1, alice + da, bob + db, m);
                    if (alice == bob) {
                        maxChocolates = Math.max(maxChocolates, mtx.get(i).get(alice) + chocolates);
                    } else {
                        maxChocolates = Math.max(
                                maxChocolates,
                                mtx.get(i).get(alice) + mtx.get(i).get(bob) + chocolates
                        );
                    }
                }
            }
        }
        return maxChocolates;
    }
}
