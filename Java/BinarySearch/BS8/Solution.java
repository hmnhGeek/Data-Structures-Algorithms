// Problem link - https://www.naukri.com/code360/problems/unique-element-in-sorted-array_1112654
// Solution - https://www.youtube.com/watch?v=AZOmHuHadxQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=9


package BinarySearch.BS8;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(Solution.getSingleElement(List.of(3, 3, 7, 7, 10, 11, 11)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 2, 2, 4, 5, 5)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 4, 4, 15)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 3, 5, 5)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8)));
        System.out.println(Solution.getSingleElement(List.of(1, 1, 2, 3, 3, 4, 4, 8, 8)));
    }

    public static Integer getSingleElement(List<Integer> arr) {
        /*
            Time complexity is O(log(n)) and space complexity is O(1).
         */
        int n = arr.size();
        if (n == 1) return arr.getFirst();
        if (arr.getFirst() != arr.get(1)) return arr.getFirst();
        if (arr.getLast() != arr.get(n - 2)) return arr.getLast();
        int low = 1, high = n - 2;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) != arr.get(mid - 1) && arr.get(mid) != arr.get(mid + 1)) return arr.get(mid);
            if (
                    (mid % 2 == 1 && arr.get(mid - 1) == arr.get(mid)) ||
                            (mid % 2 == 0 && arr.get(mid) == arr.get(mid + 1))
            ) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
}
