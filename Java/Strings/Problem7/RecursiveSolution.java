package Strings.Problem7;

public class RecursiveSolution {
    public static Integer findLcs(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        return solve(s1, n1 - 1, s2, n2 - 1);
    }

    public static Integer solve(String s1, int i, String s2, int j) {
        /*
            Time complexity is exponential and space complexity is O(m + n).
         */
        if (i < 0 || j < 0) return 0;
        if (s1.charAt(i) == s2.charAt(j)) {
            return 1 + solve(s1, i - 1, s2, j - 1);
        } else {
            return Math.max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1));
        }
    }
}
