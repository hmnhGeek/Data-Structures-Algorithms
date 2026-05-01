// Problem link - https://www.geeksforgeeks.org/minimum-steps-to-reach-end-from-start-by-performing-multiplication-and-mod-operations-with-array-elements/
// Solution - https://www.youtube.com/watch?v=_BvEJ3VIDWw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=39


package Graphs.G39;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static final Integer BASE = 100000;
    public static Integer getMinStepsToReachEnd(Integer start, List<Integer> arr, Integer end) {
        Queue<HeapElement> queue = new Queue<>();
        queue.push(new HeapElement(0, start));
        Map<Integer, Integer> distances = new HashMap<>();
        for (int i = 0; i < BASE; i += 1) {
            distances.put(i, Integer.MAX_VALUE);
        }
        distances.put(start, 0);
        while (!queue.isEmpty()) {
            HeapElement heapElement = queue.pop();
            Integer stepsTillNow = heapElement.steps, node = heapElement.data;
            if (node.equals(end)) return stepsTillNow;
            for (Integer i : arr) {
                Integer adjNode = (node * i) % BASE;
                if (distances.get(adjNode).compareTo(stepsTillNow + 1) > 0) {
                    distances.put(adjNode, stepsTillNow + 1);
                    queue.push(new HeapElement(stepsTillNow + 1, adjNode));
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(getMinStepsToReachEnd(3, Arrays.asList(2, 5, 7), 30));
        System.out.println(getMinStepsToReachEnd(7, Arrays.asList(3, 4, 65), 66175));
    }
}
