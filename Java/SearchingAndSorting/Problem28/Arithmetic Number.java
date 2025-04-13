// Problem link - https://www.geeksforgeeks.org/problems/arithmetic-number2815/1

package SearchingAndSorting.Problem28;

class Solution {
    public static void main(String[] args) {
        System.out.println(arithmeticNumber(1, 3, 2));
        System.out.println(arithmeticNumber(1, 2, 3));
        System.out.println(arithmeticNumber(1, 2, 4));
    }

    private static boolean arithmeticNumber(Integer a, Integer b, Integer c) {
        /**
         * Time complexity is O(1) and space complexity is O(1).
         */

        double lhs = (double) (b - a) /c;
        return lhs == (int) lhs;
    }
}