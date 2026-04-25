package LinkedLists.Problem23;

public class Solution {
    public static void sortDoublyLinkedList(DoublyLinkedList<Integer> dll, Integer k) {
        MinHeap<Node<Integer>> pq = new MinHeap<>();
        // move first k integers in min heap
        Node<Integer> curr = dll.head;
        int count = 0;
        while (count <= k + 1) {
            pq.insert(curr);
            curr = curr.next;
            count += 1;
        }
        Node<Integer> dummyNode = new Node<>(null);
        Node<Integer> tempNode = dummyNode;
        while (!pq.isEmpty()) {
            Node<Integer> poppedNode = pq.pop();
            tempNode.next = poppedNode;
            poppedNode.prev = tempNode;
            tempNode = poppedNode;
            if (curr != null) {
                pq.insert(curr);
                curr = curr.next;
            }
        }
        dll.head = dummyNode.next;
        dll.tail = tempNode;
    }

    public static void main(String[] args) {
        DoublyLinkedList<Integer> dll1 = new DoublyLinkedList<>();
        dll1.build(3, 2, 1, 5, 6, 4);
        System.out.println(dll1);
        sortDoublyLinkedList(dll1, 2);
        System.out.println(dll1);

        System.out.println();

        DoublyLinkedList<Integer> dll2 = new DoublyLinkedList<>();
        dll2.build(5, 6, 7, 3, 4, 4);
        System.out.println(dll2);
        sortDoublyLinkedList(dll2, 3);
        System.out.println(dll2);
    }
}
