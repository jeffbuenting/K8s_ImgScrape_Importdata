import csv
import paho.mqtt.client as mqtt
import argparse, sys
import time

def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass

if __name__ == "__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument("--inputfile", help="Input File")
    # parser.add_argument("--broker", help="MQ Broker")
    # parser.add_argument("--port", help="MQ Port")
    args=parser.parse_args()

    print("num args = ")
    print(args)
    print( "hello world if" )

    if args.inputfile != None:
        inputfile = args.inputfile
        # broker=args.broker
        # port=args.port

        print( "Reading input file and passing to MQTT...")
        
        # client= mqtt.Client("admin")
        # client.on_publish = on_publish
        # client.connect(broker,port)
        
        # with open(inputfile, newline='') as csvfile:
        #     inputdata = csv.DictReader(csvfile)
        #     for row in inputdata:
        #         print(row['Url'], row['Path'])
                #publish message
                # ret= client.publish("/data",row)

    else:
        raise Exception("Missing required input")
        # I = 0
        # while None == None:
        #     print( "No Input: {}".format(I))
        #     I += 1
        #     time.sleep(30)