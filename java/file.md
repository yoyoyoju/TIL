# File

### Read from a File
* use `Scanner` class
```java
File file = new file("file-name.txt");
Scanner reader = new Scanner(file);
while (reader.hasNextLine()) {
    String line = reader.nextLine();
    System.out.println(line);
}
reader.close();
```

* Exception handling
* Scanner Constructor throws a FileNotFoundException
* It should be
    * handled (by try and catch)
    * thrown forward
```java
// handle it by try catch block
public void readFile(File f) {
    Scanner reader = null;

    try {
        reader = new Scanner(f);
    } catch (Exception e) {
        System.out.println("We couldn't read the file. Error: " + e.getMessage());
        return; // we exit the method
    }

    while (reader.hasNextLine()) {
        String line = reader.nextLine();
        System.out.println(line);
    }

    reader.close();
}
```
```java
// delegate the responsibility to the caller
public void readFile(File f) throws FileNotFoundException {
    // the file we read
    Scanner reader = new Scanner(f);

    while (reader.hasNextLine()) {
        String line = reader.nextLine();
        System.out.println(line);
    }

    reader.close();
}
```

* Character Set Issues
    * to specify the character-set (for example UTF-8)
    `Scanner reader = new Scanner(file, "UTF-8");`


### Writing to a File
* `FileWriter` class

```java
FileWriter writer = new FileWriter("file.txt");
writer.write("Hi file!\n"); // line break has to be written
writer.write("add more");
writer.close(); // the call closes the file and makes sure the written text goes to the file
```

* FileWirter constructor and write method may throw an exception
    * has to be handled or delegated to the caller
```java
public class FileHandler {
    public void writeToFile(String fileName, String text) throws Exception {
        FileWriter writer = new FileWriter(fileName);
        writer.write(text);
        writer.close();
    }
}

// in the Main Class
 public static void main(String[] args) throws Exception {
        FileHandler handler = new FileHandler();
        handler.writeToFile("diary.txt", "Dear Diary, today was a nice day.");
    }
```

* additinal parameter boolean `append` (default false)
    * false: old content (if any) is erased and the new one is written
        `FileWriter writer = new FileWriter(filename);`
    * true: append text at the end of the already existing file
        `FileWriter writer = new FileWriter(filename, true);  //append=true`





# Related Classes

### Class File
* java.io.File
    * public class File extends Object implements Serializable, Comparable<File>
* method
    * String getName() : returns the name of the file or directory
    * String getPath() : converts this abstract pathname into a pathname string


###  Class Files
* java.nio.file.Files
    * public final class Files extends Object
    * since 1.7
* method
    * public static Stream<Path> walk(Path start, int maxDepth, FileVisitOption... options) throws IOException
    * public static Stream<Path> walk(Path start, FileVisitOption... options) throws IOException
        * example [(from stackOverflow)](https://stackoverflow.com/questions/1844688/how-to-read-all-files-in-a-folder-from-java)
        ```java
        try (Stream<Path> paths = Files.walk(Paths.get("/home/you/example"))) {
            paths
                .filter(Files::isRegularFile)
                .forEach(System.out::println);
        }
        ```
