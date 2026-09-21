package PracticeSet1.BinarySearch.BS11;

public class Solution {
    public static Integer findNthRoot(Integer m, Integer n) {
        if (n <= 1) return -1;
        int low = 1, high = m;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            int pow = getIndicator(mid, n, m);
            if (pow == 1) return mid;
            if (pow == 2) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    private static int getIndicator(int mid, Integer n, Integer m) {
        int res = 1;
        for (int i = 0; i < n; i += 1) {
            res = res * mid;
            if (res > m) return 2;
        }
        if (res == m) return 1;
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findNthRoot(27, 3));
        System.out.println(findNthRoot(9, 3));
        System.out.println(findNthRoot(625, 4));
    }
}
