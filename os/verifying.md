# verifying the integrity of the files
[link](https://www.apache.org/dyn/closer.cgi/incubator/netbeans/incubating-netbeans/incubating-10.0/incubating-netbeans-10.0-bin.zip)

* download KEYS and asc signature file
```shell
% gpg --import KEYS
% gpg --verify downloaded_file.asc downloaded_file
```

* alternatively, verify the hash
    * the hash depends on the provieded SHA file
```shell
% gpg --print-md SHA1 downloaded_file
```
* compare the output to the content of the provided SHA1 file
