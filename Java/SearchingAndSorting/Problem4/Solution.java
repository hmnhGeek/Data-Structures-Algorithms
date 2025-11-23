// Problem link - https://www.geeksforgeeks.org/problems/count-squares3649/1

package SearchingAndSorting.Problem4;

public class Solution {
    public static Integer getCount(int n) {
        /*
            Time complexity is O(sqrt(n)) and space complexity is O(1).
         */
        return (int) Math.floor(Math.sqrt(n - 1));
    }

    public static void main(String[] args) {
        System.out.println(getCount(9));
        System.out.println(getCount(3));
    }
}
