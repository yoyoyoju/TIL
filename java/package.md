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
* jar it
    * `MyProject/classes/`
    * `$ jar cMf myjar.jar com`
        * `M` flag will create the jar file without the manifest
    * `$ jar -tf myjar.jar` - to list

### use the package
* in the code :
    * `import com.example.myexamplepackage.MyClass;`
* compile
    * `javac -cp '.:myjar.jar' Main.java`
* run
    * `java -cp '.:myjar.jar' Main`
* cp for classpath
