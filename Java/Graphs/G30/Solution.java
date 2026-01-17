package Graphs.G30;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        /*
            print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))
         */
        System.out.println(WordLadder.getWordLadder(Arrays.asList("des","der","dfr","dgt","dfs"), "der", "dfs"));
    }
}
