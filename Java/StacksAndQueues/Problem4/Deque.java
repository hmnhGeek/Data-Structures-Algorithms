package StacksAndQueues.Problem4;


class DequeNode<T> {
    private T data;
    private DequeNode<T> prev;
    private DequeNode<T> next;

    public DequeNode(T data) {
        this.data = data;
        this.prev = this.next = null;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public DequeNode<T> getPrev() {
        return prev;
    }

    public void setPrev(DequeNode<T> prev) {
        this.prev = prev;
    }

    public DequeNode<T> getNext() {
        return next;
    }

    public void setNext(DequeNode<T> next) {
        this.next = next;
    }
}


public class Deque<T> {

    private DequeNode<T> head;
    private DequeNode<T> tail;
    private Integer length;

    public Deque() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public DequeNode<T> getHead() {
        return head;
    }

    public void setHead(DequeNode<T> head) {
        this.head = head;
    }

    public DequeNode<T> getTail() {
        return tail;
    }

    public void setTail(DequeNode<T> tail) {
        this.tail = tail;
    }

    public Integer getLength() {
        return length;
    }

    public void setLength(Integer length) {
        this.length = length;
    }

    public void pushFront(T x) {
        DequeNode<T> node = new DequeNode<>(x);
        if (this.length.equals(0)) {
            this.head = this.tail = node;
        } else {
            node.setNext(this.head);
            this.head.setPrev(node);
            setHead(node);
        }
        this.length += 1;
    }

    public void pushBack(T x) {
        DequeNode<T> node = new DequeNode<>(x);
        if (this.length.equals(0)) {
            setHead(node);
            setTail(node);
        } else {
            getTail().setNext(node);
            node.setPrev(getTail());
            setTail(node);
        }
        this.length += 1;
    }

    public T popFront() {
        if (this.length.equals(0)) return null;
        T item = getHead().getData();
        if (getLength().equals(1)) {
            setHead(null);
            setTail(null);
            setLength(0);
            return item;
        }
        setHead(getHead().getNext());
        getHead().setPrev(null);
        setLength(getLength() - 1);
        return item;
    }

    public T popBack() {
        if (getLength().equals(0)) return null;
        T item = getTail().getData();
        if (getLength().equals(1)) {
            setHead(null);
            setTail(null);
            setLength(0);
            return item;
        }
        setTail(getTail().getPrev());
        getTail().setNext(null);
        setLength(getLength() - 1);
        return item;
    }
}
