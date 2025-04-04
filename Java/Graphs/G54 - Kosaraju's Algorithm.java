// Problem link - https://www.geeksforgeeks.org/strongly-connected-components/
// Solution - https://www.youtube.com/watch?v=R6uoSjZ2imo&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=54


package Graphs;

import java.util.*;

class Node<T> {
    private T data;
    private Node<T> next;

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public T getData() {
        return data;
    }

    public Node<T> getNext() {
        return next;
    }
}

class Stack<T> {
    private Node<T> head;
    private Node<T> tail;
    private Integer length;

    public Stack() {
        this.head = this.tail = null;
        this.length = 0;
    }

    public Node<T> getHead() {
        return head;
    }

    public void setHead(Node<T> head) {
        this.head = head;
    }

    public Node<T> getTail() {
        return tail;
    }

    public void setTail(Node<T> tail) {
        this.tail = tail;
    }

    public Integer getLength() {
        return length;
    }

    public void setLength(Integer length) {
        this.length = length;
    }

    public boolean isEmpty() {
        return this.length.equals(0);
    }

    public void push(T x) {
        Node<T> node = new Node<>(x);
        if (isEmpty()) {
            setHead(node);
            setTail(node);
        } else {
            node.setNext(getHead());
            setHead(node);
        }
        setLength(getLength() + 1);
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T item = getHead().getData();
        setHead(getHead().getNext());
        setLength(getLength() - 1);
        return item;
    }
}

class Utils {
    private static <T> void dfs(Map<T, List<T>> graph, T node, Stack<T> stack, Map<T, Boolean> visited) {
        /**
         * Time complexity is O(V + E) and space complexity is O(V).
         */

        // visit the node
        visited.put(node, true);

        // loop on the adjacent nodes of this node and if not visited, start a DFS on that adjacent node.
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                Utils.dfs(graph, adjNode, stack, visited);
            }
        }

        // push the node in the stack; typical code for toposort.
        stack.push(node);
    }

    public static <T> Stack<T> sortByReach(Map<T, List<T>> graph) {
        /**
         * Time complexity is O(V + E) and space complexity is O(V).
         */
        // initialize a stack which will take O(V) space.
        Stack<T> stack = new Stack<>();

        // initialize a visited map which will take O(V) space.
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }

        // for unvisited nodes, do a DFS in O(V + E) time and update the stack.
        for (T node : graph.keySet()) {
            if (!visited.get(node)) {
                Utils.dfs(graph, node, stack, visited);
            }
        }

        // return the stack.
        return stack;
    }

    public static <T> Map<T, List<T>> reverseGraph(Map<T, List<T>> graph) {
        /**
         * Time complexity is O(V + E) and space complexity is O(V + E).
         */

        // create an empty reversedGraph with same nodes as in graph. This will take O(V + E) space.
        Map<T, List<T>> reversedGraph = new HashMap<>();
        for (T node : graph.keySet()) {
            reversedGraph.put(node, new ArrayList<>());
        }

        // loop in the nodes of the given graph in O(V + E) time.
        for (T node : graph.keySet()) {
            for (T adjNode : graph.get(node)) {
                // add the reverse edge in the reversed graph, i.e., from adjNode --> node.
                List<T> adjacentNodes = reversedGraph.get(adjNode);
                if (!adjacentNodes.contains(node)) {
                    adjacentNodes.add(node);
                }
                reversedGraph.put(adjNode, adjacentNodes);
            }
        }

        // return the reversed graph.
        return reversedGraph;
    }
}

class StronglyConnectedComponentsFinder {
    private static <T> void getComponent(Map<T, List<T>> graph, T node, List<T> componentNodes, Map<T, Boolean> visited) {
        /**
         * Time complexity is O(V + E) and space complexity is O(V).
         */

        // mark the node as visited and add it to the component list.
        if (!visited.get(node)) {
            visited.put(node, true);
            componentNodes.add(node);
        }

        // loop on the adjacent nodes of this node and start a DFS on them if they are not visited.
        for (T adjNode : graph.get(node)) {
            if (!visited.get(adjNode)) {
                StronglyConnectedComponentsFinder.getComponent(graph, adjNode, componentNodes, visited);
            }
        }
    }

    public static <T> List<List<T>> findStronglyConnectedComponents(Map<T, List<T>> graph) {
        /**
         * Time complexity is O(V + E) and space complexity is O(V + E).
         */

        // perform a topological sort in O(V + E) time and O(V) space.
        Stack<T> stack = Utils.sortByReach(graph);

        // get the reversed graph in O(V + E) time and O(V + E) space.
        Map<T, List<T>> reversedGraph = Utils.reverseGraph(graph);

        // create a visited hash map in O(V) time.
        Map<T, Boolean> visited = new HashMap<>();
        for (T node : graph.keySet()) {
            visited.put(node, false);
        }

        // store the strongly connected components in this list.
        List<List<T>> result = new ArrayList<>();

        // now while the stack is not empty; this will run for V iterations.
        while (!stack.isEmpty()) {
            // pop the current node.
            T node = stack.pop();

            // if the current node is not visited, initiate a DFS on the reversed graph from this node.
            if (!visited.get(node)) {
                // while doing the DFS, collect the nodes in component array that belong to this strongly connected component.
                List<T> component = new ArrayList<>();

                // This is a typical DFS, thus takes O(V + E) time and O(V) space.
                StronglyConnectedComponentsFinder.getComponent(reversedGraph, node, component, visited);

                // add this SCC in the final list.
                result.add(component);
            }
        }

        // return the final list of SCCs.
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        // Example 1
        Map<Integer, List<Integer>> graph1 = new HashMap<>();
        graph1.put(0, List.of(1));
        graph1.put(1, List.of(2));
        graph1.put(2, List.of(0, 3));
        graph1.put(3, List.of(4));
        graph1.put(4, List.of(5, 7));
        graph1.put(5, List.of(6));
        graph1.put(6, List.of(4, 7));
        graph1.put(7, List.of());
        System.out.println(StronglyConnectedComponentsFinder.findStronglyConnectedComponents(graph1));

        // Example 2
        Map<Integer, List<Integer>> graph2 = new HashMap<>();
        graph2.put(0, List.of(2, 3));
        graph2.put(1, List.of(0));
        graph2.put(2, List.of(1));
        graph2.put(3, List.of(4));
        graph2.put(4, List.of());
        System.out.println(StronglyConnectedComponentsFinder.findStronglyConnectedComponents(graph2));

        // Example 3
        Map<Integer, List<Integer>> graph3 = new HashMap<>();
        graph3.put(0, List.of(1));
        graph3.put(1, List.of(2));
        graph3.put(2, List.of(0));
        System.out.println(StronglyConnectedComponentsFinder.findStronglyConnectedComponents(graph3));

        // Example 4
        Map<Integer, List<Integer>> graph4 = new HashMap<>();
        graph4.put(1, List.of(2));
        graph4.put(2, List.of(3, 4));
        graph4.put(3, List.of(4, 6));
        graph4.put(4, List.of(1, 5));
        graph4.put(5, List.of(6));
        graph4.put(6, List.of(7));
        graph4.put(7, List.of(5));
        System.out.println(StronglyConnectedComponentsFinder.findStronglyConnectedComponents(graph4));
    }
}
