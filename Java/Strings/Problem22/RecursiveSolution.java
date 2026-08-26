package Strings.Problem22;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer countPalindromicSubsequences(String string) {
        int n = string.length();
        return solve(string, 0, n - 1);
    }

    private static Integer solve(String string, int i, int j) {
        if (i > j) return 0;
        if (i == j) return 1;
        if (string.charAt(i) == string.charAt(j)) {
            return 1 + solve(string, i + 1, j) + solve(string, i, j - 1);
        } else {
            return solve(string, i + 1, j) + solve(string, i, j - 1) - solve(string, i + 1, j - 1);
        }
    }
}
