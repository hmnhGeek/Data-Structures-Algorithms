// Problem link - https://www.geeksforgeeks.org/problems/word-ladder/1
// Solution - https://www.youtube.com/watch?v=tRPda0rcf8E&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=29


package Graphs.G29;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        /*
            Time complexity is O(n * word_length * 26) and space complexity is O(n).
         */
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("des","der","dfr","dgt","dfs"), "der", "dfs"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("geek", "gefk"), "gedk", "geek"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("poon", "plee", "same", "poie","plea","plie","poin"), "toon", "plea"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("hot","dot","dog","lot","log","cog"), "hit", "cog"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("hot","dot","dog","lot","log"), "hit", "cog"));

    }
}
