import sys
import base64
import logging
import json
import boto3
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
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    # cur = conn.cursor()
    # cur.execute("select * from testuser")
    # query_results = cur.fetchall()
    # print(event)
    event_json = json.loads(event.get('body'));
    # print(event_json['user_name'])
    # print(event_json['file'])
    remove_header = event_json['file'].split(",")[1:2]
    listToStr = ' '.join(map(str, remove_header))
    string_to_byte = bytes(listToStr,'utf-8')
    print(string_to_byte)
    f=base64.b64decode(string_to_byte)
    s3 = boto3.resource('s3')
    object = s3.Object('resumes.ap-south-1', event_json['user_name'])
    result = object.put(Body=f)
    a = ["lambda is working fine"]
    jsonString = json.dumps(a)
    return {
    'statusCode': 200,
    "headers": {
            "Access-Control-Allow-Headers": "Content-Type,Access-Control-Allow-Headers,X-Requested-With,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "GET, PUT, PATCH, POST, DELETE, OPTIONS",
            "Access-Control-Allow-Origin": "*",
        },
    'body': jsonString
    }