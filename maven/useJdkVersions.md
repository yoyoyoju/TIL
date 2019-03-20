To use multiple versions of jdk

### using toolchain
* example of `toolchains.xml` in `~/.m2` directory
```xml
<?xml version="1.0" encoding="UTF8"?>
 <toolchains>
   <!-- JDK toolchains -->
   <toolchain>
     <type>jdk</type>
     <provides>
       <version>1.8</version>
       <vendor>AdoptOpenJdk</vendor>
     </provides>
     <configuration>
       <jdkHome>/Library/Java/JavaVirtualMachines/openjdk8/Contents/Home</jdkHome>
     </configuration>
   </toolchain>
   <toolchain>
     <type>jdk</type>
     <provides>
       <version>11</version>
       <vendor>AdoptOpenJdk</vendor>
     </provides>
     <configuration>
       <jdkHome>/Library/Java/JavaVirtualMachines/openjdk11/Contents/Home</jdkHome>
     </configuration>
   </toolchain>
 
 </toolchains>
```
* use the information of `~/.m2/toolchainx.xml` by pom.xml
    * be sure that the toolchains plugin is outside of pluginManagement
```xml
<?xml version="1.0" encoding="UTF-8"?>
 
 <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>
 
   <groupId>com.company</groupId>
   <artifactId>project</artifactId>
   <version>1.0-SNAPSHOT</version>
 
   <name>project</name>
   <url>http://www.example.com</url>
 
   <properties>
     <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
     <java.version>11</java.version>
     <maven.compiler.source>${java.version}</maven.compiler.source>
     <maven.compiler.target>${java.version}</maven.compiler.target>
   </properties>
 
  <buil>
    <plugins>
      <!-- use toolchains to specify JDK version -->
      <plugin> 
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-toolchains-plugin</artifactId>
        <version>1.1</version>
        <executions>
          <execution>
            <goals>
              <goal>toolchain</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <toolchains>
            <jdk>
              <version>${java.version}</version>
            </jdk>
          </toolchains>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```


### switch java home
* put following into `~/.bash_profile`
```shell
export JAVA_8_HOME=/Library/Java/JavaVirtualMachines/openjdk8/Contents/Home
export JAVA_11_HOME=/Library/Java/JavaVirtualMachines/openjdk11/Contents/Home

alias java8='export JAVA_HOME=$JAVA_8_HOME'
alias java11='export JAVA_HOME=$JAVA_11_HOME'

export JAVA_HOME=$JAVA_8_HOME
```
