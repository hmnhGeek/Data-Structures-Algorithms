package Arrays.Problem10;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static int minJumps(List<Integer> arr) {
        int maxReach = 0, lastIndex = 0, jumps = 0;
        int n = arr.size();
        if (n == 1) {
            return 0;
        }
        for (int i = 0; i < n; i += 1) {
            maxReach = Math.max(maxReach, i + arr.get(i));
            if (i == lastIndex) {
                if (maxReach == i) {
                    return -1;
                }
                lastIndex = maxReach;
                jumps += 1;
                if (maxReach >= n - 1) {
                    return jumps;
                }
            }
        }
        return jumps;
    }

    public static void main(String[] args) {
        System.out.println(minJumps(Arrays.asList(1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9)));
        System.out.println(minJumps(Arrays.asList(1, 4, 3, 2, 6, 7)));
        System.out.println(minJumps(Arrays.asList(0, 10, 20)));
    }
}
