package LinkedLists.Problem7;

public class Solution {
    public static void main(String[] args) {
        helper(1, 2, 3, 4, 4, 2);
        helper(2, 2, 2, 2, 2, 2);
        helper(1, 2);
        helper(1);
        helper(5, 2, 4, 2);
        helper(4, 2, 5, 4, 2, 2, -1);
        helper(1, 2, 1, 2, 2, 2, 7, 7, -1);
        helper(3, 3, 3, 3, 3, -1);
        helper(10, 20, 10, 20, 30, 10, 20, 30, -1);
    }

    private static void helper(Integer... args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.build(args);
        System.out.println(linkedList);
        linkedList.removeDuplicates();
        System.out.println(linkedList);
        System.out.println();
    }
}
