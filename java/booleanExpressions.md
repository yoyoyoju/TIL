# boolean Expressions

* NOT (!)



### short circuit operators

* &&(and), ||(or)
    * left side of && is false: stops there
    * left side of || is true: stops there
    ```java
    if (refVar != null && refVar.isValidType()) {
        // if refVar is null,
        // does not evaluate the right side
        // -> does not throw NullPointerException
    }
    ```

### non short circuit operation
* &, |
* as boolean expressions, ther act like &&. ||
* EXCEPT that they force the JVM to always check both sides of the expression
* typically, &, | are used in another context, for manipulating bits


----
*headfirst java* chapter 6
