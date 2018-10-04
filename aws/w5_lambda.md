# Lambda function
To make the application a distributed system: 
asynchronously process the photo label.
1. upload photo to S3 bucket
2. S3 bucket event notification triggers Lambda
3. Lambda talks to Rekognition to process the photo label

### start RDS instance

### allow access to Lambda
create NAT instance by updating CloudFormation stack.
It allows Lambda to access internet.
Putting Lambda in my VPC will make it lose internet access.
We need the access to communicate with Rekognition and RDS.
So, put a NAT instance in VPC.

