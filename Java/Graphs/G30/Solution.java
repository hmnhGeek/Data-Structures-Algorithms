// Problem link - https://www.geeksforgeeks.org/problems/word-ladder-ii/1
// Solution - https://www.youtube.com/watch?v=DREutrv2XD0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=30


package Graphs.G30;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(WordLadder.getWordLadder(Arrays.asList("des","der","dfr","dgt","dfs"), "der", "dfs"));
        System.out.println(WordLadder.getWordLadder(Arrays.asList("geek", "gefk"), "gedk", "geek"));
        System.out.println(WordLadder.getWordLadder(Arrays.asList("hot","dot","dog","lot","log","cog"), "hit", "cog"));
        System.out.println(WordLadder.getWordLadder(Arrays.asList("hot","dot","dog","lot","log"), "hit", "cog"));
    }
}
