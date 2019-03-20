# build plugins

### exec maven plugin
* for executing Java programs from Maven
* between `<mainClass></mainClass>` tags, provide the full name of the application
* `$ mvn exec:java` will execute the mainClass
* `$ mvn exec:java -q` to run in quiet mode (see only error messages)
```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>1.6.0</version>
      <configuration>
        <mainClass>com.example.Main</mainClass>
        <cleanupDaemonThreads>false</cleanupDaemonThreads>
      </configuration>
    </plugin>
  </plugins>
</build>
```

### to find lates version 
* to find latest plugin or dependency versions for your modules
* `$ mvn versions:display-plugin-updates`
* use `-N` flag like `$ mvn -N ...` from the projects root directory
    to just check the parent POM
```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>versions-maven-plugin</artifactId>
    <version>2.5</version>
    <configuration>
        <generateBackupPoms>false</generateBackupPoms>
    </configuration>
</plugin>
```
