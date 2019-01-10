# Lambda

#### Example
```java
// Class NumberPair has two fields
interface IntegerLogic {
    boolean operation(int a, int b);
}

public boolean logicOperation(NumberPair other, IntegerLogic method) {
    return (method.operation(this.width, other.getWidth()) &&
            method.operation(this.height, other.getHeight()));
}

// example of usage
public boolean isSmaller(NumberPair other) {
    return logicOperation(other, (a, b) -> (a < b));
}
```
