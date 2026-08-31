package Graphs.G51;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DisjointSet<T> {
    public Map<T, T> parents;
    public Map<T, Integer> sizes;

    public DisjointSet(List<T> nodes) {
        this.parents = new HashMap<>();
        this.sizes = new HashMap<>();
        for (T node : nodes) {
            this.parents.put(node, node);
            this.sizes.put(node, 1);
        }
    }

    public T findUltimateParent(T node) {
        if (node == this.parents.get(node)) return node;
        this.parents.put(node, findUltimateParent(this.parents.get(node)));
        return this.parents.get(node);
    }

    public void union(T node1, T node2) {
        T ulpNode1 = findUltimateParent(node1), ulpNode2 = findUltimateParent(node2);
        if (ulpNode1 == ulpNode2) return;
        if (this.sizes.get(ulpNode1) < this.sizes.get(ulpNode2)) {
            this.parents.put(ulpNode1, ulpNode2);
            this.sizes.put(ulpNode2, this.sizes.get(ulpNode2) + this.sizes.get(ulpNode1));
        } else {
            this.parents.put(ulpNode2, ulpNode1);
            this.sizes.put(ulpNode1, this.sizes.get(ulpNode2) + this.sizes.get(ulpNode1));
        }
    }

    public boolean inSameComponents(T node1, T node2) {
        return findUltimateParent(node1) == findUltimateParent(node2);
    }

    public Integer getNumberOfComponents() {
        int count = 0;
        for (T node : this.parents.keySet()) {
            if (this.parents.get(node) == node) {
                count += 1;
            }
        }
        return count;
    }
}
