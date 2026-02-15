package BinarySearch.BS20;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(placeGasStations(Arrays.asList(1,2,3,4,5,6,7), 6));
        System.out.println(placeGasStations(Arrays.asList(1,2,3,4,5), 4));
        System.out.println(placeGasStations(Arrays.asList(1,2,3,4,5,6,7,8,9,10), 1));
        System.out.println(placeGasStations(Arrays.asList(3, 6, 12, 19, 33, 44, 67, 72, 89, 95), 2));
        System.out.println(placeGasStations(Arrays.asList(1, 13, 17, 23), 5));
    }

    private static Double placeGasStations(List<Integer> coordinates, Integer numStationsToBePlaced) {
        if (numStationsToBePlaced <= 0) return null;
        MaxHeap<HeapElement> maxHeap = new MaxHeap<>();
        populateMaxHeap(maxHeap, coordinates, coordinates.size());
        while (numStationsToBePlaced != 0) {
            HeapElement heapElement = maxHeap.pop();
            HeapElement nextElement = new HeapElement(
                    (heapElement.distance * (heapElement.placedStationsCount + 1)) /(heapElement.placedStationsCount + 2.0),
                    heapElement.index,
                    heapElement.placedStationsCount + 1
            );
            maxHeap.insert(nextElement);
            numStationsToBePlaced -= 1;
        }
        return maxHeap.pop().distance;
    }

    private static void populateMaxHeap(MaxHeap<HeapElement> maxHeap, List<Integer> coordinates, int size) {
        for (int i = 0; i < size - 1; i += 1) {
            maxHeap.insert(new HeapElement((double) (coordinates.get(i + 1) - coordinates.get(i)), i, 0));
        }
    }
}
