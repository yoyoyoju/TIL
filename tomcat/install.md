# Tomcat install
* Tomcat 9.0 install
    * JDK 8 or Later installed
    * download binary distribution from [apche tomcat](https://tomcat.apache.org/)
    * verify the file by gpg [(see example)](https://www.apache.org/dyn/closer.cgi/incubator/netbeans/incubating-netbeans/incubating-10.0/incubating-netbeans-10.0-bin.zip)
    * change permision of sh files in bin
        `$ chmod +x *.sh`
    * configure Environment variables:
        * `CATALINA_HOME` root directory of the binary distribution of Tomcat
        * `CATALINA_BASE` (optional, default=CATALINA_HOME) root dir of the active configuration
        * `JAVA_HOME` specify the location of a JDK
        * `bin/catalina.sh` has more environment variables
            * `CATALINA_OPTS` additional options for java command that starts Tomcat (such as memory limits)
            * `JAVA_OPTS` options to start and stop Tomcat
            * `CATALINA_PID` (on *nix only) where process id of the forked Tomcat java process will be written
    * ways to set the Environment variables:
        * These environment variables can be specified in the `setenv.sh` script
            * it is placed either into
                * `CATALINA_BASE/bin` (preferred, if both exists) or,
                * `CATALINA_HOME/bin`
            * the file should be readable
            * `CATALINA_HOME` and `CATALINA_BASE` variables cannot be configured, cause they are used to locate that file
            * example `$CATALINA_BASE/bin/setenv.sh`
            ```shell
            JRE_HOME=/usr/java/latest/
            CATALINA_PID="$CATALINA_BASE/tomcat.pid"
            ```
        * set the variables by editting the `bin/catalina.sh`
        * set the variables before execute the Tomcat
            `CATALINA_BASE=/tmp/tomcat_base1 bin/catalina.sh start`
        * write a script to start the tomcat [(ref)](https://stackoverflow.com/questions/6172258/how-to-set-java-home-or-catalina-home-if-i-have-more-than-1-version-used-for-pro)
            ```shell
            JAVA_HOME=/path/to/jdk
            CATALINA_HOME=/path/to/tomcat/installation
            CATALINA_BASE=/home/web1/
            export JAVA_HOME JAVA_OPTS CATALINA_HOME CATALINA_BASE
            $CATALINA_HOME/bin/catalina.sh start
            ```
    * more `README.md` and `RUNNING.txt` files in the tomcat distribution
