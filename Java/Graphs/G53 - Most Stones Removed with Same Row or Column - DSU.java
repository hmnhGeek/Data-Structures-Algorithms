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

        // Example 3
        List<Coordinate> coordinates3 = Arrays.asList(
                new Coordinate(0, 0),
                new Coordinate(0, 2),
                new Coordinate(1, 3),
                new Coordinate(3, 0),
                new Coordinate(3, 2),
                new Coordinate(4, 3)
        );
        System.out.println(removeStones(coordinates3));

        // Example 4
        List<Coordinate> coordinates4 = Arrays.asList(
                new Coordinate(0, 0),
                new Coordinate(1, 1),
                new Coordinate(2, 2),
                new Coordinate(2, 3),
                new Coordinate(2, 4),
                new Coordinate(3, 2)
        );
        System.out.println(removeStones(coordinates4));

        // Example 5
        List<Coordinate> coordinates5 = Arrays.asList(
                new Coordinate(0, 0),
                new Coordinate(0, 1),
                new Coordinate(1, 0),
                new Coordinate(1, 2),
                new Coordinate(2, 1),
                new Coordinate(2, 2)
        );
        System.out.println(removeStones(coordinates5));

        // Example 6
        List<Coordinate> coordinates6 = Arrays.asList(
                new Coordinate(0, 0),
                new Coordinate(0, 1),
                new Coordinate(1, 0)
        );
        System.out.println(removeStones(coordinates6));

        // Example 7
        List<Coordinate> coordinates7 = Arrays.asList(
                new Coordinate(2, 0),
                new Coordinate(2, 1),
                new Coordinate(3, 1),
                new Coordinate(3, 2),
                new Coordinate(5, 5)
        );
        System.out.println(removeStones(coordinates7));
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
        HashMap<Integer, Integer> stoneNodes = new HashMap<>();

        for (Coordinate coordinate : coordinates) {
            disjointSet.union(coordinate.x, coordinate.y + maxRow + 1);
            stoneNodes.put(coordinate.x, 1);
            stoneNodes.put(coordinate.y + maxRow + 1, 1);
        }

        int numComponents = 0;
        for (Integer node : stoneNodes.keySet()) {
            if (disjointSet.findUltimateParent(node).equals(node)) {
                numComponents += 1;
            }
        }
        return coordinates.size() - numComponents;
    }
}