package Graphs;

import java.util.HashMap;
import java.util.List;

class DisjointSet<T> {
    private HashMap<T, Integer> sizes;
    private HashMap<T, T> parents;

    public DisjointSet(List<T> nodes) {
        nodes.forEach(x -> {
            sizes.put(x, 1);
            parents.put(x, x);
        });
    }

    public HashMap<T, Integer> getSizes() {
        return sizes;
    }

    public void setSizes(HashMap<T, Integer> sizes) {
        this.sizes = sizes;
    }

    public HashMap<T, T> getParents() {
        return parents;
    }

    public void setParents(HashMap<T, T> parents) {
        this.parents = parents;
    }

    public T findUltimateParent(T node) {
        if (parents.get(node).equals(node)) {
            return node;
        }
        parents.put(node, findUltimateParent(parents.get(node)));
        return parents.get(node);
    }

    public void union(T node1, T node2) {
        T ulpNode1 = findUltimateParent(node1);
        T ulpNode2 = findUltimateParent(node2);

        if (ulpNode1.equals(ulpNode2)) {
            return;
        }

        if (sizes.get(ulpNode1) < sizes.get(ulpNode2)) {
            parents.put(ulpNode1, ulpNode2);
            sizes.put(ulpNode2, sizes.get(ulpNode2) + sizes.get(ulpNode1));
        } else if (sizes.get(ulpNode1).equals(sizes.get(ulpNode2))) {
            parents.put(ulpNode1, ulpNode2);
            sizes.put(ulpNode2, sizes.get(ulpNode2) + sizes.get(ulpNode1));
        } else {
            parents.put(ulpNode2, ulpNode1);
            sizes.put(ulpNode1, sizes.get(ulpNode1) + sizes.get(ulpNode2));
        }
    }

    public Integer numComponents() {
        int count = 0;
        for (T x : parents.keySet()) {
            if (parents.get(x).equals(x)) {
                count += 1;
            }
        }
        return count;
    }
}