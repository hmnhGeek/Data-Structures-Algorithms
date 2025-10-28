package StacksAndQueues.Problem8;

public class SpecialStack {
    public Stack<Integer> stack;
    public Integer minValue;

    public SpecialStack() {
        this.stack = new Stack<>();
        this.minValue = Integer.MAX_VALUE;
    }

    public boolean isEmpty() {
        return this.stack.isEmpty();
    }

    public void push(Integer x) {
        if (isEmpty()) {
            minValue = x;
            stack.push(x);
        } else if (x < minValue) {
            Integer valToPush = 2*x - minValue;
            minValue = x;
            stack.push(valToPush);
        } else {
            stack.push(x);
        }
    }

    public Integer pop() {
        if (isEmpty()) return null;
        Integer top = stack.head.data;
        stack.pop();
        if (top < minValue) {
            Integer returnVal = 2*minValue - top;
            minValue = 2*minValue - top;
            return returnVal;
        }
        if (stack.isEmpty()) {
            minValue = Integer.MAX_VALUE;
        }
        return top;
    }

    public Integer getTop() {
        Integer top = pop();
        push(top);
        return top;
    }

    public Integer getMin() {
        return minValue;
    }
}
