package PracticeSet1.BinarySearch.BS27;

import java.util.List;

public class Solution {
    public static void main(String[] args) {

    }

    public static Integer getMedian(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        int totalIntegers = n*m;
        MinHeap<Integer> pq = new MinHeap<>();
        for (int i = 0; i < n; i += 1) {
            pq.insert(mtx.get(i).getFirst());
        }
    }
}
