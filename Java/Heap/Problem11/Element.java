package Heap.Problem11;

public class Element<T extends Comparable<T>> implements Comparable<Element<T>> {
    public T data;
    public Integer i;
    public Integer j;

    public Element(T data, Integer i, Integer j) {
        this.data = data;
        this.i = i;
        this.j = j;
    }

    @Override
    public int compareTo(Element<T> o) {
        return this.data.compareTo(o.data);
    }
}
