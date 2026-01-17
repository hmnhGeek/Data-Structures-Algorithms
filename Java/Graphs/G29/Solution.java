package Graphs.G29;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("des","der","dfr","dgt","dfs"), "der", "dfs"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("geek", "gefk"), "gedk", "geek"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("poon", "plee", "same", "poie","plea","plie","poin"), "toon", "plea"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("hot","dot","dog","lot","log","cog"), "hit", "cog"));
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("hot","dot","dog","lot","log"), "hit", "cog"));

    }
}
