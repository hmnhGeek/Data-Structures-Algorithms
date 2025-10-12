// Problem link - https://www.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1
// Solution - https://youtu.be/0IqFMBatlhU


package Heap.Problem11;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(
                getSmallestRange(
                        Arrays.asList(
                                Arrays.asList(4, 7, 9, 12, 15),
                                Arrays.asList(0, 8, 10, 14, 20),
                                Arrays.asList(6, 12, 16, 30, 50)
                        )
                )
        );

        System.out.println(
                getSmallestRange(
                        Arrays.asList(
                                Arrays.asList(1, 3, 5, 7, 9),
                                Arrays.asList(0, 2, 4, 6, 8),
                                Arrays.asList(2, 3, 5, 7, 11)
                        )
                )
        );

        System.out.println(
                getSmallestRange(
                        Arrays.asList(
                                Arrays.asList(2, 4),
                                Arrays.asList(1, 7),
                                Arrays.asList(20, 40)
                        )
                )
        );
    }

    public static List<Integer> getSmallestRange(List<List<Integer>> lists) {
        /*
            Time complexity is O(n * log(k)) and space complexity is O(k).
         */

        MinHeap<Element<Integer>> minHeap = new MinHeap<>();
        Integer maxElement = Integer.MIN_VALUE;
        Integer minElement = Integer.MAX_VALUE;
        for (int i = 0; i < lists.size(); i += 1) {
            maxElement = Math.max(maxElement, lists.get(i).getFirst());
            minElement = Math.min(minElement, lists.get(i).getFirst());
            minHeap.push(new Element<>(lists.get(i).getFirst(), i, 0));
        }
        List<Integer> result = Arrays.asList(minElement, maxElement);
        while (!minHeap.isEmpty()) {
            Element<Integer> element = minHeap.pop();
            Integer data = element.data;
            result = updateResult(data, maxElement, result);
            Integer listIndex = element.i, idx = element.j;
            if (0 <= idx + 1 && idx + 1 < lists.get(listIndex).size()) {
                minHeap.push(new Element<>(lists.get(listIndex).get(idx + 1), listIndex, idx + 1));
                maxElement = Math.max(maxElement, lists.get(listIndex).get(idx + 1));
            } else {
                break;
            }
        }
        return result;
    }

    private static List<Integer> updateResult(Integer data, Integer maxElement, List<Integer> result) {
        if (maxElement - data < result.getLast() - result.getFirst()) {
            result = Arrays.asList(data, maxElement);
        } else if (maxElement - data == result.getLast() - result.getFirst()) {
            if (data < result.getFirst()) {
                result = Arrays.asList(data, maxElement);
            }
        }
        return result;
    }
}
