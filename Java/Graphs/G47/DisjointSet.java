package Graphs.G47;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DisjointSet<T> {
    public Map<T, Integer> ranks;
    public Map<T, T> parents;

    public DisjointSet(List<T> nodes) {
        this.ranks = new HashMap<>();
        this.parents = new HashMap<>();
        for (T node : nodes) {
            this.ranks.put(node, 0);
            this.parents.put(node, node);
        }
    }

    public T getUltimateParent(T node) {
        if (node == getUltimateParent(node)) return node;
        this.parents.put(node, getUltimateParent(node));
        return this.parents.get(node);
    }

    public void union(T node1, T node2) {
        T ulpNode1 = getUltimateParent(node1), ulpNode2 = getUltimateParent(node2);
        if (ulpNode1 == ulpNode2) return;
        if (this.ranks.get(ulpNode1) < this.ranks.get(ulpNode2)) {
            this.parents.put(ulpNode1, ulpNode2);
        } else if (this.ranks.get(ulpNode2) < this.ranks.get(ulpNode1)) {
            this.parents.put(ulpNode2, ulpNode1);
        } else {
            this.parents.put(ulpNode1, ulpNode2);
            this.ranks.put(ulpNode2, this.ranks.get(ulpNode2) + 1);
        }
    }

    public boolean inSameComponent(T node1, T node2) {
        return getUltimateParent(node1) == getUltimateParent(node2);
    }
}
