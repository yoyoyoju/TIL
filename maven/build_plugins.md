# build plugins

Be careful where to put. 

```xml
<project>
  <build>
    <plugins>
      <plugin>
        <!-- ... -->
      </plugin>
    </plugins>
  </build>
</project>
```

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

### jetty

To use jetty to try out servlets.
To use: `mvn jetty:run` will run the jetty, and access to `localhost:8080` from your browser.

```xml
        <!-- to enable jetty -->
        <plugin>
          <groupId>org.mortbay.jetty</groupId>
          <artifactId>maven-jetty-plugin</artifactId>
          <version>6.1.10</version>
          <configuration>
            <scanIntervalSeconds>10</scanIntervalSeconds>
            <connectors>
              <connector implementation="org.mortbay.jetty.nio.SelectChannelConnector">
                <port>8080</port>
                <maxIdleTime>60000</maxIdleTime>
              </connector>
            </connectors>
          </configuration>
        </plugin>

```

### javadoc

To use javadoc for documentation, use the build plugin and add reporting plugin, too.
To make the documentation site: use `mvn javadoc:javadoc`.
```xml
        <!-- javadoc for documentation -->
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-javadoc-plugin</artifactId>
          <version>3.1.0</version>
        </plugin>

```


### for web app

For web app, one needs to package to war file.
To use, `mvn war:war`
```xml
        <!-- for web app -->
        <plugin>
          <artifactId>maven-war-plugin</artifactId>
          <version>3.2.2</version>
          <configuration>
            <webResources>
              <resource>
                <directory>src/main/ebextensions</directory>
                <targetPath>.ebextensions</targetPath>
                <filtering>true</filtering>
              </resource>
            </webResources>
          </configuration>
        </plugin>

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
