package LinkedLists.Problem22;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<List<Integer>> getTriplets(DoublyLinkedList<Integer> dll, Integer target) {
        if (dll.length == 0 || dll.length == 1 || dll.length == 2) return null;
        Node<Integer> i = dll.head, j = i.next, k = dll.tail;
        List<List<Integer>> result = new ArrayList<>();
        while (i != dll.tail.prev) {
            while (j != k && k.next != j) {
                Integer idata = i.data, jdata = j.data, kdata = k.data;
                Integer sum = idata + jdata + kdata;
                if (sum.equals(target)) {
                    result.add(List.of(idata, jdata, kdata));
                    j = j.next;
                    k = k.prev;
                } else if (sum.compareTo(target) > 0) {
                    k = k.prev;
                } else {
                    j = j.next;
                }
            }
            i = i.next;
            j = i.next;
            k = dll.tail;
        }
        return result;
    }

    public static void test(int target, Integer...arr) {
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.build(arr);
        List<List<Integer>> result = Solution.getTriplets(dll, target);
        System.out.println(result);
    }

    public static void main(String[] args) {
        test(8, 1, 2, 3, 4);
        test(17, 1, 2, 3, 4, 5, 6, 7);
        test(13, 1, 2, 3, 8, 9);
        test(15, 1, 2, 3, 4, 5, 6, 7, 8, 9);
        test(40, 7, 33, 88, 91);
        test(19, 3, 7, 9, 23, 45);
        test(37, 8, 13, 16);
        test(17, 1, 2, 4, 5, 6, 8, 9);
        test(15, 1, 2, 4, 5, 6, 8, 9);
    }
}
