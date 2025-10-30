package Strings.Problem10;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<String> getAllSubsequences(String string) {
        List<String> result = new ArrayList<>();
        solve(string, string.length() - 1, new ArrayList<>(), result);
        return result;
    }

    private static void solve(String string, int i, List<String> temp, List<String> result) {
        if(i < 0) {
            result.add(String.join("", temp));
            return;
        }
        temp.addFirst(String.valueOf(string.charAt(i)));
        solve(string, i - 1, temp, result);
        temp.removeFirst();
        solve(string, i - 1, temp, result);
    }

    public static void main(String[] args) {
        System.out.println(getAllSubsequences("ab"));
        System.out.println(getAllSubsequences("geeks"));
    }
}
