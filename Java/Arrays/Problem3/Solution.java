package Arrays.Problem3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class ResultObject<T extends Comparable<T>> {
    private T kthSmallest;
    private T kthLargest;

    public ResultObject(T kthSmallest, T kthLargest) {
        this.kthLargest = kthLargest;
        this.kthSmallest = kthSmallest;
    }

    @Override
    public String toString() {
        return String.format("Kth Smallest = %s, Kth Largest = %s", this.kthSmallest, this.kthLargest);
    }
}

public class Solution {
    public static void main(String[] args) {
        System.out.println(getKths(new ArrayList<>(Arrays.asList(7, 10, 4, 3, 20, 15)), 3));
    }

    private static <T extends Comparable<T>> T getKthSmallest(List<T> arr, Integer k) {
        if (k > arr.size() || k <= 0) return null;
        QuickSort.sort(arr);
        return arr.get(k - 1);
    }

    private static <T extends Comparable<T>> T getKthLargest(List<T> arr, Integer k) {
        if (k > arr.size() || k <= 0) return null;
        MergeSort.sort(arr);
        return arr.get(arr.size() - k);
    }

    public static <T extends Comparable<T>> ResultObject<T> getKths(List<T> arr, Integer k) {
        T kthSmallest = getKthSmallest(arr, k);
        T kthLargest = getKthLargest(arr, k);
        return new ResultObject<>(kthSmallest, kthLargest);
    }
}
