package Arrays.Problem9;

import java.util.Collections;
import java.util.List;

public class QuickSort {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        QuickSort.sort(arr, 0, arr.size() - 1);
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, int low, int high) {
        if (low >= high) return;
        int partitionIndex = QuickSort.getPartitionIndex(arr, low, high);
        QuickSort.sort(arr, low, partitionIndex - 1);
        QuickSort.sort(arr, partitionIndex + 1, high);
    }

    private static <T extends Comparable<T>> int getPartitionIndex(List<T> arr, int low, int high) {
        T pivot = arr.get(low);
        int i = low, j = high;
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
