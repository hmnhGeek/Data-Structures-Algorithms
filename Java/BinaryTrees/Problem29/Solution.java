package BinaryTrees.Problem29;

public class Solution {
    public static Integer getMaxNonAdjacentSum(Node<Integer> root) {
        return Math.max(solve(root, true), solve(root, false));
    }

    private static Integer solve(Node<Integer> root, Boolean include) {
        if (root == null) return 0;
        if (include) {
            return root.data + solve(root.left, false) + solve(root.right, false);
        } else {
            Integer leftSum = Math.max(
                    solve(root.left, false),
                    solve(root.left, true)
            );
            Integer rightSum = Math.max(
                    solve(root.right, false),
                    solve(root.right, true)
            );
            return leftSum + rightSum;
        }
    }

    public static void main(String[] args) {
        // Example 1
        Node<Integer> one1 = new Node<>(1);
        Node<Integer> two1 = new Node<>(2);
        Node<Integer> three1 = new Node<>(3);
        Node<Integer> node1_1 = new Node<>(1);
        Node<Integer> four1 = new Node<>(4);
        Node<Integer> five1 = new Node<>(5);

        one1.left = two1;
        two1.left = node1_1;
        three1.left = four1;
        one1.right = three1;
        three1.right = five1;

        System.out.println("Example 1");
        System.out.println(getMaxNonAdjacentSum(one1));
        System.out.println();

        // Example 2
        Node<Integer> one2 = new Node<>(1);
        Node<Integer> two2 = new Node<>(2);
        Node<Integer> three2 = new Node<>(3);
        Node<Integer> node1_2 = new Node<>(1);
        Node<Integer> node1_3 = new Node<>(1);
        Node<Integer> four2 = new Node<>(4);
        Node<Integer> five2 = new Node<>(5);

        one2.left = two2;
        two2.left = node1_2;
        three2.left = four2;
        one2.right = three2;
        three2.right = five2;
        two2.right = node1_3;

        System.out.println("Example 2");
        System.out.println(getMaxNonAdjacentSum(one2));
        System.out.println();

        // Example 3
        Node<Integer> two3 = new Node<>(2);
        Node<Integer> six3 = new Node<>(6);
        Node<Integer> eight3 = new Node<>(8);
        Node<Integer> zero3 = new Node<>(0);
        Node<Integer> nine1_3 = new Node<>(9);
        Node<Integer> nine2_3 = new Node<>(9);
        Node<Integer> seven3 = new Node<>(7);

        two3.left = zero3;
        eight3.left = seven3;
        two3.right = six3;
        six3.right = eight3;
        eight3.right = nine1_3;
        nine1_3.right = nine2_3;

        System.out.println("Example 3");
        System.out.println(getMaxNonAdjacentSum(two3));
        System.out.println();

        // Example 4
        Node<Integer> eight4 = new Node<>(8);
        Node<Integer> hundered4 = new Node<>(100);
        Node<Integer> mfive4 = new Node<>(-5);
        Node<Integer> thone4 = new Node<>(31);
        Node<Integer> eione4 = new Node<>(81);
        Node<Integer> sixsix4 = new Node<>(66);
        Node<Integer> eifive4 = new Node<>(85);
        Node<Integer> mten4 = new Node<>(-10);

        eight4.left = hundered4;
        hundered4.left = thone4;
        sixsix4.left = eifive4;
        eight4.right = mfive4;
        mfive4.right = sixsix4;
        sixsix4.right = mten4;
        hundered4.right = eione4;

        System.out.println("Example 4");
        System.out.println(getMaxNonAdjacentSum(eight4));
        System.out.println();

        // Example 5
        Node<Integer> fourtyone5 = new Node<>(41);
        Node<Integer> m100_5 = new Node<>(-100);
        Node<Integer> twtytwo5 = new Node<>(22);
        Node<Integer> sixteen5 = new Node<>(16);
        Node<Integer> fiftyfive5 = new Node<>(55);
        Node<Integer> m15_5 = new Node<>(-15);
        Node<Integer> ninetytwo5 = new Node<>(92);
        Node<Integer> fourty5 = new Node<>(40);
        Node<Integer> fifty5 = new Node<>(50);

        fourtyone5.left = m100_5;
        m100_5.left = sixteen5;
        twtytwo5.left = m15_5;
        m15_5.left = fifty5;
        fourtyone5.right = twtytwo5;
        twtytwo5.right = ninetytwo5;
        m100_5.right = fiftyfive5;
        sixteen5.right = fourty5;

        System.out.println("Example 5");
        System.out.println(getMaxNonAdjacentSum(fourtyone5));
    }
}
