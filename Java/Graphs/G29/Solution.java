package Graphs.G29;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        /*
        print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["poon", "plee", "same", "poie","plea","plie","poin"], "toon", "plea"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))
         */
        System.out.println(WordLadder.getMinimumLength(Arrays.asList("des","der","dfr","dgt","dfs"), "der", "dfs"));
    }
}
