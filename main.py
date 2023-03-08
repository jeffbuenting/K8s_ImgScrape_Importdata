# reads from a csv file and creates an object that will then be passed to the next container

import csv
import paho.mqtt.client as mqtt
import argparse, sys
import time





print("no input file specified.")
I = 0
while None == None:
    print( "No Input: {}".format(I))
    I += 1
    time.sleep(30)