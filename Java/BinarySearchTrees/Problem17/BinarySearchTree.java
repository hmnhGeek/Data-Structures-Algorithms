package BinarySearchTrees.Problem17;


class Node<T extends Comparable<T>> {
    private T data;
    private Node<T> left;
    private Node<T> right;
    private Node<T> parent;
    private Integer size;
    private Integer height;
    private Integer diameter;

    public Node(T data) {
        this.data = data;
        this.left = this.right = this.parent = null;
        this.size = this.height = this.diameter = 1;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getLeft() {
        return left;
    }

    public void setLeft(Node<T> left) {
        this.left = left;
    }

    public Node<T> getRight() {
        return right;
    }

    public void setRight(Node<T> right) {
        this.right = right;
    }

    public Node<T> getParent() {
        return parent;
    }

    public void setParent(Node<T> parent) {
        this.parent = parent;
    }

    public Integer getSize() {
        return size;
    }

    public void setSize(Integer size) {
        this.size = size;
    }

    public Integer getHeight() {
        return height;
    }

    public void setHeight(Integer height) {
        this.height = height;
    }

    public Integer getDiameter() {
        return diameter;
    }

    public void setDiameter(Integer diameter) {
        this.diameter = diameter;
    }
}


public class BinarySearchTree<T extends Comparable<T>> {
    private Node<T> root;
    private Integer diameter;

    public Node<T> getRoot() {
        return root;
    }

    public void setRoot(Node<T> root) {
        this.root = root;
    }

    public Integer getDiameter() {
        return diameter;
    }

    public void setDiameter(Integer diameter) {
        this.diameter = diameter;
    }

    public BinarySearchTree() {
        this.root = null;
        this.diameter = 0;
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

    private void recalcAugmentation(Node<T> parent) {
        this.diameter = 0;
        while (parent != null) {
            Integer leftSize = parent.getLeft() != null ? parent.getLeft().getSize() : 0;
            Integer rightSize = parent.getRight() != null ? parent.getRight().getSize() : 0;
            Integer leftHeight = parent.getLeft() != null ? parent.getLeft().getHeight() : 0;
            Integer rightHeight = parent.getRight() != null ? parent.getRight().getHeight() : 0;
            parent.setSize(1 + leftSize + rightSize);
            parent.setHeight(1 + Math.max(leftHeight, rightHeight));
            parent.setDiameter(1 + leftHeight + rightHeight);
            this.diameter = Math.max(this.diameter, parent.getDiameter());
            parent = parent.getParent();
        }
    }

    private void insert(Node<T> start, Node<T> node) {
        if (start == null || node == null) return;
        if (node.getData().compareTo(start.getData()) >= 0) {
            if (start.getRight() != null) {
                insert(start.getRight(), node);
                return;
            }
            start.setRight(node);
            node.setParent(start);
            recalcAugmentation(start);
            return;
        }
        if (node.getLeft() != null) {
            insert(start.getLeft(), node);
            return;
        }
        start.setLeft(node);
        node.setParent(start);
        recalcAugmentation(start);
    }

    private Node<T> getLeftmostNode(Node<T> node) {
        if (node == null) return null;
        while (node.getLeft() != null) {
            node = node.getLeft();
        }
        return node;
    }

    private Node<T> getRightmostNode(Node<T> node) {
        if (node == null) return null;
        while (node.getRight() != null) {
            node = node.getRight();
        }
        return node;
    }

    private Node<T> getSuccessor(Node<T> node) {
        if (node == null) return null;

        if (node.getRight() != null) {
            return getLeftmostNode(node.getRight());
        }

        Node<T> parent = node.getParent();
        if (parent == null) return null;
        while (parent.getLeft() != node) {
            node = node.getParent();
            parent = parent.getParent();
            if (parent == null) return null;
        }
        return parent;
    }

    private Node<T> getPredecessor(Node<T> node) {
        if (node == null) return null;

        if (node.getLeft() != null) {
            return getRightmostNode(node.getLeft());
        }

        Node<T> parent = node.getParent();
        if (parent == null) return null;
        while (parent.getRight() != node) {
            node = node.getParent();
            parent = parent.getParent();
            if (parent == null) return null;
        }
        return parent;
    }

    private void delete(Node<T> node) {
        if (node == null) return;
        if (node.getLeft() == null && node.getRight() == null) {
            Node<T> parent = node.getParent();
            if (parent != null) {
                if (parent.getLeft() == node) {
                    parent.setLeft(null);
                } else {
                    parent.setRight(null);
                }
            } else {
                this.root = null;
                this.diameter = 0;
            }
            this.recalcAugmentation(parent);
            return;
        }
        if (node.getRight() != null) {
            Node<T> successor = getSuccessor(node);
            T data = successor.getData();
            successor.setData(node.getData());
            node.setData(data);
            delete(successor);
            return;
        }
        Node<T> predecessor = getPredecessor(node);
        T data = predecessor.getData();
        predecessor.setData(node.getData());
        node.setData(data);
        delete(predecessor);
    }

    public void delete(T x) {
        Node<T> node = getNode(this.root, x);
        if (node != null) {
            delete(node);
        }
    }

    public Node<T> getNode(Node<T> root, T x) {
        if (root == null || x == null) {
            return null;
        }
        if (x.compareTo(root.getData()) == 0) {
            return root;
        }
        if (x.compareTo(root.getData()) > 0) {
            return getNode(root.getRight(), x);
        }
        return getNode(root.getLeft(), x);
    }

    private void show(Node<T> root) {
        if (root != null) {
            this.show(root.getLeft());
            StringBuilder s = new StringBuilder("Data =");
            if (root == this.root) {
                s.append(String.format(" %s (root), ", root.getData()));
            } else {
                s.append(String.format(" %s, ", root.getData()));
            }
            s.append(String.format("size = %d, height = %d, diameter = %d", root.getSize(), root.getHeight(), root.getDiameter()));
            System.out.println(s);
            this.show(root.getRight());
        }
    }

    public void show() {
        this.show(this.root);
        System.out.println();
    }
}
