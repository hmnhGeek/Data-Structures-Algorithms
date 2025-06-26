package Arrays.Problem6;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static Integer union(List<Integer> a1, List<Integer> a2) {
        Set<Integer> set = new HashSet<>();
        set.addAll(a1);
        set.addAll(a2);
        return set.size();
    }

    public static void main(String[] args) {
        System.out.println(union(Arrays.asList(1, 2, 3, 4, 5), Arrays.asList(1, 2, 3)));
    }
}
