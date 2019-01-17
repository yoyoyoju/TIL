# enum
* enum
    * an enumerated type 
    * in addition to classes and interfaces, enumerated types are also a class type of their own
    * use when we already know the possible values of our variables
    * are defined with the keyword `enum`
    * are usually created in their own file, in the same way as classes and interfaces
    * [tutorial from Oracle](http://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
```java
public enum Suit {
    // lists its constant values
    // Enum constants are usually in capital letters
    DIAMONDS, SPADES, CLUBS, HEARTS
}
```
following Card class uses enum Suit:
```java
public class Card {
    private int value;
    private Suit suit;
    public Card(int value, Suit suit) {
        this.value = value;
        this.suit = suit;
    }
    @Override
    public String toString() {
        return suit + " " + value;
    }
    //...
}
```
usage of the Card class
```java
// in main method
Card first = new Card(10, Suit.HEARTS);
if (first.getSuit() == Suit.CLUBS) {
    System.out.println("It's clubs");
}
```

### Enum with object variables

#### Enumerated Type Constructor Parameters
* enum type can contain object variables
* the object variable values have to be set up in the constructor
* enum-type classes cannot have public constructors
```java
public enum Colour {
    // the constructor parameters are defined as constant values when they are read
    RED("red"), 
    GREEN("green"),
    BLUE("blue");

    // object variable
    private String name;

    // constructor
    private Colour(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}

// can be used as:
System.out.println(Colour.GREEN.getName());
```




### example
```java
interface IntegerMath {
    int operation(int a, int b);
}
 public enum Command {
     END("end", (a, b) -> (a)),
     SUM("sum", (a, b) -> (a + b)),
     DIFFERENCE ("difference" , (a, b) -> (a -b)),
     PRODUCT("product", (a, b) -> (a * b));

     private String value;
     private IntegerMath method;

     private Command (String value, IntegerMath mathMethod) {
         this.value = value;
         this.method = mathMethod;
     }   

     public String getSymbol() {
         return this.value;
     }   

     public IntegerMath getMethod() {
         return this.method;
     }   

     public static Command getCommand(String command) {
         for (Command c : Command.values()) {
             if (c.getSymbol().equalsIgnoreCase(command)) {
                 return c;
             }   
         }   
         return null;
     }   
 }   
```

------
reference
[mooc.fi week12](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
