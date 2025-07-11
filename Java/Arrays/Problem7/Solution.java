package Arrays.Problem7;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        List<Integer> arr1 = Arrays.asList(1, 2, 3, 4, 5);
        rotateArray(arr1);
        System.out.println(arr1);

        // Example 2
        List<Integer> arr2 = Arrays.asList(9, 8, 7, 6, 4, 2, 1, 3);
        rotateArray(arr2);
        System.out.println(arr2);
    }

    public static <T> void rotateArray(List<T> array) {
        T lastItem = array.getLast();
        int i = 1;
        int n = array.size();
        T prev = array.getFirst();
        while (i < n) {
            T currItem = array.get(i);
            array.set(i, prev);
            prev = currItem;
            i += 1;
        }
        array.set(0, lastItem);
    }
}
