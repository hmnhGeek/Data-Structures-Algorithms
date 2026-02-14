package DynamicProgramming.DP25;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n + m).
     */
    public static Integer getLcs(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        return solve(s1, n - 1, s2, m - 1);
    }

    private static Integer solve(String s1, int i, String s2, int j) {
        if (i < 0 || j < 0) return 0;
        if (s1.charAt(i) == s2.charAt(j)) {
            return 1 + solve(s1, i - 1, s2, j - 1);
        }
        return Math.max(
                solve(s1, i - 1, s2, j),
                solve(s1, i, s2, j - 1)
        );
    }
}
