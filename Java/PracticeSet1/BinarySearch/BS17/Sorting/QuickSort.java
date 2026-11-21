package PracticeSet1.BinarySearch.BS17.Sorting;

import java.util.Collections;
import java.util.List;

public class QuickSort<T extends Comparable<T>> implements Sort<T> {
    @Override
    public void sort(List<T> arr) {
        int n = arr.size();
        sort(arr, 0, n - 1);
    }

    private void sort(List<T> arr, int low, int high) {
        if (low >= high) return;
        int partitionIndex = getPartitionIndex(arr, low, high);
        sort(arr, low, partitionIndex - 1);
        sort(arr, partitionIndex + 1, high);
    }

    private int getPartitionIndex(List<T> arr, int low, int high) {
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
        Collections.swap(arr, j, low);
        return j;
    }
}
