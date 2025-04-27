package DynamicProgramming.DP53;

public class RecursiveSolution {
    private static boolean isPalindrome(String string) {
        int i = 0, j = string.length() - 1;
        while (i <= j) {
            if (string.charAt(i) == string.charAt(j)) {
                i += 1;
                j -= 1;
            } else {
                return false;
            }
        }
        return true;
    }

    private static Integer solve(String string, Integer i, Integer n) {
        if (i.equals(n)) return 0;
        Integer minimumPartitions = Integer.MAX_VALUE;
        StringBuilder temp = new StringBuilder();
        for (int j = i; j < n; j += 1) {
            temp.append(string.charAt(j));
            if (isPalindrome(String.valueOf(temp))) {
                Integer partitions = 1 + solve(string, j + 1, n);
                minimumPartitions = Math.min(minimumPartitions, partitions);
            }
        }
        return minimumPartitions;
    }

    public static Integer palindromePartitioning(String string) {
        int n = string.length();
        return solve(string, 0, n) - 1;
    }
}
