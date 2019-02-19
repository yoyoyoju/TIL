# import

### import statics
```java
// old way
import java.lang.Math;
class NoStatic {
    public static void main(String[] args) {
        System.out.println("sqrt " + Math.sqrt(2.0));
    }
}
```
```java
// static import
import static java.lang.System.out;
import static java.lang.Math.*;
class WithStatic {
    public static void main(String[] args) {
        out.println("sqrt " + sqrt(2.0));
    }
}
