package BinarySearch.BS27;

public class HeapElement implements Comparable<HeapElement> {
    private Integer value;
    private Integer row;
    private Integer col;

    public HeapElement(Integer v, Integer r, Integer c) {
        this.value = v;
        this.row = r;
        this.col = c;
    }

    public Integer getValue() {
        return value;
    }

    public void setValue(Integer value) {
        this.value = value;
    }

    public Integer getRow() {
        return row;
    }

    public void setRow(Integer row) {
        this.row = row;
    }

    public Integer getCol() {
        return col;
    }

    public void setCol(Integer col) {
        this.col = col;
    }

    @Override
    public int compareTo(HeapElement o) {
        return this.value.compareTo(o.getValue());
    }
}
