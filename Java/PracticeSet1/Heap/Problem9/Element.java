package PracticeSet1.Heap.Problem9;

public class Element implements Comparable<Element> {
    public Character character;
    public Integer count;

    public Element(Character character, Integer count) {
        this.character = character;
        this.count = count;
    }

    @Override
    public int compareTo(Element o) {
        return this.count.compareTo(o.count);
    }
}
