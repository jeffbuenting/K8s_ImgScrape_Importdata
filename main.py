# reads from a csv file and creates an object that will then be passed to the next container
import csv
import paho.mqtt.client as mqtt

def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass

if __name__ == "__main__":
    inputfile = "c:\\temp\\input.csv"
    broker="192.168.1.184"
    port=1883

    client= mqtt.Client("admin")
    client.on_publish = on_publish
    client.connect(broker,port)
    
    with open(inputfile, newline='') as csvfile:
        inputdata = csv.DictReader(csvfile)
        for row in inputdata:
            print(row['Url'], row['Path'])
            #publish message
            ret= client.publish("/data",row)

    