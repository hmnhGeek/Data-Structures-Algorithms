package BinaryTrees.Problem25;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static boolean checkMirror(List<Integer> tree, List<Integer> mirror) {
        Map<Integer, Stack<Integer>> map = new HashMap<>();

        for (int i = 0; i < tree.size(); i += 2) {
            map.put(tree.get(i), new Stack<>());
        }

        for (int i = 0; i < tree.size(); i += 2) {
            map.get(tree.get(i)).push(tree.get(i + 1));
        }

        for (int i = 0; i < mirror.size(); i += 2) {
            if (map.get(mirror.get(i)).top() != mirror.get(i + 1)) return false;
            map.get(mirror.get(i)).pop();
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(checkMirror(Arrays.asList(1, 2, 1, 3), Arrays.asList(1, 3, 1, 2)));
        System.out.println(checkMirror(Arrays.asList(1, 2, 1, 3), Arrays.asList(1, 2, 1, 3)));
    }
}
