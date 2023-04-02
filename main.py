import csv
import paho.mqtt.client as mqtt
import argparse, sys
import time
import json

# ----- MQTT Call Back functions
def on_connect(client, userdata, flags, rc):
    # https://pypi.org/project/paho-mqtt/#on-connect
    match rc:
        case 0:
            print(f"RC = {rc}: Connection Successful.")
            client.connected_flag=True
        case 1:
            print(f"Error Connecting: RC = {rc}: Invalid Protocl Version.")
            client.loop_stop()
            sys.exit()
        case 2:
            print(f"Error Connecting: RC = {rc}: Invalid Client Identifier.")
            client.loop_stop()
            sys.exit()
        case 3:
            print(f"Error Connecting: RC = {rc}: Server Unavailable.")
            client.loop_stop()
            sys.exit()
        case 4:
            print(f"Error Connecting: RC = {rc}: Bad Username or Password.")
            client.loop_stop()
            sys.exit()
        case 5:
            print(f"Error Connecting: RC = {rc}: Not Authorized.")
            client.loop_stop()
            sys.exit()
        case _:
            print( f"Error Connection: RC = {rc}: Currently Unused code.")
            client.loop_stop()
            sys.exit()

def on_publish(client, userdata, mid):
    print("message published." )

def on_disconnect(client, userdata, rc):
    print(f"disconnected OK: RC = {rc}")

# ----- Main
if __name__ == "__main__":  
    # process inputs
    parser=argparse.ArgumentParser()

    parser.add_argument("-i","--inputfile", help="Input File",required=True)
    parser.add_argument("-b","--broker", help="MQ Broker",required=True)
    parser.add_argument("-p","--port", help="MQ Port",required=True)
    parser.add_argument("-r","--retainflag", help="MQ Publish Flags",required=False,default="False")
    parser.add_argument("-c","--cleansessionflag", help="MQ Clean Session Flag",nargs='?',default="True")

    args=parser.parse_args()

    print("argments:")
    print(args)

    # assign to local vars
    inputfile = args.inputfile
    broker = args.broker
    port = int(args.port)
    retainflag = args.retainflag.lower() in ['true','1']
    cleansessionflag = args.cleansessionflag.lower() in ['true','1']

    # Initialize Client 
    mqtt.Client.connected_flag=False

    client = mqtt.Client("imginput1") 

    # callbacks
    client.on_connect=on_connect  
    client.on_publish=on_publish
    client.on_disconnect=on_disconnect
    
    

    print("Connecting to broker ",broker)
    client.connect(broker,port)    

    client.loop_start()
    

    # Wait for client to connect
    while not client.connected_flag: 
        print("In wait loop")
        time.sleep(1)

    
    print("in Main Loop")
    with open(inputfile, newline='') as csvfile:
        inputdata = csv.DictReader(csvfile)
        for row in inputdata:
            # publish message
            print("Publishing to MQTT.")
            print(row['Url'], row['Path'])
            
            jsondata = json.dumps(row)

            ret = client.publish("/imgscrape/input",jsondata,retain=retainflag,qos=2)

    client.disconnect() 
    client.loop_stop() 
    print("End MQTT Loop")
