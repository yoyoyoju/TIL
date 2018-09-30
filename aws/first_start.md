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
* to terminae
    * Service, EC2 for EC2 dashboard
    * Instances, select the one to terminate
    * Actions, Instance State, Terminate
