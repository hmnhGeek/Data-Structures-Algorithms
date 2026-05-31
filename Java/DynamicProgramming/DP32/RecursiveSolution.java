package DynamicProgramming.DP32;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n + m).
     */
    public static Integer getDistinctSubsequencesCount(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        return solve(s1, n, s2, m);
    }

    private static Integer solve(String s1, int i, String s2, int j) {
        if (j == 0) return 1;
        if (i == 0) return 0;
        if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
            return solve(s1, i - 1, s2, j - 1) + solve(s1, i - 1, s2, j);
        } else {
            return solve(s1, i - 1, s2, j);
        }
    }
}
