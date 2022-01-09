import mysql.connector
import json

mydb = mysql.connector.connect(
    host="223.190.15.34",
    user="atul",
    password="atul@123",
    database="talentum_dev"
)

def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    print(event)
    cur = mydb.cursor()
    sql = """SELECT user_id FROM user_details WHERE user_name = %s"""
    val = event['userName']
    cur.execute(sql,(val,))
    user_id = [x[0] for x in cur.fetchall()][0]
    print(user_id)
    event["response"]["claimsOverrideDetails"] = { 
        "claimsToAddOrOverride": { 
            "user_id": user_id 
            }
        } 
    return event
