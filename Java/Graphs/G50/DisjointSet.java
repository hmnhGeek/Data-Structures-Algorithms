package Graphs.G50;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DisjointSet<T> {
    public Map<T, T> parents;
    public Map<T, Integer> ranks;

    public DisjointSet(List<T> nodes) {
        this.parents = new HashMap<>();
        this.ranks = new HashMap<>();
        for (T node : nodes) {
            this.parents.put(node, node);
            this.ranks.put(node, 0);
        }
    }

    public T getUltimateParent(T node) {
        if (this.parents.get(node) == node) return node;
        this.parents.put(node, getUltimateParent(this.parents.get(node)));
        return this.parents.get(node);
    }

    public void union(T node1, T node2) {
        T ulpNode1 = getUltimateParent(node1), ulpNode2 = getUltimateParent(node2);
        if (ulpNode1 == ulpNode2) return;
        if (this.ranks.get(ulpNode1) < this.ranks.get(ulpNode2)) {
            this.parents.put(ulpNode1, ulpNode2);
        } else if (this.ranks.get(ulpNode1) > this.ranks.get(ulpNode2)){
            this.parents.put(ulpNode2, ulpNode1);
        } else {
            this.parents.put(ulpNode1, ulpNode2);
            this.ranks.put(ulpNode2, this.ranks.get(ulpNode2) + 1);
        }
    }

    public Integer getNumComponents() {
        int count = 0;
        for (T node : this.parents.keySet()) {
            if (this.parents.get(node) == node) {
                count += 1;
            }
        }
        return count;
    }
}
