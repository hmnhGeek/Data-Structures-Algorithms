package Arrays.Problem27;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Boolean isArraySubset(List<Integer> arr, List<Integer> possibleSubset) {
        Map<Integer, Integer> freqMap = getFreqMap(arr);
        Map<Integer, Integer> subsetMap = getFreqMap(possibleSubset);
        for (Integer i : subsetMap.keySet()) {
            if (!freqMap.containsKey(i)) return false;
            if (subsetMap.get(i) > freqMap.get(i)) return false;
        }
        return true;
    }

    private static Map<Integer, Integer> getFreqMap(List<Integer> arr) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (Integer i : arr) {
            freqMap.put(i, freqMap.getOrDefault(i, 0) + 1);
        }
        return freqMap;
    }

    public static void main(String[] args) {
        System.out.println(isArraySubset(Arrays.asList(11, 7, 1, 13, 21, 3, 7, 3), Arrays.asList(11, 3, 7, 1, 7)));
    }
}
