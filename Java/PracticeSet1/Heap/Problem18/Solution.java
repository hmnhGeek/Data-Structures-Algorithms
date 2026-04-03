package PracticeSet1.Heap.Problem18;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getMinimumSum(Arrays.asList(6, 8, 4, 5, 2, 3)));
        System.out.println(getMinimumSum(Arrays.asList(5, 3, 0, 7, 4)));
        System.out.println(getMinimumSum(Arrays.asList(9, 4)));
    }

    private static Integer getNumFromDigit(Integer n, Integer p) {
        return n * 10 + p;
    }

    public static String getMinimumSum(List<Integer> arr) {
        MinHeap<Integer> pq = new MinHeap<>(arr);
        Integer n1 = 0, n2 = 0;
        boolean addToFirst = true;
        while (!pq.isEmpty()) {
            Integer minDigit = pq.pop();
            if (addToFirst) {
                n1 = getNumFromDigit(n1, minDigit);
            } else {
                n2 = getNumFromDigit(n2, minDigit);
            }
            addToFirst = !addToFirst;
        }
        Integer sum = n1 + n2;
        return sum.toString();
    }
}
