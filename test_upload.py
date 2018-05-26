import boto3

bucket_name = '203494-bucket'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

my_file = open('to_be_uploaded.txt' , 'w+')
my_file.write('Here will be my test content')
my_file.close

bucket.put_object(
    Key='omega/gammatest.txt', 
    Body=open('to_be_uploaded.txt', 'rb')
)
