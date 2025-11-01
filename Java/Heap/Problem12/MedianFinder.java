package Heap.Problem12;

public class MedianFinder<T extends Number & Comparable<T>> {
    public MinHeap<T> minHeap;
    public MaxHeap<T> maxHeap;
    public Integer length;

    public MedianFinder() {
        this.minHeap = new MinHeap<>();
        this.maxHeap = new MaxHeap<>();
        this.length = 0;
    }

    public Integer getLength() {
        return length;
    }

    public void insert(T x) {
        if (maxHeap.isEmpty()) {
            maxHeap.push(x);
        } else if (maxHeap.top().compareTo(x) >= 0) {
            maxHeap.push(x);
        } else {
            minHeap.push(x);
        }
        if (maxHeap.getHeap().size() > minHeap.getHeap().size() + 1) {
            minHeap.push(maxHeap.pop());
        }
        if (minHeap.getHeap().size() > maxHeap.getHeap().size()) {
            maxHeap.push(minHeap.pop());
        }
        length = length + 1;
    }

    public double getMedian() {
        if (getLength().equals(0)) {
            return -1;
        }
        if (getLength() % 2 == 0) {
            return (maxHeap.top().doubleValue() + minHeap.top().doubleValue())/2;
        }
        return maxHeap.top().doubleValue();
    }
}
