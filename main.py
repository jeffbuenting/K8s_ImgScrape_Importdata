import csv
import paho.mqtt.client as mqtt
import argparse, sys
import time
        
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True

def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass

if __name__ == "__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument("--inputfile", help="Input File" )
    parser.add_argument("--broker", help="MQ Broker",required=False)
    parser.add_argument("--port", help="MQ Port",required=False)

    args=parser.parse_args()

    print("num args = ")
    print(args)

    if args.inputfile != None:
        inputfile = args.inputfile

        print( "Reading input file and passing to MQTT...")

        if args.broker != None and args.port != None:
            broker=args.broker

            mqtt.Client.bad_connection_flag=False

            # and convert string to int as docker env vars must be string
            port=int(args.port)

            client= mqtt.Client()
            client.on_publish = on_publish
            client.connect(broker,port)

             #
            while not client.connected_flag and not client.bad_connection_flag: #wait in loop
                print("In wait loop")
                time.sleep(1)
                
            if client.bad_connection_flag:
                client.loop_stop()    #Stop loop
                sys.exit()

        else:
            print("MQTT broker or port is missing. writing file contents only.")
        
        with open(inputfile, newline='') as csvfile:
            inputdata = csv.DictReader(csvfile)
            for row in inputdata:
                print(row['Url'], row['Path'])

                if args.broker != None and args.port != None:
                    # publish message
                    print("Publishing to MQTT.")
                    ret= client.publish("/data",row)

    else:
        raise Exception("Missing required input")
