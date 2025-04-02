package Graphs;

import javax.swing.text.html.parser.Entity;
import java.util.*;

class DisjointSet<T> {
    private HashMap<T, Integer> sizes;
    private HashMap<T, T> parents;

    public DisjointSet(List<T> nodes) {
        this.sizes = new HashMap<>();
        this.parents = new HashMap<>();
        for (T node : nodes) {
            this.sizes.put(node, 1);
            this.parents.put(node, node);
        }
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

class Coordinate {
    public Integer x;
    public Integer y;

    public Coordinate(Integer x, Integer y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public static void main(String[] args) {
        // Example 1
        List<Coordinate> coordinates = Arrays.asList(
                new Coordinate(0, 0),
                new Coordinate(0, 1),
                new Coordinate(1, 0),
                new Coordinate(1, 2),
                new Coordinate(2, 1),
                new Coordinate(2, 2)
        );
        System.out.println(removeStones(coordinates));

        // Example 2
        List<Coordinate> coordinates1 = Arrays.asList(
                new Coordinate(0, 0),
                new Coordinate(0, 2),
                new Coordinate(1, 1),
                new Coordinate(2, 0),
                new Coordinate(2, 2)
        );
        System.out.println(removeStones(coordinates1));
    }

    private static Integer removeStones(List<Coordinate> coordinates) {
        int maxRow = 0, maxCol = 0;
        for (Coordinate coordinate : coordinates) {
            maxRow = Math.max(maxRow, coordinate.x);
            maxCol = Math.max(maxCol, coordinate.y);
        }
        List<Integer> nodes = new ArrayList<>();
        for (int i = 0; i <= maxRow; i += 1) {
            nodes.add(i);
        }
        for (int j = 0; j <= maxCol; j += 1) {
            nodes.add(maxRow + 1 + j);
        }
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodes);

        HashMap<Integer, List<Integer>> rowToCol = new HashMap<>();
        for (int i = 0; i <= maxRow; i += 1) {
            rowToCol.put(i, new ArrayList<>());
        }

        HashMap<Integer, List<Integer>> colToRow = new HashMap<>();
        for (int j = 0; j <= maxCol; j += 1) {
            colToRow.put(j + maxRow + 1, new ArrayList<>());
        }

        for (int i = 0; i <= maxRow; i += 1) {
            for (Coordinate coordinate : coordinates) {
                if (coordinate.x == i) {
                    rowToCol.get(i).add(maxRow + 1 + coordinate.y);
                }
            }
        }

        for (int j = 0; j <= maxCol; j += 1) {
            for (Coordinate coordinate : coordinates) {
                if (coordinate.y == j) {
                    colToRow.get(j + maxRow + 1).add(coordinate.x);
                }
            }
        }

        for (Map.Entry<Integer, List<Integer>> entry : rowToCol.entrySet()) {
            Integer node1 = entry.getKey();
            if (entry.getValue().size() > 1) {
                for (Integer node2 : entry.getValue()) {
                    disjointSet.union(node1, node2);
                }
            }
        }

        for (Map.Entry<Integer, List<Integer>> entry : colToRow.entrySet()) {
            Integer node1 = entry.getKey();
            if (entry.getValue().size() > 1) {
                for (Integer node2 : entry.getValue()) {
                    disjointSet.union(node1, node2);
                }
            }
        }

        int numStonesRemoved = 0;
        for (Integer node : disjointSet.getParents().keySet()) {
            if (disjointSet.getParents().get(node).equals(node) && disjointSet.getSizes().get(node) > 1) {
                numStonesRemoved += (disjointSet.getSizes().get(node) - 1);
            }
        }
        return numStonesRemoved;
    }
}