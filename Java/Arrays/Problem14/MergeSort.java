package Arrays.Problem14;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeSort {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        sort(arr, 0, arr.size() - 1);
    }

    public static <T extends Comparable<T>> void sort(List<T> arr, int low, int high) {
        if (low >= high) return;
        int mid = (low + (high - low)/2);
        sort(arr, low, mid);
        sort(arr, mid + 1, high);
        List<T> mergeResult = merge(arr, low, high);
        arr.subList(low, high + 1).clear();
        arr.addAll(low, mergeResult);
    }

    private static <T extends Comparable<T>> List<T> merge(List<T> arr, int low, int high) {
        int mid = (low + (high - low)/2);
        List<T> left = arr.subList(low, mid + 1), right = arr.subList(mid + 1, high + 1);
        int i = 0, j = 0;
        List<T> mergeResult = new ArrayList<>();

        while (i < left.size() && j < right.size()) {
            if (left.get(i).compareTo(right.get(j)) <= 0) {
                mergeResult.add(left.get(i));
                 i += 1;
            } else {
                mergeResult.add(right.get(j));
                j += 1;
            }
        }

        while (i < left.size()) {
            mergeResult.add(left.get(i));
            i += 1;
        }

        while (j < right.size()) {
            mergeResult.add(right.get(j));
            j += 1;
        }

        return mergeResult;
    }
}
