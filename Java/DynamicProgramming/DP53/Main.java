package DynamicProgramming.DP53;

public class Main {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.palindromePartitioning("aaccb"));
        System.out.println(RecursiveSolution.palindromePartitioning("ababa"));
        System.out.println(RecursiveSolution.palindromePartitioning("aababa"));
        System.out.println(RecursiveSolution.palindromePartitioning("aab"));
        System.out.println(RecursiveSolution.palindromePartitioning("a"));
        System.out.println(RecursiveSolution.palindromePartitioning("ab"));
        System.out.println(RecursiveSolution.palindromePartitioning("geek"));
        System.out.println(RecursiveSolution.palindromePartitioning("ababbbabbababa"));
        System.out.println(RecursiveSolution.palindromePartitioning("bababcbadcede"));
        System.out.println();

        System.out.println(MemoizedSolution.palindromePartitioning("aaccb"));
        System.out.println(MemoizedSolution.palindromePartitioning("ababa"));
        System.out.println(MemoizedSolution.palindromePartitioning("aababa"));
        System.out.println(MemoizedSolution.palindromePartitioning("aab"));
        System.out.println(MemoizedSolution.palindromePartitioning("a"));
        System.out.println(MemoizedSolution.palindromePartitioning("ab"));
        System.out.println(MemoizedSolution.palindromePartitioning("geek"));
        System.out.println(MemoizedSolution.palindromePartitioning("ababbbabbababa"));
        System.out.println(MemoizedSolution.palindromePartitioning("bababcbadcede"));
        System.out.println();

        System.out.println(TabulationSolution.palindromePartitioning("aaccb"));
        System.out.println(TabulationSolution.palindromePartitioning("ababa"));
        System.out.println(TabulationSolution.palindromePartitioning("aababa"));
        System.out.println(TabulationSolution.palindromePartitioning("aab"));
        System.out.println(TabulationSolution.palindromePartitioning("a"));
        System.out.println(TabulationSolution.palindromePartitioning("ab"));
        System.out.println(TabulationSolution.palindromePartitioning("geek"));
        System.out.println(TabulationSolution.palindromePartitioning("ababbbabbababa"));
        System.out.println(TabulationSolution.palindromePartitioning("bababcbadcede"));
        System.out.println();
    }
}
