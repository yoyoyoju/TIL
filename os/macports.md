# MacPorts

### port command
* `$ sudo port selfupdate`
* `$ sudo port reclaim` to reclaim space by uninstalling inactive ports
    * `$ port reclaim --disable-reminders` to disable the remainder
    * `$ port reclaim --enable-reminders` to enable the remainder
* `port search`
    * `$ port search --name --glob 'php*'`
* `port deps` to list dependencies
* `port install`
    * `$ sudo port install apache2 -preforkmpm +Workermpm`
    * if the installation fail should clean and try again
    * `$ sudo port clean portname`
* `port uninstall`
    * `$ sudo port uninstall portname`
    * `$ sudo port uninstall HexFiend @2.1.2_1` to specify the version
* `port installed` to see installed versions
* `port outdated`
* `port upgrade`
    * `$ sudo port upgrade outdated`
* find all ports that depend on a given other port
    * `port echo depends:portname`
    * `port dependents portname` among installed
    * `port rdependents libksba` recursive version of dependents
    * `port installed requested and rdependentof:portname`
* leaves: not requested (not been manually installed) and do not have any dependents
    * `port echo leaves`
    * `sudo port uninstall leaves`
    * `sudo port_cutleaves` do it iterativly
* `port installed requested` manually installed ports
* `sudo port unsetrequested portname` set the port as unrequested
* `sudo port select --set python python36`


### common tasks
```shell
sudo port selfupdate
port outdated
sudo port upgrade outdated
port installed inactive
sudo port uninstall inactive
```


