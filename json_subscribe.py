#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import json
import boto3


#connecting with database Dyanamodb
db = boto3.resource('dynamodb',"us-east-1")
dT = db.Table('mohit_smgcl')

# creating client
mqttc = mqtt.Client()
# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add("json/data", on_message_msgs)
mqttc.on_message = on_message
# address to connect to broker
mqttc.connect("127.0.0.1")
mqttc.subscribe("json/data", 0)
mqttc.loop_forever()


def on_message_msgs(mosq, obj, msg):
    
    x = str(msg.payload.decode("utf-8"))
    json_convert = json.loads(x)
    # putting data into Dynamodb
    dT.put_item(
        Item={
            "vendor_code" : json_convert["data"]["vendor_code"],
            "vehicle_code": json_convert["data"]["vehicle_code"]
        }
    )

def on_message(mosq, obj, msg):
    
    print(msg.topic + " " + " " + str(msg.payload))
