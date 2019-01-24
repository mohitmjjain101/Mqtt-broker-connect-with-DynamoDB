import paho.mqtt.client as mqtt
import json

def on_connect(mqttc, userdata, flags,rc):
    if rc == 0 :
        mqttc.connected_flag = True
        print("connect ok")
    else:
        print("Bad connection Returned code = ",rc)

mqtt.Client.connected_flag=False
broker_address="127.0.0.1" 
mqttc = mqtt.Client("json")
mqttc.username_pw_set("poc", "smgcl")
mqttc.on_connect=on_connect

try:
    mqttc.connect(broker_address)
except:
    print("connection failed")

json_data=open("json_data.json").read()
mqttc.publish("sensor/data",json_data)
