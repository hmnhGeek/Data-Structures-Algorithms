// Problem link - https://www.geeksforgeeks.org/problems/alien-dictionary/1
// Solution - https://www.youtube.com/watch?v=U3N_je7tWAs&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=26


package Graphs.G26;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static <T> List<T> getTopologicalSort(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = getIndegrees(graph);
        Queue<T> queue = new Queue<>();
        List<T> result = new ArrayList<>();
        for (T node : indegrees.keySet()) {
            if (indegrees.get(node).equals(0)) {
                queue.push(node);
            }
        }
        while (!queue.isEmpty()) {
            T node = queue.pop();
            result.add(node);
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) - 1);
                if (indegrees.get(adjNode).equals(0)) {
                    queue.push(adjNode);
                }
            }
        }
        return result;
    }

    private static <T> Map<T, Integer> getIndegrees(Map<T, List<T>> graph) {
        Map<T, Integer> indegrees = new HashMap<>();
        for (T node : graph.keySet()) {
            indegrees.put(node, 0);
        }
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                indegrees.put(adjNode, indegrees.get(adjNode) + 1);
            }
        }
        return indegrees;
    }

    public static List<Character> getAlienDictionary(List<String> words) {
        /*
            Time complexity is O(V + E) and space complexity is O(V + E).
         */
        Map<Character, List<Character>> graph = getGraph(words);
        List<Character> topologicalSort = getTopologicalSort(graph);
        if (topologicalSort.size() == graph.size()) {
            return topologicalSort;
        }
        return new ArrayList<>();
    }

    private static Map<Character, List<Character>> getGraph(List<String> words) {
        Map<Character, List<Character>> graph = new HashMap<>();
        for (String word : words) {
            for (Character character : word.toCharArray()) {
                graph.putIfAbsent(character, new ArrayList<>());
            }
        }
        for (int i = 0; i < words.size() - 1; i += 1) {
            String first = words.get(i);
            String second = words.get(i + 1);
            int minLength = Math.min(first.length(), second.length());
            for (int j = 0; j < minLength; j += 1) {
                if (first.charAt(j) != second.charAt(j)) {
                    graph.get(first.charAt(j)).add(second.charAt(j));
                    break;
                }
            }
        }
        return graph;
    }

    public static void main(String[] args) {

        System.out.println(Solution.getAlienDictionary(
                List.of("baa","abcd","abca","cab","cad")
        ));

        System.out.println(Solution.getAlienDictionary(
                List.of("caa","aaa","aab")
        ));

        System.out.println(Solution.getAlienDictionary(
                List.of("dhhid", "dahi", "cedg", "fg", "gdah", "i", "gbdei", "hbgf", "e", "ddde")
        ));

        System.out.println(Solution.getAlienDictionary(
                List.of("abc","bat","ade")
        ));

        System.out.println(Solution.getAlienDictionary(
                List.of("a", "aa", "aaa")
        ));

        System.out.println(Solution.getAlienDictionary(List.of("hello", "leetcode")));
    }
}
