package Heap.Problem17;

public class HeapElement implements Comparable<HeapElement> {
    public Character character;
    public Integer count;

    public HeapElement(Character character, Integer count) {
        this.character = character;
        this.count = count;
    }

    @Override
    public int compareTo(HeapElement o) {
        return this.count.compareTo(o.count);
    }
}
