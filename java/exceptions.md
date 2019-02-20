# Exceptions

### Excpetion
* type Exception
    * class Throwable
        * getMessage() method
        * printStackTrace() method
    * Exception extends Throwable
    * RuntimeException extends Exception
        * they are not checked by the compiler: unchecked exceptions
        * compiler does not check to throw, catch and declare
        * ClassCastException, NullPointerException, etc
    * compiler checks for everything except RuntimeException
        * IOException, InterruptedException, etc

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
* try block must be followed by either a catch or a finally
    * try with only a finally (no catch) must still declare the exception
* finally block
    * no matter the try block fails or succeeds, the finally block runs
    * if the try or catch block has a return statement, finally will still run
        * Flow jumps to the finally, then back to the return

### throwing exceptions
* handle the exception:
    * try-catch
        * all the declared exceptions should be handled
        * multiple catch blocks must be ordered from smallest to biggest
    ```java
    try {
        Thread.sleep(1000);
    } catch (Exception e) {
        // runs only if an Exception is thrown
        e.printStackTrace();
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
    * in the case of multiple exceptions, all of them should be declared. (or use superclass of them)
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
