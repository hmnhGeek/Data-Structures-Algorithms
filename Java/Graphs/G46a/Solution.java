// Video - https://www.youtube.com/watch?v=aBxjDBC4M1U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=46


package Graphs.G46a;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        DisjointSet<Integer> dsr = new DisjointSet<>(List.of(1, 2, 3, 4, 5, 6, 7));
        dsr.union(1, 2);
        dsr.union(2, 3);
        dsr.union(4, 5);
        dsr.union(6, 7);
        dsr.union(5, 6);
        System.out.println(dsr.inSameComponents(3, 7));
        dsr.union(3, 7);
        System.out.println(dsr.inSameComponents(3, 7));
    }
}
