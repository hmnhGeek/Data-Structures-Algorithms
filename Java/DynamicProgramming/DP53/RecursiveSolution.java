package DynamicProgramming.DP53;

public class RecursiveSolution {
    private static Integer solve(String string, Integer i, Integer n) {
        if (i.equals(n)) return 0;
        Integer minimumPartitions = Integer.MAX_VALUE;
        StringBuilder temp = new StringBuilder();
        for (int j = i; j < n; j += 1) {
            temp.append(string.charAt(j));
            if (PalindromeChecker.isPalindrome(String.valueOf(temp))) {
                Integer partitions = 1 + solve(string, j + 1, n);
                minimumPartitions = Math.min(minimumPartitions, partitions);
            }
        }
        return minimumPartitions;
    }

    public static Integer palindromePartitioning(String string) {
        /*
            Time complexity is exponential and space complexity is O(n).
         */
        int n = string.length();
        return solve(string, 0, n) - 1;
    }
}
