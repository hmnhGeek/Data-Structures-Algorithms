package DynamicProgramming.DP31;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n + m).
     */
    public static Integer getLcsLength(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        return solve(s1, n, s2, m);
    }
    
    private static Integer solve(String s1, int i, String s2, int j) {
        if (i == 0 || j == 0) {
            return 0;
        }
        if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
            return 1 + solve(s1, i - 1, s2, j - 1);
        }
        return Math.max(
                solve(s1, i - 1, s2, j),
                solve(s1, i, s2, j - 1)
        );
    }

    public static void main(String[] args) {
        System.out.println(getLcsLength("adebc", "dcadb"));
        System.out.println(getLcsLength("ab", "defg"));
        System.out.println(getLcsLength("abcde", "ace"));
        System.out.println(getLcsLength("abc", "abc"));
        System.out.println(getLcsLength("abc", "acd"));
        System.out.println(getLcsLength("AGGTAB", "GXTXAYB"));
        System.out.println(getLcsLength("ABC", "CBA"));
    }
}
