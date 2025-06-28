package Heap.Problem6;

public class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    private T data;
    private Integer rowIndex;
    private Integer colIndex;

    public HeapElement(T data, Integer rowIndex, Integer colIndex) {
        this.data = data;
        this.rowIndex = rowIndex;
        this.colIndex = colIndex;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Integer getRowIndex() {
        return rowIndex;
    }

    public void setRowIndex(Integer rowIndex) {
        this.rowIndex = rowIndex;
    }

    public Integer getColIndex() {
        return colIndex;
    }

    public void setColIndex(Integer colIndex) {
        this.colIndex = colIndex;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.data.compareTo(o.getData());
    }
}
