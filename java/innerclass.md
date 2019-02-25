# inner class
* inner class
    * when is it useful?
        * to have different implementations of the same interface methods (like two button listeners)
        * need to act like two classes (`x.takeButton(new MyInnerButton())`)
            * outer and inner classes can be in different inheritance trees

### make an inner class from outside
```java
class Foo {
    public static void main(String[] args) {
        MyOuter outerObj = new MyOuter();
        MyOuter.MyInner innerObj = outerObj.new MyInner();
    }
}
```

----
*headfist java* ch12
