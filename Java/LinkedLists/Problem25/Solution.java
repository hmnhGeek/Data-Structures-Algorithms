package LinkedLists.Problem25;

import java.util.List;


class Part<T> {
    public Node<T> temp;
    public Integer length;

    public Part(Node<T> temp, Integer length) {
        this.temp = temp;
        this.length = length;
    }
}


public class Solution {
    public static void main(String[] args) {
        DoublyLinkedList<Integer> db = new DoublyLinkedList<>();
        db.build(1, 2, 3, 4, 5, 6);
        System.out.println(db);
        reverseInParts(db, 4);
        System.out.println(db);
    }

    public static <T> void reverseInParts(DoublyLinkedList<T> dll, int k) {
        Node<T> curr = dll.head;
        Node<T> prev = null;
        while (curr != null) {
            Part<T> part = getPart(k, curr);
            Node<T> nextCurr = delink(part);
            List<Node<T>> pointers = reversePart(curr, part);
            relink(dll, pointers, nextCurr, prev);
            prev = curr;
            curr = nextCurr;
        }
    }

    /**
     * Method to relink the part to the original DLL.
     * @param dll
     * @param pointers
     * @param nextCurr
     * @param prev
     * @param <T>
     */
    private static <T> void relink(DoublyLinkedList<T> dll, List<Node<T>> pointers, Node<T> nextCurr, Node<T> prev) {
        pointers.getLast().next = nextCurr;
        if (nextCurr != null) {
            nextCurr.prev = pointers.getLast();
        } else {
            dll.tail = pointers.getLast();
        }
        if (prev == null) {
            dll.head = pointers.getFirst();
        } else {
            prev.next = pointers.getFirst();
        }
    }

    /**
     * Reverse the DLL part.
     * @param curr A node denoting the current node.
     * @param part A Part object.
     * @return The new head and tail of the part.
     * @param <T> A generic type.
     */
    private static <T> List<Node<T>> reversePart(Node<T> curr, Part part) {
        DoublyLinkedList<T> sublist = new DoublyLinkedList<>();
        sublist.head = curr;
        sublist.tail = part.temp;
        sublist.length = part.length;
        List<Node<T>> pointers = sublist.reverse();
        return pointers;
    }

    /**
     * Method to de-link the part from the rest of the DLL.
     * @param part A {@code Part<T>} generic object.
     * @return Returns the next node which will become current.
     * @param <T> A generic type.
     */
    private static <T> Node<T> delink(Part part) {
        Node<T> nextCurr = part.temp.next;
        if (part.temp != null) {
            part.temp.next = null;
        }
        if (nextCurr != null) {
            nextCurr.prev = null;
        }
        return nextCurr;
    }

    /**
     * Method to return the part of the DLL (no de-linking yet).
     * @param k Denotes the size of the part.
     * @param curr Current pointer from which k nodes must be traversed.
     * @return A {@code Part<T>} object containing the last node of the part and the size of the part (could be
     * {@code k} or less than {@code k}.
     * @param <T> A generic type denoting the kind of elements stored in the linked list.
     */
    private static <T> Part<T> getPart(int k, Node<T> curr) {
        Node<T> temp = curr;
        Node<T> prevOfTemp = temp.prev;
        int counter = 1;
        int length = 0;
        while (counter != k && temp != null) {
            prevOfTemp = temp;
            temp = temp.next;
            counter += 1;
            length += 1;
        }

        // if temp became null before k nodes, then we can just reverse the small part.
        if (temp == null) {
            temp = prevOfTemp;
        }
        Part part = new Part(temp, length);
        return part;
    }
}
