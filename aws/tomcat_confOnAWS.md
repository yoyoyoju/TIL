# tomcat on AWS

### install Tomcat on EC2 instance
* launch ec2 instance
* configure security groups
    * create a security Group with
        * set SSH rule
        * ALL ICMP rule (for enabling ping)
        * custom TCP rule for port 8080
        * HTTP, HTTPS rules
    * assign the security group to the instance
* download and install jdk8
* download and install, configure tomcat9
