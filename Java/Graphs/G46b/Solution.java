// Video - https://www.youtube.com/watch?v=aBxjDBC4M1U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=46


package Graphs.G46b;


public class Solution {
    public static void main(String[] args) {
        DisjointSet<Integer> dss = new DisjointSet<>(1, 2, 3, 4, 5, 6, 7);
        dss.union(1, 2);
        dss.union(2, 3);
        dss.union(4, 5);
        dss.union(6, 7);
        dss.union(5, 6);
        System.out.println(dss.inSameComponent(3, 7));
        dss.union(3, 7);
        System.out.println(dss.inSameComponent(3, 7));
    }
}
