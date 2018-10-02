# Week 2
* upload photos to S3 bucket using API
* tag using Rekognition

## API

### IAM set up Ex4
IAM: Identity and Access Management. Should not user the root user credentials. Rather create an AWS IAM user for neccessary permission.
* IAM user
    * permission policy: what the user can and cannot do in AWS
    * Access keys: access key ID and a secret access key


#### create a custum policy
* go to `IAM` dashboard
* `Policies` from left navigation menu: to create custum policy

#### create IAM user
create an user, attach a policy, generate the access keys
* IAM dashboard
* User from left navigation menu
* Add user
* User name
* choose access, Permission
* download csv

#### EC2 as IAM user
Launch EC2 instance as the created IAM user.
* login to the console as the user
* launch an instance in VPC
* connect to the instance using SSH

#### set up credential
* `aws configure`
* put the access key id and secret access key
* choose region
* choose default output format
* `aws ec2 describe-instances` : query the information about the instances in my account


### Install Boto3 aud explore Ex4
Boto3 is a SDK(software development kit).

#### install Boto3
```shell
sudo yum -y install python36
sudo pip-3.6 install boto3
```

#### using boto3
in python3
```python
import boto3
client = boto3.client('ec2')
client.describe_instances()
client.describe_key_pairs()
```
To quit, `Ctrl-D`


### Cloud9 Environment Ex5
* open `Cloud9` dashboard
* create environment
* Name
* Configure setting: Network settings (the VPC and subnet)


### explore
```shell
aws ec2 describe-instances
sudo  pip-3.6 install boto3
```
in python3 (make a file and run it)
```python3
import boto3
client = boto3.client('ec2')
client.describe_instances()
```

### S3 bucket
* `S3` dashboard
* create bucket
* bucket name
* region


### S3 uploader component



