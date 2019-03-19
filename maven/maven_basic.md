# Maven
[maven in 5 minutes](http://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)


* `$ mvn --version` to see the version

* create a project
    * example for app
`$ mvn archetype:generate -DgroupId=com.company -DartifactId=project -Dpackage=com.company.project -Dversion=1.0-SNAPSHOT -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false`
    * example for webapp
`$ mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-webapp -DgroupId=com.company.app -DartifactId=my-webapp`
    * (provided Archetypes)[https://maven.apache.org/guides/introduction/introduction-to-archetypes.html]

* `pom.xml` is the core of a project's configuration in maven

* to build `mvn package`
* for clean install `mvn clean install`
