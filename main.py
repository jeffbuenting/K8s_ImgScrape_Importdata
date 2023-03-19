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
    print( "hello world args" )