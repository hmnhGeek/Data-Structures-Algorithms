package StacksAndQueues.Problem4;

public class SpecialStack<T> {
    private Stack<T> stack;
    private Deque<T> deque;

    public SpecialStack() {
        this.stack = new Stack<>();
        this.deque = new Deque<>();
    }

    public Stack<T> getStack() {
        return stack;
    }

    public void setStack(Stack<T> stack) {
        this.stack = stack;
    }

    public Deque<T> getDeque() {
        return deque;
    }

    public void setDeque(Deque<T> deque) {
        this.deque = deque;
    }

    public void push(T x) {
        getDeque().pushBack(x);
        if (getDeque().getLength() - getStack().getLength() > 1) {
            T t = getDeque().popFront();
            getStack().push(t);
        }
    }

    public T pop() {
        if (getDeque().getLength().equals(0)) return null;
        T item = getDeque().popBack();
        if (getDeque().getLength().compareTo(getStack().getLength()) < 0) {
            T t = getStack().pop();
            getDeque().pushFront(t);
        }
        return item;
    }
}
