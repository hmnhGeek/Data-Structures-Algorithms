// Problem link -

package SearchingAndSorting.Problem5;

public class Solution {
    public static Integer findMiddleElement(int a, int b, int c) {
        /*
            Time complexity is O(1) and space complexity is O(1).
         */
        Integer minVal = Math.min(Math.min(a, b), c);
        Integer maxVal = Math.max(Math.max(a, b), c);
        return a + b + c - maxVal -  minVal;
    }

    public static void main(String[] args) {
        System.out.println(findMiddleElement(978, 518, 300));
        System.out.println(findMiddleElement(162, 934, 200));
        System.out.println(findMiddleElement(246, 214, 450));
    }
}
