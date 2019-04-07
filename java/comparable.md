# Comparable interface

* has a method compareTo (only one way to compare)
* used for `Collections.sort`
* java.lang.Comparable
    ```java
    public interface Comparable<T> {
        /**
         * Returns a negative integer, zero, or a positive integer
         * as this object is less than, equal to, or greater than
         * the specified object.
         */
        int compareTo(T o);
    }
    ```
* example:
    ```java
    class Hand implements Comparable<Hand> {
    //...
        @Override
        public int compareTo(Hand other) {
            return this.value - other.getValue();
        }
    ```



----
see also:
[comparable](comparable.md)
