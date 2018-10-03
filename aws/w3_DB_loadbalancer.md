# week3 Database and LoadBalancer

### RDS database instance Ex7
RDS: Relational Database Service
* open `RDS` dashboard
* `create database`
* check "only enable options eligible for RDS Free Usage Tier"
* choose `MySQL`
* Next Settings set:
    * DB instance identifier
    * Master username
    * password(make a note)
* Next advanced set up:
    * under network set VPC
    * database option: database name (make a note)
* Launch DB instance - takes some minutes
* make a note of the Endpoint


### modify security group Ex7
* Details, Security and network, chlick the security group
* make a note of the security group ID
* click `Inbound`
* edit
* in the source text box type `sq` pick the security group I want
* save


### using mySQL Ex7
`mysql -h $DATABASE_HOST -u web_user -p`
where DATABASE_HOST is the endpoint of RDS


### Stop the database instance Ex7
* open RDS dashboard
* instances
* action -> Stop


### start RDS database instance Ex8
* RDS dashboard
* choose stopped instance
* instance action -> start


### screate a security group Ex8
security group for the EC2 instance in the VPC.
* EC2 dashboard
* security groups from left navigation menu
* create security group
* set name, description, VPC (web-server-sq)
* Inbound -> add rule
    * allow HTTP and SSH


### modify RDS security group Ex8
allow RDS instance to communicate with the EC2 instance that is acting as the web server
* EC2 dashboard
* Security groups from lever navigation menu
* select the RDS security group
* Inbound -> Edit
* add rule
* Type: MySQL/Aurora
* Source: web-server-sq (set it in the previous step)
* save


### S3 for deployment artifacts Ex8
Create a S3 bucket to store the deployment artifacts
* S3 dashboard
* create bucket


### upload deployment package Ex8
uwsqi server hosts the Python Flask application. After zip the app upload it to the 
deploy s3 bucket:
`aws s3 cp ~/deploy-app.zip s3://DEPLOY_BUCKET_NAME/`


### create an IAM role Ex8
create an IAM role to authenticate the EC2 instance to download the deployment artifacts in S3 bucket.
* IAM dashboard
* Roles from left navigation menu
* create role
* select type of trusted entity: EC2-Allows EC2 instances to call AWS services on your behalf.
* Next: Permissions
* select the access I want to give (S3Full, RekognitionReadOnly)
* Next: Review
* type the name
* Create role


## create instances and deploy Ex8
* Create two EC2 instances
* install the application via user data script
    * script installs Python3 and dev tools, nginx web server, uwsgi app server
    * creates a directory for photos app
    * downloads the deployment package from the S3 bucket
    * installs the requirements as `requirements.txt`
    * starts nginx and uwsgi servers


### Create the first EC2 instance and deploy Ex8
* EC2 dashboard
* Launch Instance
* AMI, Instance Type
* Network, subnet - choose the proper VPC and subnet
* IAM role
* Advanced Details : put the script for deploy
* make a memo of IPv4 Public IP


### test Ex8
in a browser connect to the public IP from previous step


### Load Balancer Ex8
* EC2 dashboard
* Load Balancers from left navigation menu
* create load balancer
* Application load balancer and create
* Name, Scheme and listeners
* VPC
* Availability Zone and public subnet from each
* assign a security group: existing security group
* Target group
* add EC2 instances to target

* Target Groups -> Targets to check the target's health
* to connect Load Balancer's DNS name


### take one server down Ex8
* connect to the server via SSH
* `sudo rm -rf /photos/`
* ` sudo restart uwsgi`


### clean up Ex8
* terminate EC2 instances
* Delete load balance
* stop the RDS database instance

