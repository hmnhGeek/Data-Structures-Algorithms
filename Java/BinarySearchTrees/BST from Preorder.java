package BinarySearchTrees;


import java.util.Arrays;
import java.util.List;

class Node<T> {
    private T data;
    private Integer size;
    private Integer height;
    private Integer diameter;
    private Node<T> left;
    private Node<T> right;
    private Node<T> parent;

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
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

    public Node(T data) {
        this.data = data;
        this.size = this.height = this.diameter = 1;
        this.left = this.right = this.parent = null;
    }
}

class BinarySearchTree<T extends Comparable<T>> {
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

    public void recalcAugmentation(Node<T> parent) {
        setDiameter(0);
        while (parent != null) {
            int leftSize = parent.getLeft() != null ? parent.getLeft().getSize() : 0;
            int rightSize = parent.getRight() != null ? parent.getRight().getSize() : 0;
            int leftHeight = parent.getLeft() != null ? parent.getLeft().getHeight() : 0;
            int rightHeight = parent.getRight() != null ? parent.getRight().getHeight() : 0;
            parent.setSize(1 + leftSize + rightSize);
            parent.setHeight(1 + Math.max(leftHeight, rightHeight));
            parent.setDiameter(1 + leftHeight + rightHeight);
            setDiameter(Math.max(getDiameter(), parent.getDiameter()));
            parent = parent.getParent();
        }
    }

    private void _insert(Node<T> start, Node<T> node) {
        if (start == null || node == null) {
            return;
        }
        if (node.getData().compareTo(start.getData()) >= 0) {
            if (start.getRight() != null) {
                _insert(start.getRight(), node);
                return;
            }
            start.setRight(node);
            node.setParent(start);
            recalcAugmentation(start);
            return;
        }
        if (start.getLeft() != null) {
            _insert(start.getLeft(), node);
            return;
        }
        start.setLeft(node);
        node.setParent(start);
        recalcAugmentation(start);
    }

    public void insert(T x) {
        Node<T> node = new Node<>(x);
        if (getRoot() == null) {
            setRoot(node);
            setDiameter(1);
            return;
        }
        _insert(getRoot(), node);
    }

    private Node<T> getLeftmostLeaf(Node<T> node) {
        if (node == null) {
            return null;
        }
        while (node.getLeft() != null) {
            node = node.getLeft();
        }
        return node;
    }

    private Node<T> getRightmostLeaf(Node<T> node) {
        if (node == null) {
            return null;
        }
        while (node.getRight() != null) {
            node = node.getRight();
        }
        return node;
    }

    private Node<T> getSuccessor(Node<T> node) {
        if (node == null) {
            return null;
        }
        if (node.getRight() != null) {
            return getLeftmostLeaf(node.getRight());
        }
        Node<T> parent = node.getParent();
        if (parent == null) {
            return null;
        }
        while (parent.getLeft() != node) {
            node = node.getParent();
            parent = parent.getParent();
            if (parent == null) {
                return null;
            }
        }
        return parent;
    }

    private Node<T> getPredecessor(Node<T> node) {
        if (node == null) {
            return null;
        }
        if (node.getLeft() != null) {
            return getRightmostLeaf(node.getLeft());
        }
        Node<T> parent = node.getParent();
        if (parent == null) {
            return null;
        }
        while (parent.getRight() != node) {
            node = node.getParent();
            parent = parent.getParent();
            if (parent == null) {
                return null;
            }
        }
        return parent;
    }

    private void _delete(Node<T> node) {
        if (node == null) {
            return;
        }
        if (node.getLeft() == null && node.getRight() == null) {
            Node<T> parent = node.getParent();
            if (parent != null) {
                if (parent.getLeft() == node) {
                    parent.setLeft(null);
                }
                else {
                    parent.setRight(null);
                }
            }
            else {
                setRoot(null);
                setDiameter(0);
            }
            recalcAugmentation(parent);
            return;
        }
        if (node.getRight() != null) {
            Node<T> successor = getSuccessor(node);
            T successorData = successor.getData();
            successor.setData(node.getData());
            node.setData(successorData);
            _delete(successor);
            return;
        }
        Node<T> predecessor = getPredecessor(node);
        T predecessorData = predecessor.getData();
        predecessor.setData(node.getData());
        node.setData(predecessorData);
    }

    private Node<T> getNode(Node<T> start, T data) {
        if (start == null || data == null) {
            return null;
        }
        if (start.getData().equals(data)) {
            return start;
        }
        if (data.compareTo(start.getData()) > 0) {
            return getNode(start.getRight(), data);
        }
        return getNode(start.getLeft(), data);
    }

    public void delete(T data) {
        Node<T> node = getNode(getRoot(), data);
        if (node != null) {
            _delete(node);
        }
    }

    private void _show(Node<T> start) {
        if (start != null) {
            _show(start.getLeft());
            StringBuilder message = new StringBuilder("Data = " + start.getData());
            if (start == getRoot()) {
                message.append(" (root)");
            }
            message.append(String.format(", size = %d, ht = %d, d = %d", start.getSize(), start.getHeight(), start.getDiameter()));
            System.out.println(message);
            _show(start.getRight());
        }
    }

    public void show() {
        _show(getRoot());
        System.out.println();
    }
}

class Solution {
    public static void main(String[] args) {
        // Example 1
        BinarySearchTree<Integer> binarySearchTree1 = constructBst(Arrays.asList(10, 5, 1, 7, 40, 50));
        binarySearchTree1.show();

        // Example 2
        BinarySearchTree<Integer> binarySearchTree2 = constructBst(Arrays.asList(1, 2));
        binarySearchTree2.show();

        // Example 3
        BinarySearchTree<Integer> binarySearchTree3 = constructBst(Arrays.asList(2, 1));
        binarySearchTree3.show();

        // Example 4
        BinarySearchTree<Integer> binarySearchTree4 = constructBst(Arrays.asList(22, 12, 8, 20, 30, 25, 40));
        binarySearchTree4.show();

        // Example 5
        BinarySearchTree<Integer> binarySearchTree5 = constructBst(Arrays.asList(100, 20, 10, 30, 200, 150, 300));
        binarySearchTree5.show();
    }

    private static <T extends Comparable<T>> BinarySearchTree<T> constructBst(List<T> preorder) {
        BinarySearchTree<T> binarySearchTree = new BinarySearchTree<T>();
        preorder.forEach(binarySearchTree::insert);
        return binarySearchTree;
    }
}