package LinkedLists.Problem28;

public class Node<T> {
    public T data;
    public Node<T> bottom, next;

    public Node(T data) {
        this.data = data;
        this.bottom = this.next = null;
    }
}
