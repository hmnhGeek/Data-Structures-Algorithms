package StacksAndQueues.Problem8;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void test(Integer...x) {
        SpecialStack specialStack = new SpecialStack();
        List<Integer> list = new ArrayList<>();
        for (Integer i : x) {
            specialStack.push(i);
            list.add(specialStack.getMin());
        }
        System.out.println(list);
    }

    public static void main(String[] args) {
        test(18, 19, 29, 15, 16);
        test(34, 335, 1814, 86);

        // with pop()
        SpecialStack specialStack = new SpecialStack();
        specialStack.push(12);
        specialStack.push(15);
        specialStack.push(10);
        System.out.println(specialStack.getMin());
        specialStack.pop();
        System.out.println(specialStack.getMin());
        System.out.println(specialStack.getTop());
        specialStack.push(10);
        System.out.println(specialStack.getTop());
    }
}
