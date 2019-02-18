# static

### static variable
* static variable
    * it is shared among all instances of the class
    * static variables are initialized when a class is loaded
        * before any object of that class can be created
        * before any static method of the class runs


### static initializer
* static initializer
    * a block of code that runs when a class is loaded, before any other code can use the class
    * for example, one can initialize a static final variable
    ```java
    public class Foo {
        // Constant variable names should be in all caps
        public static final double BAR_SIGN;
        static {
            BAR_SIGN = (double) Math.random();
        }

    }
