package Matrix.Problem5;

import java.util.Collections;
import java.util.List;

public class QuickSort {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        int n = arr.size();
        sort(arr, 0, n - 1);
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, Integer low, Integer high) {
        if (low >= high) return;
        Integer partitionIndex = getPartitionIndex(arr, low, high);
        sort(arr, low, partitionIndex - 1);
        sort(arr, partitionIndex + 1, high);
    }

    private static <T extends Comparable<T>> Integer getPartitionIndex(List<T> arr, Integer low, Integer high) {
        Integer i = low, j = high;
        T pivot = arr.get(low);
        while (i < j) {
            while (arr.get(i).compareTo(pivot) <= 0 && i <= high - 1) {
                i += 1;
            }
            while (arr.get(j).compareTo(pivot) > 0 && j >= low + 1) {
                j -= 1;
            }
            if (i < j) {
                Collections.swap(arr, i, j);
            }
        }
        Collections.swap(arr, low, j);
        return j;
    }
}
