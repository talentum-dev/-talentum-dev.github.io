import sys
import base64
import logging
import json
import boto3
import mysql.connector

mydb = mysql.connector.connect(
    host="223.190.15.34",
    user="atul",
    password="atul@123",
    database="talentum_dev"
)


def lambda_handler(event, context):
    print(event)
    # cur = mydb.cursor()
    # sql = "INSERT IGNORE INTO user_details (user_name, email_id,user_type,phone) VALUES (%s, %s, %s,%s)"
    # val = (event['userName'],event['request']['userAttributes']['email'],"C",event['request']['userAttributes']['phone_number'])
    # cur.execute(sql,val)
    # mydb.commit()
    
#     skill tagline logic
# 	{
# 		fetch tagline id from table skills_tagline
# 		update user_skills_tagline table with user id and latest tagline. there can be only one tagline per user
# 	}
#     skills logic
# 	{
# 		1 => for each skill fetch their ids into an array from table skills
# 		delete all skills for the user from table user_skills
# 		insert skills ids from 1 into user_skills
# 	}

    event_json = json.loads(event.get('body'));
    print(event_json['tagline'])
    print(event_json['skills'])
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