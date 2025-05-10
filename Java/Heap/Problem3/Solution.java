package Heap.Problem3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class HeapObject implements Comparable<HeapObject> {
    private Integer element;
    private Integer index;

    public HeapObject(Integer element, Integer index) {
        this.element = element;
        this.index = index;
    }

    public Integer getElement() {
        return element;
    }

    public Integer getIndex() {
        return index;
    }

    @Override
    public int compareTo(HeapObject o) {
        return this.element.compareTo(o.getElement());
    }
}

public class Solution {
    private static List<Integer> getSlidingWindowMaximum(List<Integer> arr, Integer k) {
        if (k <= 0 || k > arr.size()) return null;
        MaxHeap<HeapObject> maxHeap = new MaxHeap<>();
        List<Integer> result = new ArrayList<>();
        int n = arr.size();
        for (int i = 0; i < n; i += 1) {
            maxHeap.insert(new HeapObject(arr.get(i), i));
            while (maxHeap.getHeap().getFirst().getIndex() <= i - k) {
                maxHeap.pop();
            }
            if (i >= k - 1) {
                result.add(maxHeap.getHeap().getFirst().getElement());
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 2, 3, 1, 4, 5, 2, 3, 6), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(5, 1, 3, 4, 2, 6), 1));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 3, 2, 1, 7, 3), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 3, -1, -3, 5, 3, 6, 7), 3));
    }
}
