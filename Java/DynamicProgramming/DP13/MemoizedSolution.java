package DynamicProgramming.DP13;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(m^4 * n) and space complexity is O(m + n + m^2 * n).
     */
    public static Integer cherryPickup(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Integer maxChocolates = 0;
        Map<Integer, Map<Integer, Map<Integer, Integer>>> dp = getBlankDp(n, m);
        for (int alice = 0; alice < m; alice += 1) {
            for (int bob = 0; bob < m; bob += 1) {
                Integer chocolatesCollected = solve(mtx, n - 1, alice, bob, m, dp);
                maxChocolates = Math.max(chocolatesCollected, maxChocolates);
            }
        }
        return maxChocolates;
    }

    private static Map<Integer, Map<Integer, Map<Integer, Integer>>> getBlankDp(int n, int m) {
        Map<Integer, Map<Integer, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Map<Integer, Integer>> aliceRow = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                Map<Integer, Integer> bobRow = new HashMap<>();
                for (int k = 0; k < m; k += 1) {
                    bobRow.put(k, null);
                }
                aliceRow.put(j, bobRow);
            }
            dp.put(i, aliceRow);
        }
        return dp;
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int alice, int bob, int m, Map<Integer, Map<Integer, Map<Integer, Integer>>> dp) {
        if (i == 0) {
            if (alice == 0 && bob == m - 1) {
                return mtx.getFirst().getFirst() + mtx.getFirst().getLast();
            }
            return 0;
        }
        if (dp.get(i).get(alice).get(bob) != null) {
            return dp.get(i).get(alice).get(bob);
        }
        int maxChocolates = 0;
        for (int da = -1; da <= 1; da += 1) {
            for (int db = -1; db <= 1; db += 1) {
                if (0 <= alice + da && alice + da < m && 0 <= bob + db && bob + db < m) {
                    int chocolates = solve(mtx, i - 1, alice + da, bob + db, m, dp);
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
        dp.get(i).get(alice).put(bob, maxChocolates);
        return dp.get(i).get(alice).get(bob);
    }
}
