package SearchingAndSorting.Problem34;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;


class InversionCounter {
    public Integer count = 0;
}


public class Solution {
    public static void main(String[] args) {
        System.out.println(mergeSort(new ArrayList<>(Arrays.asList(2, 4, 1, 3, 5))));
    }

    private static Integer mergeSort(List<Integer> arr) {
        InversionCounter counter = new InversionCounter();
        mergeSort(arr, 0, arr.size() - 1, counter);
        return counter.count;
    }

    private static void mergeSort(List<Integer> arr, int low, int high, InversionCounter inversionCounter) {
        if (low >= high) return;
        int mid = (low + (high - low)/2);
        mergeSort(arr, low, mid, inversionCounter);
        mergeSort(arr, mid + 1, high, inversionCounter);
        List<Integer> mergedList = merge(arr, low, high, inversionCounter);
        arr.subList(low, high + 1).clear();
        arr.addAll(low, mergedList);
    }

    private static List<Integer> merge(List<Integer> arr, int low, int high, InversionCounter inversionCounter) {
        int mid = (low + (high - low)/2);
        List<Integer> left = arr.subList(low, mid + 1);
        List<Integer> right = arr.subList(mid + 1, high + 1);
        int i = 0, j = 0;
        List<Integer> merged = new ArrayList<>();
        while (i < left.size() && j < right.size()) {
            if (left.get(i) <= right.get(j)) {
                merged.add(left.get(i));
                i += 1;
            } else {
                inversionCounter.count += (left.size() - i);
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
