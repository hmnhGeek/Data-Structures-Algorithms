// Problem link - https://www.geeksforgeeks.org/problems/minimum-sum4058/1

package Heap;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class MinHeap {
    private List<Integer> heap;

    public MinHeap() {
        this.heap = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.heap.isEmpty();
    }

    public Integer getLci(Integer pi) {
        int lci = 2 * pi + 1;
        return (lci >= 0 && lci < this.heap.size()) ? lci : null;
    }

    public Integer getRci(Integer pi) {
        int rci = 2 * pi + 2;
        return (rci >= 0 && rci < this.heap.size()) ? rci : null;
    }

    public Integer getPi(Integer ci) {
        if(ci == 0) {
            return null;
        }
        return (ci - 1)/2;
    }
    
    public Integer getMinChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) {
            return null;
        }
        if (lci == null) {
            return rci;
        }
        if (rci == null) {
            return lci;
        }
        Integer minChildIndex = lci;
        if (this.heap.get(rci) < this.heap.get(minChildIndex)) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    public void minHeapifyUp(Integer startIndex) {
        if (startIndex == 0) {
            return;
        }
        Integer pi = getPi(startIndex);
        Integer lci = getLci(pi);
        Integer rci = getRci(pi);
        Integer minChildIndex = getMinChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (heap.get(pi) > heap.get(minChildIndex)) {
                Collections.swap(heap, pi, minChildIndex);
            }
            minHeapifyUp(pi);
        }
    }

    public void minHeapifyDown(Integer pi) {
        Integer lci = getLci(pi);
        Integer rci = getRci(pi);
        Integer minChildIndex = getMinChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (heap.get(pi) > heap.get(minChildIndex)) {
                Collections.swap(heap, pi, minChildIndex);
            }
            minHeapifyDown(minChildIndex);
        }
    }

    public void insert(Integer x) {
        heap.add(x);
        minHeapifyUp(heap.size() - 1);
    }

    public Integer pop() {
        if (heap.isEmpty()) {
            return null;
        }
        Integer item = heap.getFirst();
        Collections.swap(heap, 0, heap.size() - 1);
        heap.removeLast();
        minHeapifyDown(0);
        return item;
    }
}


class Solution {
    public static void main(String[] args) {
        System.out.println(getMinSum(Arrays.asList(6, 8, 4, 5, 2, 3)));
        System.out.println(getMinSum(Arrays.asList(5, 3, 0, 7, 4)));
        System.out.println(getMinSum(Arrays.asList(9, 4)));
    }

    public static Integer getMinSum(List<Integer> arr) {
        /*
        * Time complexity is O(n * log(n)) and space complexity is O(n).
        * */

        // create a min heap and push all the elements into it in O(n * log(n)) time and O(n) space.
        MinHeap minHeap = new MinHeap();
        arr.forEach(minHeap::insert);

        // initialize two variables to store the numbers formed after the min heap operations.
        int num1 = 0;
        int num2 = 0;

        // while the min heap is not empty. This will run for `n` times.
        while (!minHeap.isEmpty()) {
            // add LSB to the number 1. This will take O(log(n)) time.
            num1 = (num1 * 10) + minHeap.pop();

            // if min heap is still not empty...
            if (!minHeap.isEmpty()) {
                // add LSB to the number 2. This will take O(log(n)) time.
                num2 = (num2 * 10) + minHeap.pop();
            }
        }

        // finally return the sum.
        return num1 + num2;
    }
}