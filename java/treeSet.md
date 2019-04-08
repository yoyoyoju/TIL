# TreeSet

* java.lang.Object
    * java.util.AbstractCollection<E>
        * java.util.AbstractSet<E>
            * java.util.TreeSet<E>


###  comparable

* have to tell the TreeSet how to compare by one of the two way
    1. element type must implements Comparable
    2. pass Comparator into the TreeSet's constructor
* if the elements does not provide a way to compare, it fails at runtime.
* example:
    1. use Comparable
    ```java
    class Book implements Comparable {
        String title;
        public Book (String t) {
            title = t;
        }
        public int compareTo(Object b) {
            Book book = (Book) b;
            return (title.compareTo(book.title));
        }
    }
    // Book can be used in a TreeSet like:
    TreeSet<Book> tree = new TreeSet<Book>();
    tree.add(new Book("example book"));
    ```
    2. use Comparator
    ```java
    public class BookCompare implements Comparator<Book> {
        public int compare(Book one, Book two) {
            return (one.title.compareTo(two.title));
        }
    }
    class Test{
        BookCompare bCompare = new BookCompare();
        TreeSet<Book> tree = new TreeSet<>(bCompare);
        tree.add(new Book("example book"));
    }
    ```



---
reference: **headFirst java** chapter 16
