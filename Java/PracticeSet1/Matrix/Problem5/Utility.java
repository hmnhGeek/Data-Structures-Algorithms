package PracticeSet1.Matrix.Problem5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Utility {
    public static <T extends Comparable<T>> void quickSort(List<T> arr) {
        int n = arr.size();
        sort(arr, 0, n - 1);
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, int low, int high) {
        if (low >= high) return;
        int partitionIndex = getPartitionIndex(arr, low, high);
        sort(arr, low, partitionIndex - 1);
        sort(arr, partitionIndex + 1, high);
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
        Collections.swap(arr, j, low);
        return j;
    }

    public static <T> List<T> flattenMatrix(List<List<T>> mtx) {
        int n = mtx.size();
        List<T> result = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < n; j += 1) {
                result.add(mtx.get(i).get(j));
            }
        }
        return result;
    }

    public static <T> List<List<T>> rebuildMatrix(List<T> arr, int n) {
        List<List<T>> matrix = new ArrayList<>();
        for (int i = 0; i < n; i += 1) {
            List<T> row = new ArrayList<>();
            for (int j = 0; j < n; j += 1) {
                row.add(arr.get(i*n + j))
            }
            matrix.add(row);
        }
        return matrix;
    }
}
