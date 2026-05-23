package LinkedLists.Problem24;

public class Node<T> {
    public T data;
    public Node<T> next, prev;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }
}
