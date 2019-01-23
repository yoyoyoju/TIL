### install python3
* managing software using macport[:more info](https://guide.macports.org)

* install
install python3 using macports:
```shell
sudo port install python36
sudo port select --set python3 python36
python -V       # to check the version
sudo port install py36-numpy py36-scipy py36-matplotlib py36-pandas py36-statsmodels py36-pip
# sudo port select --set pip pip36    #  did not work
# sudo pip install -U scikit-learn    # 
sudo pip-3.6 install -U scikit-learn
```
* port search : to search a specific softward 
    * `--name` search only ports' names
    * `--glob` treat the search string as glob search string (expand wildcards) (default)
    * `--line` compact output
    * `--regex` regular expression
`$ port search --name --line 'php*`

* uninstall
    `sudo port uninstall portname`



