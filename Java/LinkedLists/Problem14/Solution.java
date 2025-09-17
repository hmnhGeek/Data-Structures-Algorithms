package LinkedLists.Problem14;

public class Solution {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        l1.build(16,3,89,2,6,4,3);
        System.out.println(l1);
        l1 = QuickSort.sort(l1);
        System.out.println(l1);
    }


}
