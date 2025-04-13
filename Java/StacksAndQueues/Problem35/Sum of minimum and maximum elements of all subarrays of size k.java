package StacksAndQueues.Problem35;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

class Node<T extends Comparable<T>> {
    private T data;
    private Node<T> prev;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.prev = this.next = null;
    }

    public Node<T> getPrev() {
        return prev;
    }

    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }
}


class Deque<T extends Comparable<T>> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public Deque() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void pushBack(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            this.head = this.tail = node;
        }
        else {
            this.tail.setNext(node);
            node.setPrev(this.tail);
            this.tail = node;
        }
        this.length += 1;
    }

    public T popFront() {
        if (isEmpty()) {
            return null;
        }
        if (this.length == 1) {
            T item = this.head.getData();
            this.head = this.tail = null;
            this.length = 0;
            return item;
        }
        T item = this.head.getData();
        Node<T> nextHead = this.head.getNext();
        nextHead.setPrev(null);
        this.head.setNext(null);
        this.head = nextHead;
        this.length -= 1;
        return item;
    }

    public T getFront() {
        if (isEmpty()) {
            return null;
        }
        return this.head.getData();
    }

    public T getBack() {
        if (isEmpty()) {
            return null;
        }
        return this.tail.getData();
    }

    public T popBack() {
        if (isEmpty()) {
            return null;
        }
        if (this.length == 1) {
            T item = this.head.getData();
            this.head = this.tail = null;
            this.length = 0;
            return item;
        }
        T item = this.tail.getData();
        Node<T> prevNode = this.tail.getPrev();
        prevNode.setNext(null);
        this.tail.setPrev(null);
        this.length -= 1;
        this.tail = prevNode;
        return item;
    }
}


class Solution {
    public static void main(String[] args) {
        System.out.println(getSum(Arrays.asList(2, 5, -1, 7, -3, -1, -2), 4));
        System.out.println(getSum(Arrays.asList(1, 2, 3, 4, 5), 3));
        System.out.println(getSum(Arrays.asList(2, 4, 7, 3, 8, 1), 4));
    }

    public static Integer getSum(List<Integer> array, Integer k) {
        /**
         *  Time complexity is O(n) and space complexity is O(n).
         */

        // get max and min sliding window sums in O(n) time and O(n) space.
        List<Integer> maxes = getSlidingWindowMaximum(array, k);
        List<Integer> minis = getSlidingWindowMinimum(array, k);

        // iterate on both lists and sum them up in O(n) time.
        int n = maxes.size();
        int sum = 0;
        for (int i = 0; i < n; i += 1) {
            sum += (array.get(maxes.get(i)) + array.get(minis.get(i)));
        }
        return sum;
    }

    private static List<Integer> getSlidingWindowMaximum(List<Integer> array, Integer k) {
        Deque<Integer> dq = new Deque<>();
        List<Integer> result = new ArrayList<>();
        int n = array.size();
        for (int i = 0; i < n; i += 1) {
            // remove the front element if it is out of window.
            if (!dq.isEmpty() && dq.getFront().equals(i - k)) {
                dq.popFront();
            }

            // while the dq does not maintain a decreasing order, pop from back.
            while (!dq.isEmpty() && array.get(dq.getBack()) < array.get(i)) {
                dq.popBack();
            }

            // push the current index into dq.
            dq.pushBack(i);

            // if i has crossed the first window, push the front into result list as it corresponds to the max value index.
            if (i >= k - 1) {
                result.add(dq.getFront());
            }
        }
        return result;
    }

    private static List<Integer> getSlidingWindowMinimum(List<Integer> array, Integer k) {
        Deque<Integer> dq = new Deque<>();
        List<Integer> result = new ArrayList<>();
        int n = array.size();
        for (int i = 0; i < n; i += 1) {
            if (!dq.isEmpty() && dq.getFront().equals(i - k)) {
                dq.popFront();
            }
            while (!dq.isEmpty() && array.get(dq.getBack()) >= array.get(i)) {
                dq.popBack();
            }
            dq.pushBack(i);
            if (i >= k - 1) {
                result.add(dq.getFront());
            }
        }
        return result;
    }
}