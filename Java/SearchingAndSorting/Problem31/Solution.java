// Problem link - https://www.spoj.com/problems/PRATA/
// Solution - https://www.youtube.com/watch?v=-Nx1h54KzUQ


package SearchingAndSorting.Problem31;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer minTimeToCook(Integer p, List<Integer> cooks) {
        /*
            Time complexity is O(L * log(p)) and space complexity is O(1).
         */

        // search space for time, of the order O(p^2).
        int low = 0, high = 100000000;

        // typical binary search
        while (low <= high) {
            // possible time to cook all.
            int mid = (low + (high - low)/2);

            // check if in mid-time can all the parathas be cooked or not.
            boolean canCook = isCookingPossible(cooks, p, mid);

            // if they can be cooked, then try for even lower time.
            if (canCook) {
                high = mid - 1;
            } else {
                // else look for more time to cook.
                low = mid + 1;
            }
        }

        // low points to the correct time.
        return low;
    }

    private static boolean isCookingPossible(List<Integer> cooks, Integer p, int mid) {
        // track the number of parathas cooked.
        Integer pCooked = 0;

        // loop on all the cooks.
        for (int i = 0; i < cooks.size(); i += 1) {
            Integer cook = cooks.get(i);

            // for the first paratha, store the time taken by the ith cook.
            int time = cook;
            int j = 2;

            // while you're within the time limit.
            while (time <= mid) {
                // increment the cooked count
                pCooked += 1;

                // increment time for the next paratha
                time += (cook * j);

                // increment j for GP effect.
                j += 1;
            }

            // if the cooked amount has exceeded the required amount, return true.
            if (pCooked >= p) return true;
        }

        // else return false.
        return false;
    }

    public static void main(String[] args) {
        System.out.println(minTimeToCook(10, Arrays.asList(1, 2, 3, 4)));
        System.out.println(minTimeToCook(8, Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1)));
        System.out.println(minTimeToCook(8, List.of(1)));
    }
}
