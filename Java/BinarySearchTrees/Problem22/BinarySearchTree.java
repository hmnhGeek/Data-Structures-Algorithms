package BinarySearchTrees.Problem22;


class Node<T> {
    public T data;
    public Node<T> left;
    public Node<T> right;
    public Node<T> parent;
    public Integer size;
    public Integer height;
    public Integer diameter;

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

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (this.root == null) {
            this.root = node;
            this.diameter = 1;
            return;
        }
        insert(this.root, node);
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
    }

    public Node<T> getLeftmostLeaf(Node<T> node) {
        if (node == null) {
            return null;
        }
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    public Node<T> getRightmostLeaf(Node<T> node) {
        if (node == null) {
            return null;
        }
        while (node.right != null) {
            node = node.right;
        }
        return node;
    }

    public Node<T> getSuccessor(Node<T> node) {
        if (node == null) return null;
        if (node.right != null) {
            return getLeftmostLeaf(node.right);
        }
        Node<T> parent = node.parent;
        if (parent == null) return null;
        while (parent.left != node) {
            node = node.parent;
            parent = parent.parent;
            if (parent == null) {
                return null;
            }
        }
        return parent;
    }

    public Node<T> getPredecessor(Node<T> node) {
        if (node == null) return null;
        if (node.left != null) {
            return getRightmostLeaf(node.left);
        }
        Node<T> parent = node.parent;
        if (parent == null) return null;
        while (parent.right != node) {
            node = node.parent;
            parent = parent.parent;
            if (parent == null) {
                return null;
            }
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

    public Node<T> getNode(Node<T> start, T x) {
        if (start == null || x == null) return null;
        if (start.data == x) return start;
        if (x.compareTo(start.data) > 0) return getNode(start.right, x);
        return getNode(start.left, x);
    }

    public void delete(T x) {
        Node<T> node = getNode(this.root, x);
        delete(node);
    }

    public void show(Node<T> start) {
        if (start != null) {
            show(start.left);
            StringBuilder sb = new StringBuilder(String.format("Data = %s", start.data));
            if (start == root) {
                sb.append(" (root), ");
            } else {
                sb.append(", ");
            }
            sb.append(String.format("size = %d, height = %d, diameter = %d", start.size, start.height, start.diameter));
            System.out.println(sb);
            show(start.right);
        }
    }

    public void show() {
        show(root);
        System.out.println();
    }
}
