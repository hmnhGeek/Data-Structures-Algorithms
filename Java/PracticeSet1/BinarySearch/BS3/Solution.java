package PracticeSet1.BinarySearch.BS3;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getFirstOccurrence(List<Integer> arr, Integer x) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) < x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return 0 <= low && low < arr.size() ? low : null;
    }

    public static Integer getLastOccurrence(List<Integer> arr, Integer x) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (arr.get(mid) <= x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return 0 <= high && high < arr.size() ? high : null;
    }

    public static List<Integer> getOccurrences(List<Integer> arr, Integer x) {
        Integer first = getFirstOccurrence(arr, x);
        Integer last = getLastOccurrence(arr, x);
        if (arr.get(first) == arr.get(last) && arr.get(first) == x) {
            return List.of(first, last);
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(getOccurrences(Arrays.asList(2, 4, 6, 8, 8, 8, 11, 13), 8));
        System.out.println(getOccurrences(Arrays.asList(0, 1, 1, 5), 1));
        System.out.println(getOccurrences(Arrays.asList(0, 0, 1, 1, 2, 2, 2, 2), 2));
        System.out.println(getOccurrences(Arrays.asList(1, 3, 3, 5), 2));
    }
}
