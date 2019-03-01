# Reading a file

### File API
* class File
    * constructor: File(String pathname)
    * the contents can be read using Scanner class
    * public Scanner (File source)
        * `import java.util.*`
        * `Scanner`'s method `nextLine()` does not reture a new line at the end
        * `hasNext()` boolean true if the file contains something more to read
        * `next()` reads the following word as String object
        * at the end we close the file using `close`
        * one can tell which character set to use:
            * `new Scanner(f, "UTF-8");` // use UTF-8 character set
            * use environment variable: JAVA_TOOL_OPTIONS "-Dfile.encoding=UTF8"
```java
    import java.io.File;
    // filename.txt in the project root
    File file = new File("filename.txt"); 

    // public Scanner (File source)
    Scanner reader = new Scanner(file);
    while (reader.hasNextLine()) {
        String line = reader.nextLine();
        System.out.println(line);
    }
    reader.close();
}
```
* Scanner(File source) throws FileNotFoundException
    * handle the exception:
    ```java
    public void readFile(File f) {
        Scanner reader = null;
        try {
            reader = new Scanner(f);
        } catch (Exception e) {
            System.out.println("error" + e.getMessage());
            return; // exit the method
        }
        while (reader.hasNextLine()){
            String line = reader.nextLine();
            System.out.println(line);
        }
        reader.close();
    }
    ```
    * or delegate the exception to the caller
    ```java
    public void readFile(File f) throws Exception {
        Scanner reader = new Scanner(f);
        while(reader.hasNextLine()) {
            String line = reader.nextLine();
            System.out.println(line);
        }
        reader.close();
    }
    ```



### using FileReader
* *headfirst java* ch14
* example code:
    ```java
    import java.io.*;

    class ReadAFile {
        public static void main(String[] args) {
            try {
                File myFile = new File("MyText.txt");
                FileReader fileReader = new FileReader(myFile);
                BufferedReader reader = new BufferedReader(fileReader);

                String line = null;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
                reader.close();

            } catch(Exception ex) {
                ex.printStackTrace(); 
            }
        }
    }
    ```
