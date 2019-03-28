# plugins for reporting
put under `<project><reporting><plugins>`.

### javadoc

Put the plugin in `<build>` also. (The version should match)
To use , `mvn javadoc:javadoc`
```xml
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-javadoc-plugin</artifactId>
        <version>3.1.0</version>
        <configuration>
        </configuration>
      </plugin>
    </plugins>
  </reporting>

  <build>
    <plugins>
        <!-- javadoc for documentation -->
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-javadoc-plugin</artifactId>
          <version>3.1.0</version>
        </plugin>
    </plugins>
  </build>
```
