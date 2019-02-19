# Wrapping a primitive 
* wrap a primitive when I want to use the value as an object
    * to put into a collection
* wrapping a value
    ```java
    int i = 288;
    Integer iWrap = new Integer(i);
    ```
* unwrapping a value
    ```java
    int unWrapped = iWrap.intValue();
    ```
* Autoboxing from Java5.0
    ```java
    ArrayList<Integer> listOfNumbers = new ArrayList<>();
    listOfNumbers.add(3); // autoboxing
    int num = listOfNumbers.get(0); // unboxing
    ```
    * For all the cases below, one can use areference to a wrapper, or a primitive of the matching type
        * Method arguments
            * `void takeNumber(Integer i)` or `void takeNumber(int i)`
        * return values
            * `int giveNumber() {return x;}` or `Integer giveNumber() {return x;}`
        * Operations on numbers
            * `Integer i = new Integer(3);i++;` `Integer k = i + 3;`
        * assignments
            * `Double d = x;`


### wrapper methods
* Wrapper classes have static utility methods
    ```java
    int x = Integer.parseInt("2");
    int x = Integer.parseInt("two");    // NumberFormatException!!!
    double d = Double.parseDouble("42.24");
    boolean b = Boolean.parseBoolean("True");   // ignores the cases of the characters
    ```
