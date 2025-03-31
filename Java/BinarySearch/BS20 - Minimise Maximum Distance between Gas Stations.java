package BinarySearch;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Utility {
    public static <T> List<T> getList(Integer size, T defaultValue) {
        List<T> list = new ArrayList<>();
        for (int i = 0; i < size; i += 1) {
            list.add(defaultValue);
        }
        return list;
    }
}

class LinearSolution {
    public static Double getMinimizedMaxDistance(List<Integer> arr, Integer k) {
        /**
         * Time complexity is O(nk) and space complexity is O(n).
         */

        int n = arr.size();
        
        // get the list of slots in O(n) time and O(n) space.
        List<Integer> slots = Utility.getList(n - 1, 0);
        
        // loop on the `k` gas stations that needs to be placed in k iterations.
        for (int i = 0; i < k; i += 1) {
            // store the max slot length and index based on the current state of the slots.
            int maxSlotIndex = -1;
            double maxSlotLength = 0.0;
            
            // loop on the existing gas stations in `n - 1` iterations.
            for (int j = 0; j < n - 1; j += 1) {
                // compute the slot length of each slot and update the max slot length and index. Basically, this inner
                // loop is trying to find the maximum slot where the next gas station can be placed.
                int left = arr.get(j);
                int right = arr.get(j + 1);
                double slotLength = (right - left)/((double) slots.get(j) + 1.0);
                if (maxSlotLength < slotLength) {
                    maxSlotLength = slotLength;
                    maxSlotIndex = j;
                }
            }

            // once the largest slot is found, put the next gas station there.
            slots.set(maxSlotIndex, slots.get(maxSlotIndex) + 1);
        }

        // finally, again find the max slot length which would point to the minimized maximum length between any two gas
        // stations. This is our final answer and this takes O(n) time.
        double maxSlotLength = 0;
        for (int j = 0; j < n - 1; j += 1) {
            int left = arr.get(j);
            int right = arr.get(j + 1);
            double slotLength = (right - left)/((double) slots.get(j) + 1.0);
            if (maxSlotLength < slotLength) {
                maxSlotLength = slotLength;
            }
        }
        return maxSlotLength;
    }
}


class Slot implements Comparable<Slot> {
    private Double length;
    private Integer gasStationsPlaced;

    public Slot(Double length, Integer gasStationsPlaced) {
        this.length = length;
        this.gasStationsPlaced = gasStationsPlaced;
    }

    public Double getLength() {
        return length;
    }

    public void setLength(Double length) {
        this.length = length;
    }

    public Integer getGasStationsPlaced() {
        return gasStationsPlaced;
    }

    public void setGasStationsPlaced(Integer gasStationsPlaced) {
        this.gasStationsPlaced = gasStationsPlaced;
    }


    @Override
    public int compareTo(Slot o) {
        if (this.length - o.getLength() < 0) {
            return -1;
        } else if (this.length - o.getLength()  == 0) {
            return 0;
        } else {
            return  1;
        }
    }

    @Override
    public String toString() {
        return String.format("Slot length = %s, Gas stations placed = %d", getLength(), getGasStationsPlaced());
    }
}

class MaxHeap<T extends Comparable<T>> {
    private List<T> heap;

    public MaxHeap() {
        this.heap = new ArrayList<>();
    }

    public boolean isEmpty() {
        return heap.isEmpty();
    }

    public Integer getLci(int pi) {
        int lci = 2*pi + 1;
        return 0 <= lci && lci < heap.size() ? lci : null;
    }

    public Integer getRci(int pi) {
        int rci = 2*pi + 2;
        return 0 <= rci && rci < heap.size() ? rci : null;
    }

    public Integer getPi(int ci) {
        if (ci == 0) {
            return null;
        }
        int pi = (ci - 1)/2;
        return 0 <= pi && pi < heap.size() ? pi : null;
    }

    public Integer getMaxChildIndex(Integer lci, Integer rci) {
        if (lci == null && rci == null) {
            return null;
        }
        if (lci == null) {
            return rci;
        }
        if (rci == null) {
            return lci;
        }
        Integer maxChildIndex = lci;
        if (heap.get(rci).compareTo(heap.get(maxChildIndex)) > 0) {
            maxChildIndex = rci;
        }
        return maxChildIndex;
    }

    public void maxHeapifyUp(Integer startIndex) {
        if (startIndex.equals(0)) {
            return;
        }
        Integer pi = getPi(startIndex);
        Integer lci = getLci(pi);
        Integer rci = getRci(pi);
        Integer maxChildIndex = getMaxChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (heap.get(pi).compareTo(heap.get(maxChildIndex)) < 0) {
                Collections.swap(heap, pi, maxChildIndex);
            }
            maxHeapifyUp(pi);
        }
    }

    public void maxHeapifyDown(Integer pi) {
        Integer lci = getLci(pi);
        Integer rci = getRci(pi);
        Integer maxChildIndex = getMaxChildIndex(lci, rci);
        if (maxChildIndex != null) {
            if (heap.get(pi).compareTo(heap.get(maxChildIndex)) < 0) {
                Collections.swap(heap, pi, maxChildIndex);
            }
            maxHeapifyDown(maxChildIndex);
        }
    }

    public void insert(T x) {
        heap.add(x);
        maxHeapifyUp(heap.size() - 1);
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = heap.getFirst();
        Collections.swap(heap, 0, heap.size() - 1);
        heap.removeLast();
        maxHeapifyDown(0);
        return item;
    }
}

class BetterSolution {
    public static Double getMinimizedMaxDistance(List<Integer> arr, Integer k) {
        MaxHeap<Slot> maxHeap = new MaxHeap<>();
        List<Slot> slots = new ArrayList<>();
        for (int i = 0; i < arr.size() - 1; i += 1) {
            slots.add(new Slot((double) (arr.get(i + 1) - arr.get(i)), 0));
        }
        slots.forEach(maxHeap::insert);
        for (int i = 0; i < k; i += 1) {
            Slot maxSlot = maxHeap.pop();
            double length = maxSlot.getLength();
            int gasStationsPlaced = maxSlot.getGasStationsPlaced();
            double slotLength = length * (gasStationsPlaced + 1);
            double newSlotLength = slotLength/(gasStationsPlaced + 1.0 + 1.0);
            maxHeap.insert(new Slot(newSlotLength, gasStationsPlaced + 1));
        }
        Slot minimizedMaxSlot = maxHeap.pop();
        return minimizedMaxSlot.getLength();
    }
}


class Solution {
    public static void main(String[] args) {
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1, 13, 17, 23), 5));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1,2,3,4,5,6,7), 6));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1, 2, 3, 4, 5), 4));
        System.out.println(LinearSolution.getMinimizedMaxDistance(IntStream.range(1, 11).boxed().toList(), 1));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(3, 6, 12, 19, 33, 44, 67, 72, 89, 95), 2));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1, 13, 17, 23), 5));

        System.out.println();
        System.out.println(BetterSolution.getMinimizedMaxDistance(Arrays.asList(1, 13, 17, 23), 5));
        System.out.println(BetterSolution.getMinimizedMaxDistance(Arrays.asList(1,2,3,4,5,6,7), 6));
        System.out.println(BetterSolution.getMinimizedMaxDistance(Arrays.asList(1, 2, 3, 4, 5), 4));
        System.out.println(BetterSolution.getMinimizedMaxDistance(IntStream.range(1, 11).boxed().toList(), 1));
        System.out.println(BetterSolution.getMinimizedMaxDistance(Arrays.asList(3, 6, 12, 19, 33, 44, 67, 72, 89, 95), 2));
        System.out.println(BetterSolution.getMinimizedMaxDistance(Arrays.asList(1, 13, 17, 23), 5));
    }
}