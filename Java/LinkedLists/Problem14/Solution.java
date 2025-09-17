// Problem link - https://www.geeksforgeeks.org/problems/quick-sort-on-linked-list/1
// Solution - https://www.youtube.com/watch?v=ByUiqQGz5_w

package LinkedLists.Problem14;

public class Solution {
    private static void test(Integer...args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(args);
        System.out.println(String.format("Original: %s", linkedList));
        linkedList = QuickSort.sort(linkedList);
        System.out.println(String.format("Sorted: %s", linkedList));
        System.out.println();
    }

    public static void main(String[] args) {
        test(16, 3, 89, 2, 6, 4, 3);
        test(1, 6, 2);
        test(1, 9, 3, 8);
        test(10, 1, 10);
    }
}
