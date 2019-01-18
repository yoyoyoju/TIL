### Variable Number of Method Parameters
* how to pass an indefinite number of a specific type of parameters:
    * placing an ellipsis (`...`) after the parameter type
    `public int sum(int... values)` :as many integer parameters as the user wants 
    * the parameters can be handled as a table
    * a method can be assigned only one parameter which receives an indefinite number of values
    * the indefine number of variable shoud be the first parameter:
    ```java
    public void print(String... characterStrings, int times) // right
    public void print(int times, String... strings) // wrong
    ```
    * alternative approach would be using a list as a parameter

example
```java
public int sum(int... values) {
    int sum = 0;
    // the method has a table-like variable called values
    for(int i = 0; i<values.length; i++) {
        sum += values[i];
    }
    return sum;
}
// usage
sum(2, 3, 5, 2);
sum(1, 2);
```
------
reference
[mooc.fi, week12, 54.6](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)


