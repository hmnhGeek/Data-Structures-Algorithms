package BinarySearchTrees.Problem3;


class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right, parent;
    public Integer size, diameter, height;

    public Node(T data) {
        this.data = data;
        this.left = this.right = this.parent = null;
        this.size = this.diameter = this.height = 1;
    }
}


public class BinarySearchTree<T extends Comparable<T>> {
    public Node<T> root;
    public Integer diameter;

    public BinarySearchTree() {
        this.root = null;
        this.diameter = 0;
    }

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (root == null) {
            root = node;
            diameter = 1;
            return;
        }
        insert(root, node);
    }

    private void insert(Node<T> root, Node<T> node) {
        if (root == null || node == null) return;
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

    private void recalcAugmentation(Node<T> parent) {
        diameter = 0;
        while (parent != null) {
            Integer leftSize = 0, leftHeight = 0;
            if (parent.left != null) {
                leftSize = parent.left.size;
                leftHeight = parent.left.height;
            }
            Integer rightSize = 0, rightHeight = 0;
            if (parent.right != null) {
                rightSize = parent.right.size;
                rightHeight = parent.right.height;
            }
            parent.size = 1 + leftSize + rightSize;
            parent.height = 1 + Math.max(leftHeight, rightHeight);
            parent.diameter = 1 + leftHeight + rightHeight;
            this.diameter = Math.max(diameter, parent.diameter);
            parent = parent.parent;
        }
    }
}
