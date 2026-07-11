// Problem link - https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1


package PracticeSet1.Matrix.Problem3;


import java.util.Arrays;
import java.util.List;


class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    public Integer data;
    public Integer i, j;

    public HeapElement(Integer data, Integer i, Integer j) {
        this.data = data;
        this.i = i;
        this.j = j;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.data.compareTo(o.data);
    }
}


public class Solution {
    public static void main(String[] args) {
        // Example 1
        System.out.println(
                getMedianFromMatrix(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5),
                                Arrays.asList(2, 6, 9),
                                Arrays.asList(3, 6, 9)
                        )
                )
        );

        // Example 2
        System.out.println(
                getMedianFromMatrix(
                        Arrays.asList(
                                Arrays.asList(1),
                                Arrays.asList(2),
                                Arrays.asList(3)
                        )
                )
        );

        // Example 3
        System.out.println(
                getMedianFromMatrix(
                        Arrays.asList(
                                Arrays.asList(3),
                                Arrays.asList(5),
                                Arrays.asList(8)
                        )
                )
        );
    }

    public static Integer getMedianFromMatrix(List<List<Integer>> mtx) {
        /*
            Time complexity is O(nm * log(n)) and space complexity is O(n).
         */

        int n = mtx.size(), m = mtx.getFirst().size();
        int counterLimit = (n*m/2) + 1;
        int counter = 0;
        MinHeap<HeapElement<Integer>> pq = new MinHeap<>();

        for (int i = 0; i < n; i += 1) {
            pq.insert(new HeapElement<>(mtx.get(i).getFirst(), i, 0));
        }

        while (!pq.isEmpty()) {
            HeapElement<Integer> he = pq.pop();
            counter += 1;
            if (counter == counterLimit) return he.data;
            int j = he.j;
            if (0 <= j + 1 && j + 1 < m) {
                pq.insert(new HeapElement<>(mtx.get(he.i).get(j + 1), he.i, j + 1));
            }
        }

        return null;
    }
}
