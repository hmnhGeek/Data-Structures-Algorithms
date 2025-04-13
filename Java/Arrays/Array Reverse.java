// Problem link - https://www.geeksforgeeks.org/program-to-reverse-an-array/

package Arrays;


import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Question1 {
    public static void main(String[] args) {
        System.out.println(reverseArray(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(reverseArray(Arrays.asList(1, 2, 3, 4)));
        System.out.println(reverseArray(Arrays.asList(1, 4, 3, 2, 6, 5)));
        System.out.println(reverseArray(Arrays.asList(4, 5, 1, 2)));
    }

    public static List<Integer> reverseArray(List<Integer> array) {
        /**
         * Time complexity is O(n) and space complexity is O(1).
         */

        int n = array.size();
        int i = 0, j = n - 1;

        // while the pointers `i` and `j` follow relative order...
        while (i < j) {
            // swap the indices
            Collections.swap(array, i, j);
            i += 1;
            j -= 1;
        }
        return array;
    }
}