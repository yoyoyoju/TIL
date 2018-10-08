# managing java

### installing
install from `tar.gz`
```shell
tar -xvf jdkfile.tar.gz
sudo mkdir -p /usr/lib/jvm/jdk-11/          # create dir to store java
sudo mv jdk-11/* /usr/lib/jvm/jdk-11/       # move java to the dir
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk-11/bin/java" 1010
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk-11/bin/javac" 1010
```



### change default version
```shell
sudo update-alternatives --config java
```
will show available version and you can choose which one to set as the default.
[reference](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-18-04)



