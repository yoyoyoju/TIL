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


