package SearchingAndSorting.Problem28;

class Solution {
    public static void main(String[] args) {
        System.out.println(arithmeticNumber(1, 3, 2));
        System.out.println(arithmeticNumber(1, 2, 3));
        System.out.println(arithmeticNumber(1, 2, 4));
    }

    private static boolean arithmeticNumber(Integer a, Integer b, Integer c) {
        double lhs = (double) (b - a) /c;
        return lhs == (int) lhs;
    }
}