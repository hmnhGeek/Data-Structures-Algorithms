package DynamicProgramming.DP13;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(m^4 * n) and space complexity is O(m^2 * n).
     */
    public static Integer cherryPickup(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        Integer maxChocolates = 0;
        Map<Integer, Map<Integer, Map<Integer, Integer>>> dp = getBlankDp(n, m);

        // alice = 0 and bob = m - 1
        dp.get(0).get(0).put(m - 1, mtx.getFirst().getFirst() + mtx.getFirst().getLast());

        for (int alice = 0; alice < m; alice += 1) {
            for (int bob = 0; bob < m; bob += 1) {
                for (int i = 1; i < n; i += 1) {
                    for (int a = 0; a < m; a += 1) {
                        for (int b = 0; b < m; b += 1) {
                            int maximumChocolatesObtained = 0;
                            for (int da = -1; da <= 1; da += 1) {
                                for (int db = -1; db <= 1; db += 1) {
                                    if (0 <= a + da && a + da < m && 0 <= b + db && b + db < m) {
                                        int chocolates = dp.get(i - 1).get(a + da).get(b + db);
                                        if (a == b) {
                                            maximumChocolatesObtained = Math.max(maximumChocolatesObtained, mtx.get(i).get(a) + chocolates);
                                        } else {
                                            maximumChocolatesObtained = Math.max(
                                                    maximumChocolatesObtained,
                                                    mtx.get(i).get(a) + mtx.get(i).get(b) + chocolates
                                            );
                                        }
                                    }
                                }
                            }
                            dp.get(i).get(a).put(b, maximumChocolatesObtained);
                        }
                    }
                }
                maxChocolates = Math.max(dp.get(n - 1).get(alice).get(bob), maxChocolates);
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
                    bobRow.put(k, 0);
                }
                aliceRow.put(j, bobRow);
            }
            dp.put(i, aliceRow);
        }
        return dp;
    }
}
