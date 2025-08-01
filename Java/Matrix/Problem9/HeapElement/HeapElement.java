package Matrix.Problem9.HeapElement;

public class HeapElement<T extends Comparable<T>> implements Comparable<HeapElement<T>> {
    private T data;
    private Integer i;
    private Integer j;

    public HeapElement(T data, Integer i, Integer j) {
        this.data = data;
        this.i = i;
        this.j = j;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Integer getI() {
        return i;
    }

    public void setI(Integer i) {
        this.i = i;
    }

    public Integer getJ() {
        return j;
    }

    public void setJ(Integer j) {
        this.j = j;
    }

    @Override
    public int compareTo(HeapElement<T> o) {
        return this.data.compareTo(o.getData());
    }
}
