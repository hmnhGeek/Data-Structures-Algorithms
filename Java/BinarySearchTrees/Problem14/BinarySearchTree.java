package BinarySearchTrees.Problem14;

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
        this.diameter = this.size = this.height = 1;
        this.left = this.right = this.left = null;
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

    public BinarySearchTree() {
        this.root = null;
        this.diameter = 0;
    }

    public Node<T> getRoot() {
        return root;
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

    private void insert(Node<T> start, Node<T> node) {
        if (root == null || node == null) return;
        if (node.getData().compareTo(start.getData()) >= 0) {
            if (start.getRight() != null) {
                insert(start.getRight(), node);
                return;
            }
            start.setRight(node);
            node.setParent(start);
            recalcAug(start);
            return;
        }
        if (start.getLeft() != null) {
            insert(start.getLeft(), node);
            return;
        }
        start.setLeft(node);
        node.setParent(start);
        recalcAug(start);
    }

    private void recalcAug(Node<T> parent) {
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

    public Node<T> getLeftmostLeaf(Node<T> node) {
        if (node == null) return null;
        while (node.getLeft() != null) {
            node = node.getLeft();
        }
        return node;
    }

    public Node<T> getRightmostLeaf(Node<T> node) {
        if (node == null) return null;
        while (node.getRight() != null) {
            node = node.getRight();
        }
        return node;
    }

    public Node<T> getSuccessor(Node<T> node) {
        if (node == null) {
            return null;
        }
        if (node.getRight() != null) {
            return this.getLeftmostLeaf(node.getRight());
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

    public Node<T> getPredecessor(Node<T> node) {
        if (node == null) {
            return null;
        }
        if (node.getLeft() != null) {
            return this.getRightmostLeaf(node.getLeft());
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

    public void delete(Node<T> node) {
        if (node == null) return;
        if (node.getRight() == null && node.getLeft() == null) {
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
            recalcAug(parent);
            return;
        }
        if (node.getRight() != null) {
            Node<T> successor = getSuccessor(node);
            T succData = successor.getData();
            successor.setData(node.getData());
            node.setData(succData);
            delete(successor);
            return;
        }
        Node<T> predecessor = getPredecessor(node);
        T preData = predecessor.getData();
        predecessor.setData(node.getData());
        node.setData(preData);
        delete(predecessor);
        return;
    }

    public void delete(T x) {
        Node<T> node = getNode(this.root, x);
        if (node != null) {
            delete(node);
        }
    }

    public Node<T> getNode(Node<T> root, T x) {
        if (root == null || x == null) return null;
        if (root.getData().equals(x)) return root;
        if (x.compareTo(root.getData()) > 0) return getNode(root.getRight(), x);
        return getNode(root.getLeft(), x);
    }

    private void show(Node<T> start) {
        if (start != null) {
            show(start.getLeft());
            StringBuilder stringBuilder = new StringBuilder(String.format("Data = %s", start.getData()));
            if (start == this.root) {
                stringBuilder.append(" (root), ");
            } else {
                stringBuilder.append(", ");
            }
            stringBuilder.append(String.format("size = %d, height = %d, diameter = %d", start.getSize(), start.getHeight(), start.getDiameter()));
            System.out.println(stringBuilder);
            show(start.getRight());
        }
    }

    public void show() {
        show(this.root);
        System.out.println();
    }
}
