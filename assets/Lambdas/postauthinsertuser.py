import mysql.connector
import json

mydb = mysql.connector.connect(
    host="223.190.15.34",
    user="atul",
    password="atul@123",
    database="talentum_dev"
)


def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    print(event)
    cur = mydb.cursor()
    sql = "INSERT IGNORE INTO user_details (user_name, email_id,user_type,phone) VALUES (%s, %s, %s,%s)"
    val = (event['userName'],event['request']['userAttributes']['email'],"C",event['request']['userAttributes']['phone_number'])
    cur.execute(sql,val)
    mydb.commit()
    a = ['lambda is working', 'great']
    jsonString = json.dumps(a)
    return event
