package LinkedLists.Problem7;

public class Solution {
    public static void main(String[] args) {
        // Example 1
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(1, 2, 3, 4, 4, 2);
        System.out.println(l1);
        l1.removeDuplicates();
        System.out.println(l1);
    }
}
