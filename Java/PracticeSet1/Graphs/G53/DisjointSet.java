package PracticeSet1.Graphs.G53;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DisjointSet<T> {
    public Map<T, Integer> size;
    public Map<T, T> parent;

    public DisjointSet(List<T> nodes) {
        this.size = new HashMap<>();
        this.parent = new HashMap<>();
        for (T node : nodes) {
            this.size.put(node, 1);
            this.parent.put(node, node);
        }
    }

    public T findUltimateParent(T node) {
        if (this.parent.get(node).equals(node)) return node;
        this.parent.put(node, findUltimateParent(this.parent.get(node)));
        return this.parent.get(node);
    }

    public void union(T node1, T node2) {
        T ulpNode1 = findUltimateParent(node1), ulpNode2 = findUltimateParent(node2);
        if (ulpNode1 == ulpNode2) return;
        if (this.size.get(ulpNode1) < this.size.get(ulpNode2)) {
            this.parent.put(ulpNode1, ulpNode2);
            this.size.put(ulpNode2, this.size.get(ulpNode1) + this.size.get(ulpNode2));
        } else {
            this.parent.put(ulpNode2, ulpNode1);
            this.size.put(ulpNode1, this.size.get(ulpNode1) + this.size.get(ulpNode2));
        }
    }

    public boolean inSameComponent(T node1, T node2) {
        return findUltimateParent(node1).equals(findUltimateParent(node2));
    }
}
