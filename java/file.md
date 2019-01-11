
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
