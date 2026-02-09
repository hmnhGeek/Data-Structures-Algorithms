package Arrays.Problem16;

import java.util.ArrayList;
import java.util.List;

public class MergeSort {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        int n = arr.size();
        sort(arr, 0, n - 1);
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, int low, int high) {
        if (low >= high) return;
        int mid = (low + (high - low)/2);
        sort(arr, low, mid);
        sort(arr, mid + 1, high);
        List<T> merged = merge(arr, low, high);
        int counter = 0;
        for (int i = low; i <= high; i += 1) {
            arr.set(i, merged.get(counter));
            counter += 1;
        }
    }

    private static <T extends Comparable<T>> List<T> merge(List<T> arr, int low, int high) {
        int mid = (low + (high - low)/2);
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
