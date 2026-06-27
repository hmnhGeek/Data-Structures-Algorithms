package DynamicProgramming.DP34;

public class RecursiveSolution {
    public static boolean isMatching(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        return solve(s1, n, s2, m);
    }

    private static boolean solve(String s1, int i, String s2, int j) {
        if (i == 0 && j == 0) return true;
        if (i == 0 && j > 0) return false;
        if (i > 0 && j == 0) {
            for (int k = i - 1; k >= 0; k -= 1) {
                if (s1.charAt(k) != '*') return false;
            }
            return true;
        }
        if (s1.charAt(i - 1) == s2.charAt(j - 1) || s1.charAt(i - 1) == '?') {
            return solve(s1, i - 1, s2, j - 1);
        } else if (s1.charAt(i - 1) == '*') {
            return solve(s1, i - 1, s2, j) || solve(s1, i, s2, j - 1);
        } else {
            return false;
        }
    }
}
