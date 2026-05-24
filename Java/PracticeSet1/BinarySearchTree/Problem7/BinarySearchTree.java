package PracticeSet1.BinarySearchTree.Problem7;

public class BinarySearchTree<T extends Comparable<T>> {
    public Node<T> root;
    public Integer diameter;

    public BinarySearchTree() {
        this.root = null;
        this.diameter = 0;
    }

    private void recalcAugmentation(Node<T> parent) {
        this.diameter = 0;
        while (parent != null) {
            Integer leftSize = 0, rightSize = 0, leftHeight = 0, rightHeight = 0;
            if (parent.left != null) {
                leftSize = parent.left.size;
                leftHeight = parent.left.height;
            }
            if (parent.right != null) {
                rightSize = parent.right.size;
                rightHeight = parent.right.height;
            }
            parent.size = 1 + leftSize + rightSize;
            parent.height = 1 + Math.max(leftHeight, rightHeight);
            parent.diameter = 1 + leftHeight + rightHeight;
            this.diameter = Math.max(this.diameter, parent.diameter);
            parent = parent.parent;
        }
    }

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (this.root == null) {
            this.root = node;
            this.diameter = 1;
            return;
        }
        insert(root, node);
    }

    private void insert(Node<T> root, Node<T> node) {
        if (node == null || root == null) return;
        if (node.data.compareTo(root.data) >= 0) {
            if (root.right != null) {
                insert(root.right, node);
                return;
            }
            root.right = node;
            node.parent = root;
            recalcAugmentation(root);
            return;
        }
        if (root.left != null) {
            insert(root.left, node);
            return;
        }
        root.left = node;
        node.parent = root;
        recalcAugmentation(root);
    }
}
