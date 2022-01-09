import base64
import logging
import boto3
from botocore.exceptions import ClientError
import json

#rds settings
rds_host  = "database-1.xxxxxxxx.us-east-1.rds.amazonaws.com"
name = 'admin'
password = 'adminadmin'
db_name = 'test_rds'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# try:
#     conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
# except pymysql.MySQLError as e:
#     logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
#     logger.error(e)
#     sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
#Creating Session With Boto3.

def handler(event, context):
    print(event['requestContext']['authorizer']['claims']['cognito:username'])
    s3 = boto3.resource('s3')
    object = s3.Object('resumes.ap-south-1',event['requestContext']['authorizer']['claims']['cognito:username'])
    body = object.get()['Body'].read()
    myObj = base64.b64encode(body)
    responseBody = {
        "resume_base64": myObj.decode("utf-8")
    };
    jsonString = json.dumps(responseBody)
    return {
    'statusCode': 200,
    "headers": {
            "Access-Control-Allow-Headers": "Content-Type,Access-Control-Allow-Headers,X-Requested-With,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "GET, PUT, PATCH, POST, DELETE, OPTIONS",
            "Access-Control-Allow-Origin": "*"
        },
    'body': jsonString
    }