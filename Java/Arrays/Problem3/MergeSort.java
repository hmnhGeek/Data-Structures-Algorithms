package Arrays.Problem3;

import java.util.ArrayList;
import java.util.List;

public class MergeSort {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        sort(arr, 0, arr.size() - 1);
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, Integer low, Integer high) {
        if (low >= high) return;
        Integer mid = (low + (high - low)/2);
        sort(arr, low, mid);
        sort(arr, mid + 1, high);
        List<T> mergedArray = merge(arr, low, high);
        arr.subList(low, high + 1).clear();
        arr.addAll(low, mergedArray);
    }

    private static <T extends Comparable<T>> List<T> merge(List<T> arr, Integer low, Integer high) {
        Integer mid = (low + (high - low)/2);
        List<T> left = arr.subList(low, mid + 1), right = arr.subList(mid + 1, high + 1);
        int i = 0, j = 0;
        List<T> merged = new ArrayList<>();
        while (i < left.size() && j < right.size()) {
            if (left.get(i).compareTo(right.get(j)) <= 0) {
                merged.add(left.get(i));
                i += 1;
            } else {
                merged.add(right.get(j));
                j += 1;
            }
        }
        while (i < left.size()) {
            merged.add(left.get(i));
            i += 1;
        }
        while (j < right.size()) {
            merged.add(right.get(j));
            j += 1;
        }
        return merged;
    }
}
