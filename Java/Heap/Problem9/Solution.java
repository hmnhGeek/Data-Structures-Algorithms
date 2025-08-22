package Heap.Problem9;


class HeapElement implements Comparable<HeapElement> {
    private Character character;
    private Integer count;

    public HeapElement(Character character, Integer count) {
        this.character = character;
        this.count = count;
    }

    public Character getCharacter() {
        return character;
    }

    public void setCharacter(Character character) {
        this.character = character;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }

    @Override
    public int compareTo(HeapElement o) {
        return this.count.compareTo(o.getCount());
    }
}


public class Solution {

}
