package BinarySearch.BS11;

public class Solution {
    public static Integer findNthRoot(Integer x, Integer n) {
        if (n < 0 || x < 0) return -1;
        int low = 0, high = x;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            double midResult = Math.pow(mid, n);
            if (midResult == x) return mid;
            if (midResult > x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(findNthRoot(27, 3));
        System.out.println(findNthRoot(9, 3));
        System.out.println(findNthRoot(625, 4));
    }
}
