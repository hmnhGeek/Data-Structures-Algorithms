package Strings.Problem14;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n + m).
     */
    public static Integer getMinOps(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        return solve(s1, n - 1, s2, m - 1);
    }

    public static Integer solve(String s1, int i, String s2, int j) {
        if (i < 0) return j + 1;
        if (j < 0) return i + 1;
        if (s1.charAt(i) == s2.charAt(j)) {
            return solve(s1, i - 1, s2, j - 1);
        }
        return Math.min(
                Math.min(
                        1 + solve(s1, i, s2, j - 1),
                        1 + solve(s1, i - 1, s2, j)
                ),
                1 + solve(s1, i - 1, s2, j - 1)
        );
    }
}
