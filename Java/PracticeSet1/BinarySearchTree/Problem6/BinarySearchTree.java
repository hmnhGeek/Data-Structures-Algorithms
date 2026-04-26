package PracticeSet1.BinarySearchTree.Problem6;


class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left, right, parent;
    public Integer size, height, diameter;

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

    public void recalcAugmentation(Node<T> parent) {
        this.diameter = 0;
        while (parent != null) {
            Integer leftSize = 0;
            Integer leftHeight = 0;
            if (parent.left != null) {
                leftSize = parent.left.size;
                leftHeight = parent.left.height;
            }
            Integer rightSize = 0;
            Integer rightHeight = 0;
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
        insert(this.root, node);
    }

    public void insert(Node<T> root, Node<T> node) {
        if (root == null || node == null) return;
        if (node.data.compareTo(root.data) >= 0) {
            if (root.right != null) {
                root.right = node;
                node.parent = root;
                recalcAugmentation(root);
                return;
            }
            insert(root.right, node);
            return;
        }
        if (node.left != null) {
            root.left = node;
            node.parent = root;
            recalcAugmentation(root);
            return;
        }
        insert(root.left, node);
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
        if (node == null) {
            return null;
        }
        if (node.right != null) return getLeftmostNode(node);
        Node<T> parent = node.parent;
        if (parent == null) return null;
        while (parent.left != node) {
            parent = parent.parent;
            node = node.parent;
            if (parent == null) return null;
        }
        return parent;
    }

    public Node<T> getPredecessor(Node<T> node) {
        if (node == null) {
            return null;
        }
        if (node.left != null) return getRightmostNode(node);
        Node<T> parent = node.parent;
        if (parent == null) return null;
        while (parent.right != node) {
            parent = parent.parent;
            node = node.parent;
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
    }

    public void delete(T x) {
        Node<T> node = getNode(this.root, x);
        delete(node);
    }

    private Node<T> getNode(Node<T> root, T x) {
        if (root == null || x == null) return null;
        if (root.data == x) {
            return root;
        }
        if (x.compareTo(root.data) > 0) {
            return getNode(root.right, x);
        }
        return getNode(root.left, x);
    }
}
