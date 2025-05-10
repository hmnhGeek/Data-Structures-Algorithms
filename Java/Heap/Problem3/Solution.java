package Heap.Problem3;

class HeapObject implements Comparable<HeapObject> {
    private Integer element;
    private Integer index;

    public HeapObject(Integer element, Integer index) {
        this.element = element;
        this.index = index;
    }

    public Integer getElement() {
        return element;
    }

    public Integer getIndex() {
        return index;
    }

    @Override
    public int compareTo(HeapObject o) {
        return this.element.compareTo(o.getElement());
    }
}

public class Solution {
}
