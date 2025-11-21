package Strings.Problem11;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class Solution {
    public static List<String> getAllPermutations(String string) {
        int n = string.length();
        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            solve(string, new ArrayList<>(), i, n, result);
        }
        return result;
    }

    private static void solve(String string, List<Integer> curr, int i, int n, List<String> result) {
        if (curr.size() == n) {
            Stream<Integer> integerStream = curr.stream();
            String permutation = getPermutation(integerStream.toList(), string);
            if (!result.contains(permutation)) {
                result.add(permutation);
            }
            return;
        }
        for (int j = 0; j < n; j += 1) {
            if (curr.contains(j)) continue;
            curr.add(j);
            solve(string, curr, j, n, result);
            curr.removeLast();
        }
    }

    private static String getPermutation(List<Integer> list, String string) {
        String resultant = "";
        for (int y : list) {
            resultant += string.charAt(y);
        }
        return resultant;
    }

    public static void main(String[] args) {
        System.out.println(getAllPermutations("ABC"));
        System.out.println(getAllPermutations("AAA"));
        System.out.println(getAllPermutations("ABSG"));
    }
}
