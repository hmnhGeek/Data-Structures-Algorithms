package PracticeSet1.BinarySearch.BS17;

import PracticeSet1.BinarySearch.BS17.Sorting.*;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {

    }

    public static Integer aggressiveCows(List<Integer> arr, Integer cowsCount) {
        if (cowsCount <= 0) return null;
        Sort<Integer> quickSort = new QuickSort<>();
        quickSort.sort(arr);
        int low = 0, high = arr.getLast();
        while (low <= high) {
            int mid = (low + (high - low)/2);
            if (placingAllCowsPossible(arr, mid, cowsCount)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }
}
