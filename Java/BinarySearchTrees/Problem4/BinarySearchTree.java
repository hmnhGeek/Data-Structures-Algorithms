package BinarySearchTrees.Problem4;


class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right, parent;
    Integer size, height, diameter;

    public Node(T data) {
        this.data = data;
        this.left = this.right = this.parent = null;
        this.size = this.height = this.diameter = 1;
    }
}


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
            this.diameter = Math.max(this.diameter, parent.diameter);
            parent = parent.parent;
        }
    }

    private void insert(Node<T> start, Node<T> node) {
        if (start == null || node == null) return;
        if (node.data.compareTo(start.data) >= 0) {
            if (start.right != null) {
                insert(start.right, node);
                return;
            }
            start.right = node;
            node.parent = start;
            recalcAugmentation(start);
            return;
        }
        if (start.left != null) {
            insert(start.left, node);
            return;
        }
        start.left = node;
        node.parent = start;
        recalcAugmentation(start);
        return;
    }

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (this.root == null) {
            this.root = node;
            this.diameter = 1;
            return;
        }
        insert(this.root, node);
    }
}
