# reads from a csv file and creates an object that will then be passed to the next container

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
    parser.add_argument("--broker", help="MQ Broker")
    parser.add_argument("--port", help="MQ Port")
    args=parser.parse_args()

    print("num args = ")
    print(args)

    if args.inputfile != None:
        inputfile = args.inputfile
        broker=args.broker
        port=args.port

        print( "Normal Processing")





print("no input file specified.")
I = 0
while None == None:
    print( "No Input: {}".format(I))
    I += 1
    time.sleep(30)