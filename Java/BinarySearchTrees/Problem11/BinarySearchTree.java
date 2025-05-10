package BinarySearchTrees.Problem11;

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

    public Integer getDiameter() {
        return diameter;
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
        if (start.getLeft() != null) {
            insert(start.getLeft(), node);
            return;
        }
        start.setLeft(node);
        node.setParent(start);
        recalcAugmentation(start);
        return;
    }

    public void insert(T data) {
        Node<T> node = new Node<>(data);
        if (this.root == null) {
            this.root = node;
            this.diameter = 1;
            return;
        }
        insert(this.root, node);
        return;
    }

    private Node<T> getLeftmostLeaf(Node<T> node) {
        if (node == null) return null;
        while (node.getLeft() != null) {
            node = node.getLeft();
        }
        return node;
    }

    private Node<T> getRightmostLeaf(Node<T> node) {
        if (node == null) return null;
        while (node.getRight() != null) {
            node = node.getRight();
        }
        return node;
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
            recalcAugmentation(parent);
            return;
        }
        if (node.getRight() != null) {
            Node<T> successor = getSuccessor(node);
            T successorData = successor.getData();
            successor.setData(node.getData());
            node.setData(successorData);
            delete(successor);
            return;
        }
        Node<T> predecessor = getPredecessor(node);
        T predecessorData = predecessor.getData();
        predecessor.setData(node.getData());
        node.setData(predecessorData);
        delete(predecessor);
        return;
    }

    private Node<T> getSuccessor(Node<T> node) {
        if (node == null) return null;
        if (node.getRight() != null) return getLeftmostLeaf(node.getRight());
        Node<T> parent = node.getParent();
        if (parent == null) return null;
        while (parent.getLeft() != node) {
            node = node.getParent();
            parent = parent.getParent();
            if (parent == null) {
                return null;
            }
        }
        return null;
    }

    private Node<T> getPredecessor(Node<T> node) {
        if (node == null) return null;
        if (node.getLeft() != null) return getRightmostLeaf(node.getLeft());
        Node<T> parent = node.getParent();
        if (parent == null) return null;
        while (parent.getRight() != node) {
            node = node.getParent();
            parent = parent.getParent();
            if (parent == null) {
                return null;
            }
        }
        return null;
    }

    private Node<T> getNode(Node<T> start, T data) {
        if (start == null || data == null) return null;
        if (start.getData().equals(data)) return start;
        if (data.compareTo(start.getData()) > 0) {
            return getNode(start.getRight(), data);
        }
        return getNode(start.getLeft(), data);
    }

    public void delete(T data) {
        Node<T> node = getNode(this.root, data);
        if (node != null) {
            delete(node);
            return;
        }
    }

    private void show(Node<T> start) {
        if (start != null) {
            show(start.getLeft());
            StringBuilder stringBuilder = new StringBuilder(String.format("Data = %s", start.getData()));
            if (start == this.root) {
                stringBuilder.append(" (root),");
            } else {
                stringBuilder.append(",");
            }
            stringBuilder.append(String.format(" size = %d,", start.getSize()));
            stringBuilder.append(String.format(" height = %d,", start.getHeight()));
            stringBuilder.append(String.format(" diameter = %d", start.getDiameter()));
            System.out.println(stringBuilder);
            show(start.getRight());
        }
    }

    public void show() {
        show(this.root);
        System.out.println();
    }
}
