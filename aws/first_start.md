# AWS first start
edX lecture: AWS Developer Building on AWS. Personal note from the lecture.

### sign up
Introduction to Exercise 1
* create a new AWS account (as free tier)
* set up a billing alert 
    * under `My Account`, `Preference`


### Amazon EC2
Introduction to Exercise 2
* using APIs
* need to set up
    * AMI (Amazon Machine Image)
    * instance type (Hardware profile)
    * security groups
    * storage
    * key pairs
* how to:
    * in the console, `EC2 Dashboard`
    * `Launch Instance`
    * choose AMI (Amazon Linux AMI)
    * choose Instance type
    * instance details
        * Advanced details, user data (these commands will be run when it launches)
    * storage
    * tags: user defined metadata for the instance (key: value pair)
    * security group: selete existing one? eipsq
    * key pairs: new one
    * launch
    * waite until the status checks changes from `initializing` to `2/2 checks passed`.
    * connect to the `IPv4 public IP` from a browser
* to connect
    * `chmod 400 path/to/yourkeyname.pem`
    * `ssh -i path/to/yourkeyname.pem ubuntu@12.123.123.123`
* to terminae
    * Service, EC2 for EC2 dashboard
    * Instances, select the one to terminate
    * Actions, Instance State, Terminate


### VPC
virtual private cloud. How the network traffic is routed. How the network connects or not to the internet.
* `cloudFormation`
* `create stack`
* choose a template: upload one
* then creat
* Go to VPC dashboard
* choose `Your VPCs` from left navigation menu
* write down the vpc-id
* choose `Subnet` from left navigation menu


### EC2 instance in a VPC
* choose AMI, Type
* from `Network` choose from previous VPC
* from `Subnet` choose from previous subnet
* Advanced Detail
* Tag
* Configure Security Group
* write down the IPv4 Public IP


### Connect to the EC2 instance
* `chmod 400 PATH-TO-PEM-FILE`
* `ssh -i PATH-TO-PEM-FILE ec2-user@PUBLIC-IP`


### View data
* `cat /var/log/cloud-init-output.log`  : log
* `curl http://169.254.169.254/latest/meta-data/`   : instance metadata
* `curl http://169.254.169.254/latest/dynamic/instance-identity/document`   : instance identity
* `curl http://169.254.169.254/latest/meta-data/public-ipv4`    : Public IP address
* `curl http://169.254.169.254/latest/meta-data/mac`    : MAC address
* `curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/Your-MAC/vpc-id`    
    * VPC ID (Your-MAC should be replace by real MAC address)
* `curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/Your-MAC/subnet-id` : subnet-id
* `curl http://169.254.169.254/latest/user-data` : user data


### Terminate

----------------
reference:
* edX AWS Developer: Building on AWS
* [about git install](devoncmather.com/setting-aws-ec2-instance-lamp-git/)
