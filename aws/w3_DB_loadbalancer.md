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


###
