package Arrays.Problem17;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMaxProfit(Arrays.asList(7,1,5,3,6,4)));
        System.out.println(getMaxProfit(Arrays.asList(7,6,4,3,1)));
        System.out.println(getMaxProfit(Arrays.asList(7, 10, 1, 3, 6, 9, 2)));
        System.out.println(getMaxProfit(Arrays.asList(1, 3, 6, 9, 11)));
        System.out.println(getMaxProfit(Arrays.asList(2, 100, 150, 120)));
        System.out.println(getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(getMaxProfit(Arrays.asList(17, 20, 11, 9, 12, 6)));
        System.out.println(getMaxProfit(Arrays.asList(98, 101, 66, 72)));
    }

    public static Integer getMaxProfit(List<Integer> arr) {
        int mini = arr.getFirst();
        int maxProfit = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            int profit = arr.get(i) - mini;
            maxProfit = Math.max(maxProfit, profit);
            mini = Math.min(mini, arr.get(i));
        }
        return maxProfit;
    }
}
