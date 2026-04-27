package StacksAndQueues.Problem15;

public class Utils {
    public static <T extends Comparable<T>> Node<T> getMiddleNode(Node<T> startNode) {
        if (startNode == null) return null;
        Node<T> slow = startNode, fast = startNode.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
