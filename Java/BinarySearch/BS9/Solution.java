package BinarySearch.BS9;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(Solution.getPeakElement(List.of(1, 5, 1, 2, 1)));
        System.out.println(Solution.getPeakElement(List.of(1, 8, 1, 5, 3)));
        System.out.println(Solution.getPeakElement(List.of(1, 2, 1)));
        System.out.println(Solution.getPeakElement(List.of(1, 2, 3, 1)));
        System.out.println(Solution.getPeakElement(List.of(1, 2, 1, 3, 5, 6, 4)));
        System.out.println(Solution.getPeakElement(List.of(1, 2, 4, 5, 7, 8, 3)));
        System.out.println(Solution.getPeakElement(List.of(10, 20, 15, 2, 23, 90, 80)));
        System.out.println(Solution.getPeakElement(List.of(1, 2, 3)));
    }

    public static Integer getPeakElement(List<Integer> arr) {
        int n = arr.size();
        if (n == 1) return arr.getFirst();

        if (arr.getFirst() > arr.get(1)) return arr.getFirst();
        if (arr.getLast() > arr.get(n - 2)) return arr.getLast();

        int low = 1, high = n - 2;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            Integer elem = arr.get(mid);

            if (arr.get(mid - 1) < elem && elem > arr.get(mid + 1)) {
                return elem;
            }
            if (arr.get(mid - 1) < elem && elem < arr.get(mid + 1)) {
                low = mid + 1;
            } else if (arr.get(mid - 1) > elem && elem > arr.get(mid + 1)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }
}
