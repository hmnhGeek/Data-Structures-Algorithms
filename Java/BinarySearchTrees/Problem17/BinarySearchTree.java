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
}
