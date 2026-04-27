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

    public static <T extends Comparable<T>> Stack<T> sort(Stack<T> stack) {
        if (stack.head == null || stack.head.next == null) return stack;
        Node<T> middleNode = getMiddleNode(stack.head);
        Stack<T> leftStack = new Stack<>();
        leftStack.head = stack.head;
        leftStack.tail = middleNode;
        Stack<T> rightStack = new Stack<>();
        rightStack.head = middleNode.next;
        rightStack.tail = stack.tail;
        middleNode.next = null;
        if (stack.length % 2 == 1) {
            leftStack.length = (stack.length / 2) + 1;
        } else {
            leftStack.length = stack.length / 2;
        }
        rightStack.length = stack.length / 2;
        Stack<T> leftStackSorted = sort(leftStack);
        Stack<T> rightStackSorted = sort(rightStack);
        return merge(leftStackSorted, rightStackSorted);
    }

    private static <T extends Comparable<T>> Stack<T> merge(Stack<T> s1, Stack<T> s2) {
        Node<T> dummy = new Node<>(null);
        Node<T> temp = dummy;
        Stack<T> resultantStack = new Stack<>();
        resultantStack.length = s1.length + s2.length;
        Node<T> i = s1.head, j = s2.head;
        while (i != null && j != null) {
            if (i.data.compareTo(j.data) <= 0) {
                temp.next = i;
                i = i.next;
            } else {
                temp.next = j;
                j = j.next;
            }
            temp = temp.next;
            temp.next = null;
        }

        while (i != null) {
            temp.next = i;
            i = i.next;
            temp = temp.next;
            temp.next = null;
        }

        while (j != null) {
            temp.next = j;
            j = j.next;
            temp = temp.next;
            temp.next = null;
        }

        resultantStack.head = dummy.next;
        resultantStack.tail = temp;
        return resultantStack;
    }
}
