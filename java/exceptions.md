# Exceptions

### handling exceptions
* when things are not as we expected: throw an exception
* `NullPointerException`, `IndexOutOfBoundsException`, etc.
* handling exception using `try{ } catch (Exception e) { }`
```java
// example of parseInt and NumberFormatException
try {
    int num = Integer.parseInt(reader.nextLine());
} catch (Exception e) {
    System.out.println("is not proper number");
}
```

### throwing exceptions
* handle the exception:
    * try-catch
    ```java
    try {
        Thread.sleep(1000);
    } catch (Exception e) {
    }
    ```
    * throws Exception:
        * avoid to handle the exceptions in the method
        * delegate the responsibility to the caller
        * even the mein method can delegates it: the exceptions will interrupt the program
        * `public static void main(String[] args) throws Exception {}`
    ```java
    public void sleep(int sec) throws Exception {
        Thread.sleep(sec * 1000);
    }
    ```
* throw an exception ourselves
    * `throw new NumberFormatException()`
    * IllegalArgumentException: to make sure the conditions for parameters are met.
    ```java
    public Grade(int grade) {
        if (grade < 0 || grade > 5) {
            throw new IllegalArgumentException("The grade has to be between 0-5");
        }
        this.grade = grade;
    }
    ```
