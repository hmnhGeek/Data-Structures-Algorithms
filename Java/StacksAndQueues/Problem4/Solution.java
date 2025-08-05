// Problem link with Solution - https://www.geeksforgeeks.org/dsa/design-a-stack-with-find-middle-operation/

package StacksAndQueues.Problem4;

public class Solution {
    public static void main(String[] args) {
        SpecialStack<Integer> specialStack1 = new SpecialStack<>();
        specialStack1.push(1);
        specialStack1.push(2);
        System.out.println(specialStack1.getMiddle());
        System.out.println(specialStack1.pop());
        System.out.println(specialStack1.popMiddle());
    }
}
