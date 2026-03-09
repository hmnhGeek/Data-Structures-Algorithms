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

    private Node<T> getLeftmostLeaf(Node<T> node) {
        if (node == null) return null;
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    private Node<T> getRightmostLeaf(Node<T> node) {
        if (node == null) return null;
        while (node.right != null) {
            node = node.right;
        }
        return node;
    }

    private Node<T> getSuccessor(Node<T> node) {
        if (node == null) return null;
        if (node.right != null) return getLeftmostLeaf(node.right);
        Node<T> parent = node.parent;
        if (parent == null) return null;
        while (parent.left != node) {
            node = node.parent;
            parent = parent.parent;
            if (parent == null) return null;
        }
        return parent;
    }

    private Node<T> getPredecessor(Node<T> node) {
        if (node == null) return null;
        if (node.left != null) return getRightmostLeaf(node.left);
        Node<T> parent = node.parent;
        if (parent == null) return null;
        while (parent.right != node) {
            node = node.parent;
            parent = parent.parent;
            if (parent == null) return null;
        }
        return parent;
    }

    private void delete(Node<T> node) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            Node<T> parent = node.parent;
            if (parent != null) {
                if (parent.left == node) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            } else {
                this.root = null;
                this.diameter = 0;
            }
            recalcAugmentation(parent);
            return;
        }
        if (node.right != null) {
            Node<T> successor = getSuccessor(node);
            T temp = successor.data;
            successor.data = node.data;
            node.data = temp;
            delete(successor);
            return;
        }
        Node<T> predecessor = getPredecessor(node);
        T temp = predecessor.data;
        predecessor.data = node.data;
        node.data = temp;
        delete(predecessor);
        return;
    }

    public void delete(T x) {
        Node<T> node = getNode(this.root, x);
        delete(node);
    }

    public Node<T> getNode(Node<T> start, T x) {
        if (start == null || x == null) return null;
        if (x == start.data) return start;
        if (x.compareTo(start.data) > 0) return getNode(start.right, x);
        return getNode(start.left, x);
    }
}
