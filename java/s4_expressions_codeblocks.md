# session4 Expressions Statements CodeBlocks Methods

### Keywords and Expressions
* Keywords: 
    * reserved words (showing in blue)
    * cannot be used as user variable
    * [List of Java Keywords](https://en.wikipedia.org/wiki/List_of_Java_keywords)

* Expressions:
    * variables values operators (except the type or semicolon)
    * components within blancket
    * `highScore == 10`, `a = (100 - 28 * 2)`

### Statements whitespace and indenting
* statement:
    * complete line (including type or semicolon)
    * methods
    * can be multiple lines: the line break does not make change
    ```java
    System.out.println("This is" +
        " another" +
        " still more.");
    // This is another still more.
    ```
    * can put several statements in the same line:
    `int a = 50; a++;`
    * java does not care about white spaces

### Code Blocks
* things within braces `{ ... }`.
* can add multiple statements
* the code block can access values from outside
* but outside cannot access values created inside
```java
if(score < 500) {
    System.out.println("less than 500")
    int thiscannotbeaccessed = 500
} else if (score < 800) {
    System.out.println("less than 800")
} else {
    System.out.println("other case")
}

// I cannot access thiscannotbeaccessed value
// I created inside of the code block
```


### methods
* arguments: type variablename
* easier to maintain
* void methods are called procedure
Example: 
```java
public static void main(Strin[] args) {
    calculateScore(true, 800, 5, 100);
}

public static void calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) {
    if (gameOver) {
        int finalScore = score + (levelCompleted * bonus);
        System.out.println("Your final score was " + finalScore);
    }
} 
```

* can also return values: functions
```java
public static void main(Strin[] args) {
    int highScore = calculateScore(true, 800, 5, 100);
}

public static int calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) {
    if (gameOver) {
        int finalScore = score + (levelCompleted * bonus);
        System.out.println("Your final score was " + finalScore);
        return finalScore
    }
    return -1   // in the case of gameOver == false
} 
```


### method overload
* Same method name with different sets of arguments.
* should have unique method signiture.
* changing return type does not change the method signiture.


### Constants
* values cannot be changed
* assinged  in the class in the beginning
```java
public class Main {
    private static final String INVALID_VALUE_MESSAGE = "Invalid value";
    // ...
}
```
