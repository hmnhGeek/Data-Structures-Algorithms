package DynamicProgramming.DP29;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    private static Integer getLCSLength(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        return solve(s1, n, s2, m);
    }

    private static Integer solve(String s1, int i, String s2, int j) {
        if (i == 0 || j == 0) return 0;
        if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
            return 1 + solve(s1, i - 1, s2, j - 1);
        }
        return Math.max(
                solve(s1, i - 1, s2, j),
                solve(s1, i, s2, j - 1)
        );
    }

    private static Integer getLPSLength(String string) {
        StringBuilder sb = new StringBuilder();
        for (int i = string.length() - 1; i >= 0; i -= 1) {
            sb.append(string.charAt(i));
        }
        return getLCSLength(string, sb.toString());
    }

    public static Integer getMinCharToMakePalindrome(String string) {
        Integer lps = getLPSLength(string);
        return string.length() - lps;
    }
}
