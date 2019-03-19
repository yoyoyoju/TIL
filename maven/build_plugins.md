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
