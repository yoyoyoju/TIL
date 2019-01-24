# mistakes

### java version
```
java.lang.UnsupportedClassVersionError: Ch1Servlet has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0 (unable to load class [Ch1Servlet])
```
It basically means the class file was compiled by jdk11, and the tomcat (which uses jdk1.8) cannot use the class file.
So, the source code should be compiled by proper jdk version.
To do so, have to set 
`$ export JAVA_HOME=/path/to/proper/jdk/version/Contents/Home`
before compile the source code.
One can put it into the ~/.bash_profile file like this too:
```bash
alias j8="export JAVA_HOME=`/usr/libexec/java_home -v 1.8`; java -version"
```

### using BASE
I tried to use CATALINA_BASE but it did not really work well for unknown reason...
I just use CATALINA_HOME as CATALINA_BASE

