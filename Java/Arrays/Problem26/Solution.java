package Arrays.Problem26;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(10, 22, 5, 75, 65, 80)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(100, 30, 15, 10, 8, 25, 80)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(90, 80, 70, 60, 50)));
    }

    public static void main(String[] args) {
        recursive();
    }
}
