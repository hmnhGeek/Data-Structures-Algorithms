package Arrays.Problem16;

import java.util.ArrayList;
import java.util.List;


class InversionCounter {
    public Integer count;

    public InversionCounter(Integer count) {
        this.count = count;
    }
}


public class MergeSort {
    public static <T extends Comparable<T>> Integer getInversionCount(List<T> arr) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        int n = arr.size();
        InversionCounter inversionCounter = new InversionCounter(0);
        sort(arr, 0, n - 1, inversionCounter);
        return inversionCounter.count;
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, int low, int high, InversionCounter inversionCounter) {
        if (low >= high) return;
        int mid = (low + (high - low)/2);
        sort(arr, low, mid, inversionCounter);
        sort(arr, mid + 1, high, inversionCounter);
        List<T> merged = merge(arr, low, high, inversionCounter);
        int counter = 0;
        for (int i = low; i <= high; i += 1) {
            arr.set(i, merged.get(counter));
            counter += 1;
        }
    }

    private static <T extends Comparable<T>> List<T> merge(List<T> arr, int low, int high, InversionCounter inversionCounter) {
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
                inversionCounter.count += (left.size() - i);
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
