// Problem link - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

package Arrays.Problem6;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static Integer union(List<Integer> a1, List<Integer> a2) {
        /*
            Time complexity is O(n + m) and space complexity is O(n + m).
         */
        Set<Integer> set = new HashSet<>();
        set.addAll(a1);
        set.addAll(a2);
        return set.size();
    }

    public static void main(String[] args) {
        System.out.println(union(Arrays.asList(1, 2, 3, 4, 5), Arrays.asList(1, 2, 3)));
        System.out.println(union(Arrays.asList(85, 25, 1, 32, 54, 6), Arrays.asList(85, 2)));
        System.out.println(union(Arrays.asList(1, 2, 1, 1, 2), Arrays.asList(2, 2, 1, 2, 1)));
    }
}
