// Problem link - https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
// Solution - https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10


package PracticeSet1.BinarySearch.BS9;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(findPeak(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 5, 1)));
        System.out.println(findPeak(List.of(1, 5, 1, 2, 1)));
        System.out.println(findPeak(List.of(1, 8, 1, 5, 3)));
        System.out.println(findPeak(List.of(1, 2, 1)));
        System.out.println(findPeak(List.of(1, 2, 3, 1)));
        System.out.println(findPeak(List.of(1, 2, 1, 3, 5, 6, 4)));
        System.out.println(findPeak(List.of(1, 2, 4, 5, 7, 8, 3)));
        System.out.println(findPeak(List.of(10, 20, 15, 2, 23, 90, 80)));
        System.out.println(findPeak(List.of(1, 2, 3)));
    }

    public static <T extends Comparable<T>> T findPeak(List<T> arr) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int n = arr.size();
        if (n == 0) return null;
        if (n == 1) return arr.getFirst();
        if (arr.getFirst().compareTo(arr.get(1)) > 0) return arr.getFirst();
        if (arr.getLast().compareTo(arr.get(n - 2)) > 0) return arr.getLast();
        int low = 1, high = n - 2;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            T element = arr.get(mid);
            if (arr.get(mid - 1).compareTo(element) < 0 && element.compareTo(arr.get(mid + 1)) > 0) {
                return element;
            }
            if (arr.get(mid - 1).compareTo(element) < 0 && element.compareTo(arr.get(mid + 1)) < 0) {
                low = mid + 1;
            } else if (arr.get(mid - 1).compareTo(element) > 0 && element.compareTo(arr.get(mid + 1)) > 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return null;
    }
}
