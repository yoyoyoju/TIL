# package

### make a jar
* put the package name in java files
    * `package com.example.myexamplepackage;`
* make the corresponding directory to the name of package
    * `MyProject/src/com/example/myexamplepackage/`
* put the codes in the right place
    * `MyProject/src/com/example/myexamplepackage/` - here the java files
* in the source code directory
    * `MyProject/src/`
    * `$ javac -d ../classes com/example/myexamplepackage/*.java`
        * `-d` flag: where to put the compiled code
* jar it
    * `MyProject/classes/`
    * `$ jar cMf myjar.jar com`
        * `M` flag will create the jar file without the manifest
    * `$ jar -tf myjar.jar` - to list


### make JAR executable

* need to create a **manifest** file
    * `manifest.txt` file states which class has the `main()` method
        * press the return key after typing the Main-Class line, or your manifest may not work correctly.
        * put the manifest file into the "classes" directory, where all other `.class` files are.
        ```txt
        Main-Class: MyApp
        ```
* run the jar tool to create a JAR file that contains everything in the classes directory, plus the manifest
    ```shell
    % cd MyProject/classes
    % jar -cvmf manifest.txt app1.jar *.class
    ```
* Run the executable JAR
    ```shell
    # in the directory where the JAR is
    % java -jar app1.jar    # -jar flag for jar file
    ```
    * the JVM does not dig into other directories (the class file should be right there)
    * if the class is part of a package, JVM looks only in the directories that match the package statement.



### use the package
* in the code :
    * `import com.example.myexamplepackage.MyClass;`
* compile
    * `javac -cp '.:myjar.jar' Main.java`
* run
    * `java -cp '.:myjar.jar' Main`
* cp for classpath


--- 
reference: **headfirst java** chapter 17
