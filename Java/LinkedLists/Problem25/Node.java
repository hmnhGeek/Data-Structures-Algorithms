package LinkedLists.Problem25;

public class Node<T> {
    public T data;
    public Node<T> prev, next;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }
}
