# Lambda function Ex11
To make the application a distributed system: 
asynchronously process the photo label.
1. upload photo to S3 bucket
2. S3 bucket event notification triggers Lambda
3. Lambda talks to Rekognition to process the photo label

### start RDS instance

### allow access to Lambda
create NAT(network address translation) instance by updating CloudFormation stack.
It allows Lambda to access internet.
Putting Lambda in my VPC will make it lose internet access.
We need the access to communicate with Rekognition and RDS.
So, put a NAT instance in VPC.

* open CloudFormation dashboard
* choose the stack to add NAT
* update Stack at the top
* upload templete
* choose key pair

* open EC2 dashboard
* Instances in the left navigation menu: can see NAT instance


### IAM role for Lambda
to authenticate Lambda to talk to Rekognition and S3
* IAM dashboard
* create role
* trusted entity: Lambda
* attach policy:
    * LambdaVPCAccessExecutionRole
    * RekognitionReadOnlyAccess
    * S3ReadOnlyAccess
* role name : labels-lambda-role
* create role


### security group
create security group for lambda in VPC
* EC2 dashboard
* security groups from left navigation menu
* create security group

### modify security group for RDS
To allow it to communicate with Lambda function
* open RDS dashboard
* instances from left navigation menu
* under Details, Security and network click security group
* inbound on the bottom
* edit
* add rule
* Type: MySQL/Aurora
* Source: labels-lambda-sg
* save

### placeholder lambda function
create a placeholder Lambda function.
* Lambda dashboard
* create a function
* name, Runtime(python3.6)
* choose role
* create function
* under Network section choose VPC and subnet
* choose security group
* put in code
* save

### test
test the placeholder lambda by simulating an S3 event.
* open lambda dashboard
* functions on the left navigation menu
* click the function
* test on the top
* Event template: S3 Put, name -> create
* test

### code
the creating label part is done by Lambda (lambda_function.py)
```python
def lambda_handler(even, context):
    # this part process the label
    ...
```

### test locally
in the lambda code, simulate s3 event:(lambda_funcation.py)
```python
fake_s3_event = {
    # JSON snippet
    ...
}
fake_context = []
lambda_handler(fake_s3_event, fake_context)
```

### pack it and update
packaget the libraries and update the Lambda function
```
cd ~/environment
mkdir libraries
pip-3.6 install 'mysql_connector_python<8.1' -t libraries
cd libraries/
zip -r ~/environment/lambda.zip *
cd ~/environment/exercise-lambda/LambdaImageLabels/
zip ~/environment/lambda.zip *.py
cd ~/environment
aws lambda update-function-code --function-name labels-lambda --zip-file fileb://lambda.zip
```

### configure
* lambda dashboard
* functions from left navigation menu
* click the function
* Environment variables:
    * DATABASE_HOST
    * DATABASE_USER
    * DATABASE_PASSWORD
    * DATABSE_DB_NAME
* save

### test
* lambda dashboard -> functions
* choose my function
* drop-down list left to the Test button
* configure test events
* edit saved test events
* paste the test code of `fake_s3_event` from lambda_function.py
* save
* test

| I had an error message here saying timeOutError.
| It was from RDS instance did not allow lambda to write the labels,
| because I set the Inbound rule wrong.
| I set the wrong Type (should have been MYSQL/Aurora)

### s3 bucket to trigger
configure S3 bucket to trigger lambda function
* open S3 dashboard
* select the bucket
* Properties tab
* Advanced settings -> Events
* add notification
* Events: ObjectCreate(All)
* Send to: Lambda Function and choose the lambda
* save

### test the app
run the application.py

### stop the NAT instance

### stop the RDS instance

