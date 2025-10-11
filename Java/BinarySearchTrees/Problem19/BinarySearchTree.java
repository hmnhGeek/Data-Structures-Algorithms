package BinarySearchTrees.Problem19;


import java.util.Map;

class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left;
    public Node<T> right;
    public Node<T> parent;
    public Integer height;
    public Integer size;
    public Integer diameter;

    public Node(T data) {
        this.data = data;
        left = right = parent = null;
        height = size = diameter = 1;
    }
}


public class BinarySearchTree<T extends Comparable<T>> {

    public Node<T> root;
    public Integer diameter;

    public BinarySearchTree() {
        root = null;
        diameter = 0;
    }

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (root == null) {
            root = node;
            diameter = 1;
            return;
        }
        insert(root, node);
        return;
    }

    public void insert(Node<T> start, Node<T> node) {
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

    private void recalcAugmentation(Node<T> parent) {
        diameter = 0;
        while (parent != null) {
            Integer leftSize = parent.left != null ? parent.left.size : 0;
            Integer rightSize = parent.right != null ? parent.right.size : 0;
            Integer leftHeight = parent.left != null ? parent.left.height : 0;
            Integer rightHeight = parent.right != null ? parent.right.height : 0;
            parent.size = 1 + leftSize + rightSize;
            parent.height = 1 + Math.max(leftHeight, rightHeight);
            parent.diameter = 1 + leftHeight + rightHeight;
            parent = parent.parent;
        }
    }

    public Node<T> getLeftmostNode(Node<T> node) {
        if (node == null) return null;
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    public Node<T> getRightmostNode(Node<T> node) {
        if (node == null) return null;
        while (node.right != null) {
            node = node.right;
        }
        return node;
    }

    public Node<T> getSuccessor(Node<T> node) {
        if (node == null) return null;
        if (node.right != null) return getLeftmostNode(node.right);
        Node<T> parent = node.parent;
        if (parent == null) {
            return null;
        }
        while (parent.left != node) {
            node = node.parent;
            parent = parent.parent;
            if (parent == null) return null;
        }
        return parent;
    }

    public Node<T> getPredecessor(Node<T> node) {
        if (node == null) return null;
        if (node.left != null) return getRightmostNode(node.left);
        Node<T> parent = node.parent;
        if (parent == null) {
            return null;
        }
        while (parent.right != node) {
            node = node.parent;
            parent = parent.parent;
            if (parent == null) return null;
        }
        return parent;
    }

}
