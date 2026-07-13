package BinaryTrees.Problem23;


class Flag {
    public Integer level;
    public Boolean flag;

    public Flag() {
        this.level = null;
        this.flag = Boolean.TRUE;
    }
}


public class Solution {
    public static <T> Boolean allLeavesAtSameLevel(Node<T> root) {
        Flag fl = new Flag();
        solve(root, 0, fl);
        return fl.flag;
    }

    private static <T> void solve(Node<T> root, Integer level, Flag fl) {
        if (root == null) return;
        if (fl.flag == Boolean.FALSE) return;
        if (root.left == null && root.right == null) {
            if (fl.level == null) {
                fl.level = level;
            } else {
                fl.flag = fl.level.equals(level);
            }
        }
        solve(root.left, level + 1, fl);
        solve(root.right, level + 1, fl);
    }

    public static void main(String[] args) {

        // Example 1
        Node<Integer> n1 = new Node<>(1);
        Node<Integer> n2 = new Node<>(2);
        Node<Integer> n3 = new Node<>(3);
        n1.left = n2;
        n1.right = n3;
        System.out.println(allLeavesAtSameLevel(n1));

        // Example 2
        Node<Integer> n10 = new Node<>(10);
        Node<Integer> n20 = new Node<>(20);
        Node<Integer> n30 = new Node<>(30);
        Node<Integer> n10_1 = new Node<>(10);
        Node<Integer> n15 = new Node<>(15);
        n10.left = n20;
        n10.right = n30;
        n20.left = n10_1;
        n20.right = n15;
        System.out.println(allLeavesAtSameLevel(n10));

        // Example 3
        Node<Integer> a1 = new Node<>(1);
        Node<Integer> a2 = new Node<>(2);
        Node<Integer> a3 = new Node<>(3);
        a3.left = a2;
        a3.right = a1;
        System.out.println(allLeavesAtSameLevel(a3));

        // Example 4
        Node<Integer> b12 = new Node<>(12);
        Node<Integer> b5 = new Node<>(5);
        Node<Integer> b7 = new Node<>(7);
        Node<Integer> b3 = new Node<>(3);
        Node<Integer> b1 = new Node<>(1);
        b12.left = b5;
        b12.right = b7;
        b5.left = b3;
        b7.right = b1;
        System.out.println(allLeavesAtSameLevel(b12));

        // Example 5
        Node<Integer> c12 = new Node<>(12);
        Node<Integer> c5 = new Node<>(5);
        Node<Integer> c3 = new Node<>(3);
        Node<Integer> c9 = new Node<>(9);
        Node<Integer> c1 = new Node<>(1);
        Node<Integer> c2 = new Node<>(2);
        c12.left = c5;
        c5.left = c3;
        c5.right = c9;
        c3.left = c1;
        c9.left = c2;
        System.out.println(allLeavesAtSameLevel(c12));

        // Example 6
        Node<Integer> d12 = new Node<>(12);
        Node<Integer> d5 = new Node<>(5);
        Node<Integer> d7 = new Node<>(7);
        Node<Integer> d3 = new Node<>(3);
        d12.left = d5;
        d12.right = d7;
        d5.left = d3;
        System.out.println(allLeavesAtSameLevel(d12));
    }
}
