package Greedy.GD1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class MinHeap<T extends Comparable<T>> implements Heap<T> {
    private List<T> heap;

    public MinHeap() {
        this.heap = new ArrayList<>();
    }

    @Override
    public List<T> getHeap() {
        return this.heap;
    }

    @Override
    public Integer getChildIndex(Integer lci, Integer rci) {
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
        if (getHeap().get(rci).compareTo(getHeap().get(minChildIndex)) < 0) {
            minChildIndex = rci;
        }
        return minChildIndex;
    }

    @Override
    public void heapifyUp(Integer startIndex) {
        if (startIndex.equals(0)) return;
        int pi = getPi(startIndex);
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (getHeap().get(pi).compareTo(getHeap().get(minChildIndex)) > 0) {
                Collections.swap(getHeap(), pi, minChildIndex);
            }
            heapifyUp(pi);
        }
    }

    @Override
    public void heapifyDown(Integer pi) {
        Integer lci = getLci(pi), rci = getRci(pi);
        Integer minChildIndex = getChildIndex(lci, rci);
        if (minChildIndex != null) {
            if (getHeap().get(pi).compareTo(getHeap().get(minChildIndex)) > 0) {
                Collections.swap(getHeap(), pi, minChildIndex);
            }
            heapifyDown(minChildIndex);
        }
    }
}

class SolutionGD1 {
    public static void main(String[] args) {
        System.out.println(getMinCostToConnectRopes(Arrays.asList(4, 3, 2, 6)));
        System.out.println(getMinCostToConnectRopes(Arrays.asList(4, 2, 7, 6, 9)));
        System.out.println(getMinCostToConnectRopes(List.of(10)));
    }

    public static Integer getMinCostToConnectRopes(List<Integer> ropes) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */

        // create a min heap and push all the `n` ropes into it in O(n * log(n)) time.
        MinHeap<Integer> minHeap = new MinHeap<>();
        ropes.forEach(minHeap::insert);

        // define a cost variable which will store the total cost to connect all the ropes.
        Integer cost = 0;

        // until there is just one rope in the min heap, i.e., it will run for n-iterations...
        while (minHeap.getHeap().size() != 1) {
            // get the first and the second-smallest ropes.
            Integer firstRope = minHeap.pop(), secondRope = minHeap.pop();
            // update the cost.
            cost += (firstRope + secondRope);
            // push back into the min heap in O(n * log(n)) time.
            minHeap.insert(firstRope + secondRope);
        }
        return cost;
    }
}