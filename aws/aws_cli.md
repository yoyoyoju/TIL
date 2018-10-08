# using aws CLI

### file commands for s3
```
aws s3 ls s3://mybucket
aws s3 cp myfolder s3://mybucket/myfolder --recursive
aws s3 sync myfolder s3://mybucket/myfolder --exclude *.tmp
```


-------
reference: [amazon](https://aws.amazon.com/cli/)
