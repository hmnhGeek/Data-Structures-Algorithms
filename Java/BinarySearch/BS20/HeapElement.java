package BinarySearch.BS20;

public class HeapElement implements Comparable<HeapElement> {
    public Double distance;
    public Integer index;
    public Integer placedStationsCount;

    public HeapElement(Double distance, Integer index, Integer placedStationsCount) {
        this.distance = distance;
        this.index = index;
        this.placedStationsCount = placedStationsCount;
    }

    @Override
    public int compareTo(HeapElement o) {
        return this.distance.compareTo(o.distance);
    }

    @Override
    public String toString() {
        return String.format("Distance = %f, Index = %d, Stations = %d", distance, index, placedStationsCount);
    }
}
