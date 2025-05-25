package LinkedLists.Problem8;

public class Solution {
    public static void main(String[] args) {
        solve(2, 5, 6, 2, 1);
    }

    public static <T> void lastToFront(LinkedList<T> linkedList) {
        if (linkedList.getHead() == linkedList.getTail()) return;
        Node<T> curr = linkedList.getHead();
        Node<T> prev = null;
        while (curr != linkedList.getTail()) {
            prev = curr;
            curr = curr.getNext();
        }
        prev.setNext(null);
        curr.setNext(linkedList.getHead());
        linkedList.setHead(curr);
        linkedList.setTail(prev);
    }

    public static <T> void solve(T... args) {
        LinkedList<T> linkedList = new LinkedList<>();
        linkedList.build(args);
        System.out.println(linkedList);
        lastToFront(linkedList);
        System.out.println(linkedList);
    }
}
