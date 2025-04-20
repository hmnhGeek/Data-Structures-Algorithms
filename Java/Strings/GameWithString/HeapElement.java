package Strings.GameWithString;

public class HeapElement implements Comparable<HeapElement> {
    private Integer count;
    private Character character;

    public HeapElement(Character character, Integer count) {
        this.character = character;
        this.count = count;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }

    public Character getCharacter() {
        return character;
    }

    public void setCharacter(Character character) {
        this.character = character;
    }

    @Override
    public int compareTo(HeapElement o) {
        return this.count.compareTo(o.getCount());
    }
}
