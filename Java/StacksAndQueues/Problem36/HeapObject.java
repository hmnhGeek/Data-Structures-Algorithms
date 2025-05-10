package StacksAndQueues.Problem36;

public class HeapObject implements Comparable<HeapObject> {
    private Character character;
    private Integer count;

    public HeapObject(Character character, Integer count) {
        this.character = character;
        this.count = count;
    }

    public Character getCharacter() {
        return character;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }

    @Override
    public int compareTo(HeapObject o) {
        return this.count.compareTo(o.getCount());
    }
}
