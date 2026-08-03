package LinkedLists.Problem29;

public class Solution {
    public static void sort(LinkedList<Integer> linkedList) {
        Node<Integer> zeroDummy = new Node<>(null);
        Node<Integer> zeroTemp = zeroDummy;

        Node<Integer> oneDummy = new Node<>(null);
        Node<Integer> oneTemp = oneDummy;

        Node<Integer> twoDummy = new Node<>(null);
        Node<Integer> twoTemp = twoDummy;

        Node<Integer> curr = linkedList.head;
        while (curr != null) {
            Node<Integer> nextCurr = curr.next;
            if (curr.data == 0) {
                zeroTemp.next = curr;
                zeroTemp = zeroTemp.next;
                zeroTemp.next = null;
            } else if (curr.data == 1) {
                oneTemp.next = curr;
                oneTemp = oneTemp.next;
                oneTemp.next = null;
            } else {
                twoTemp.next = curr;
                twoTemp = twoTemp.next;
                twoTemp.next = null;
            }
            curr = nextCurr;
        }
        if (zeroDummy.next != null) {
            linkedList.head = zeroDummy.next;
            if (oneDummy.next != null) {
                zeroTemp.next = oneDummy.next;
                oneTemp.next = twoDummy.next;
            } else {
                zeroTemp.next = twoDummy.next;
            }
        } else {
            if (oneDummy.next != null) {
                linkedList.head = oneDummy.next;
                oneTemp.next = twoDummy.next;
            } else {
                linkedList.head = twoDummy.next;
            }
        }
        if (twoDummy.next != null) {
            linkedList.tail = twoTemp;
        } else if (oneDummy.next != null) {
            linkedList.tail = oneTemp;
        } else {
            linkedList.tail = zeroTemp;
        }
    }

    public static void main(String[] args) {
        test(1, 2, 2, 1, 2, 0, 2, 2);
    }

    private static void test(Integer...args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(args);
        System.out.println(linkedList);
        sort(linkedList);
        System.out.println(linkedList);
        System.out.println();
    }
}
