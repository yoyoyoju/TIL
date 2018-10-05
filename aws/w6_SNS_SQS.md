# using SNS and SQS
To make more distributes and event driven, 
use SNS and SQS service.
* SNS: Amazon Simple Notification Service - 
issue event notification to a topic so that subscribers 
can get the notification.
* SQS: Amazon Simple Queue Service -
queuing messages to be pulled and processed by other services.

### start RDS instance

### Turn on the NAT instance
start the NAT instance from EC2 Instances.

### Create an SNS topic
Create a SNS Topic and update its permissions to allow S3 to publish an event.

* open SNS dashboard
* get started
* create topic with name
* Topic on the left navigation menu
* make a note of the topic ARN
* Actions -> Edit topic policy -> Advanced view
    ```JSON
    ...
    "Condition":
    {
        "ArnLike":
        {
  	    "aws:SourceArn": "arn:aws:s3:::YOUR_BUCKET_NAME"    # fill in the BUCKET_NAME
        }
    }
    ...
    ```
* update policy

### Update S3 event notification
Update S3 event notification to publish an event to the SNS Topic.
* S3 dashboard -> select my bucket
* Properties tab -> Advanced setting -> Events
* Delete the previous one going to Lambda
* add notification
    * events: objectCreate(all)
    * send to: SNS Topic
    * save

### Create an email subscription
* SNS dashboard
* Topics from left navigation menu and select the Topic
* Actions -> Subscribe to topic
    * Protocol : Email
    * Endpoint : my email address
    * Create subscription

### create SQS
Create SQS queue and update the queue permissions
* SQS dashboard
* get started now
    * queue name 
    * quick-create queue
    * details (make a note of the queue URL and ARN)
* Permissions tab at the bottom
    * Edit policy document(Advanced) and Save
    ```JSON
    ...
    "Id": "policy1"
    "Statement":
    [
        {
            "Sid": "sid1",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "SQS:SendMessage",
            "Resource": "YOUR_QUEUE_ARN",
            "Condition":
            {
                "ArnEquals":
                {
                    "aws:SourceArn": "YOUR_TOPIC_ARN"
                }
            }
        }
    ]
    ...
    ```

### Subscribe SQS queue to the SNS
* SNS dashboard -> Topics -> check the topic
* Actions -> Subscribe to topic
    * Protocol: Amazon SQS
    * Endpoint: SQS queue ARN
    * create subscription

### update Lambda to subscribe to SNS
* Lambda dashboard -> Function -> select the Lambda
* add triggers list, scroll down, select SNS
* configure triggers
* Add
* save

### Lambda function
Lambda function receives SNS event notification when photo is uploaded to S3 bucket.
Then it talks to Rekognition to process the labels and update it into RDS.

```python
s3_event = json.loads(event['Records'][0]["Sns"]["Message"])
bucket = s3_event['Records'][0]["s3"]["bucket"]["name"]
key = s3_event['Records'][0]["s3"]["object"]["key"]
print("Received event. Bucket: [%s], Key: [%s]" % (bucket, key))
```

using AWS CLI, update Lambda function:
`aws lambda update-function-code --function-name labels-lambda --zip-file fileb://lambda.zip`

### test SQS queue
boto3 client for long-polls the queue for an incoming message. 
From the message, the client extracts imformations: message body, S3 object key, object size.
```python
sqs = boto3.client('sqs')
response = sqs.receive_message( 
    QueueUrl=queue_url, 
    WaitTimeSeconds=20
)
# then process response
sqs.delete_message(
    QueueUrl=queue_url, 
    ReceiptHandle=receipt_handle
)
```

### Stop NAT instance

### Stop RDS instance

-------

### To delete the rescources from this course
* RDS: delete the edx-photos-db RDS instance
* Lambda: delete the labels-lambda function (this delete the database security group)
* VPC: delte labels-lambda-sg security group
* VPC: web-server-sg security group
* Cloud9: delete BuildingOnAWS environment
* CloudFormation: delete edx-vpc-stack CloudFormation stack (this delete NAT instance)
* SNS: delete the uploads-topic SNS topic
* SQS: uploads-queue SQS queue
* S3: delete S3 photos and deployment buckets
* Cognito: delete the photos-pool userpool
