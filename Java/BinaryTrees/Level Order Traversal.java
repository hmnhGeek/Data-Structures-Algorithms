package BinaryTrees;

import java.util.List;

class QueueNode {
    public Integer getData() {
        return data;
    }

    public QueueNode getNext() {
        return next;
    }

    private Integer data;
    private QueueNode next;

    public QueueNode(Integer data) {
        this.data = data;
        this.next = null;
    }

    public void setNext(QueueNode next) {
        this.next = next;
    }
}

class Queue {
    private QueueNode head;
    private QueueNode tail;
    private Integer length;

    public Queue() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public void push(Integer x) {
        QueueNode node = new QueueNode(x);
        if (isEmpty()) {
            head = tail = node;
        }
        else {
            tail.setNext(node);
            tail = node;
        }
        length += 1;
    }

    public Integer pop() {
        if (isEmpty()) {
            return null;
        }
        Integer item = head.getData();
        head = head.getNext();
        length -= 1;
        return item;
    }
}


//class Solution {
//    public static List<Integer> getLevelOrderTraversal()
//}