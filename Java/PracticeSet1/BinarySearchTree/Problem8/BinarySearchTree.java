package PracticeSet1.BinarySearchTree.Problem8;

public class BinarySearchTree<T extends Comparable<T>> {
    public Node<T> root;
    public Integer diameter;

    public BinarySearchTree() {
        this.root = null;
        this.diameter = 0;
    }

    public void recalcAugmentation(Node<T> parent) {
        this.diameter = 0;
        while (parent != null) {
            int leftSize = 0, leftHeight = 0;
            if (parent.left != null) {
                leftSize = parent.left.size;
                leftHeight = parent.left.height;
            }
            int rightSize = 0, rightHeight = 0;
            if (parent.right != null) {
                rightSize = parent.right.size;
                rightHeight = parent.right.height;
            }
            parent.size = 1 + leftSize + rightSize;
            parent.height = 1 + Math.max(leftHeight, rightHeight);
            parent.diameter = 1 + leftHeight + rightHeight;
            this.diameter = Math.max(parent.diameter, this.diameter);
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
    }

    private Node<T> getNode(Node<T> start, T x) {
        if (start == null || x == null) return null;
        if (start.data == x) return start;
        if (x.compareTo(start.data) >= 0) {
            return getNode(start.right, x);
        }
        return getNode(start.left, x);
    }
}
