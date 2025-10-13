package SlidingWindows.L2;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMaxPointsFromCards(Arrays.asList(1,2,3,4,5,6,1), 3));
        System.out.println(getMaxPointsFromCards(Arrays.asList(2, 2, 2), 2));
        System.out.println(getMaxPointsFromCards(Arrays.asList(9,7,7,9,7,7,9), 7));
    }

    public static int getMaxPointsFromCards(List<Integer> cards, int k) {
        if (k <= 0) return 0;
        int n = cards.size();
        int i = k - 1;
        int j = n;
        int maxPoints = 0, currentPoints = 0;
        for (int x = 0; x < k; x += 1) {
            currentPoints += cards.get(x);
        }
        maxPoints = currentPoints;
        if (k >= n) return currentPoints;
        while (i >= 0) {
            currentPoints -= cards.get(i);
            i -= 1;
            j -= 1;
            currentPoints += cards.get(j);
            maxPoints = Math.max(maxPoints, currentPoints);
        }
        return maxPoints;
    }
}
