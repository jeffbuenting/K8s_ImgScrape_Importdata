import csv
import paho.mqtt.client as mqtt
import argparse, sys
import time

def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass

if __name__ == "__main__":
    print( "hello world function" )