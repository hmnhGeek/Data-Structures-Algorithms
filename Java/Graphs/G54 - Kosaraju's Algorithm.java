package Graphs;

import jdk.jshell.execution.Util;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }

    public Node<T> getNext() {
        return next;
    }
}

class Stack<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public Stack() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public Node<T> getHead() {
        return head;
    }

    public void setHead(Node<T> head) {
        this.head = head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public void setTail(Node<T> tail) {
        this.tail = tail;
    }

    public Integer getLength() {
        return length;
    }

    public void setLength(Integer length) {
        this.length = length;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            setHead(node);
            setTail(node);
        } else {
            getTail().setNext(node);
            setTail(node);
        }
        setLength(getLength() + 1);
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = getHead().getData();
        setHead(getHead().getNext());
        setLength(getLength() - 1);
        return item;
    }
}

class Utils {
    private static <T> void dfs(Map<T, List<T>> graph, T node, Stack<T> stack, Map<T, Boolean> visited) {
        visited.put(node, true);
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                Utils.dfs(graph, adjNode, stack, visited);
            }
        }
        stack.push(node);
    }

    public static <T> Stack<T> sortByReach(Map<T, List<T>> graph) {
        Stack<T> stack = new Stack<>();
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                Utils.dfs(graph, node, stack, visited);
            }
        }
        return stack;
    }
}