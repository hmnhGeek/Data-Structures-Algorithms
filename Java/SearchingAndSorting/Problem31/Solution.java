package SearchingAndSorting.Problem31;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer minTimeToCook(Integer p, List<Integer> cooks) {
        int low = 0, high = 100000000;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            boolean canCook = isCookingPossible(cooks, p, mid);
            if (canCook) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static boolean isCookingPossible(List<Integer> cooks, Integer p, int mid) {
        Integer pCooked = 0;
        for (int i = 0; i < cooks.size(); i += 1) {
            Integer cook = cooks.get(i);
            int time = cook;
            int j = 2;
            while (time <= mid) {
                pCooked += 1;
                time += (cook * j);
                j += 1;
            }
            if (pCooked >= p) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(minTimeToCook(10, Arrays.asList(1, 2, 3, 4)));
        System.out.println(minTimeToCook(8, Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1)));
        System.out.println(minTimeToCook(8, List.of(1)));
    }
}
