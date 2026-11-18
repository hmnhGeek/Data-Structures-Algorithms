package PracticeSet1.Heap.Problem10.Misc;

import PracticeSet1.Heap.Problem10.LinkedList.Node;

/*
    Instead of binding Node class to a comparable T, create a custom element which
    will always store nodes which store a comparable T.
 */
public class Element<T extends Comparable<T>> implements Comparable<Element<T>> {
    public Node<T> node;

    public Element(Node<T> node) {
        this.node = node;
    }

    @Override
    public int compareTo(Element<T> o) {
        return this.node.data.compareTo(o.node.data);
    }
}
