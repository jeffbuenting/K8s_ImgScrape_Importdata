





        client= mqtt.Client("admin")
        client.on_publish = on_publish
        client.connect(broker,port)
        
        with open(inputfile, newline='') as csvfile:
            inputdata = csv.DictReader(csvfile)
            for row in inputdata:
                print(row['Url'], row['Path'])
                #publish message
                ret= client.publish("/data",row)
    else:
        print("no input file specified.")
        I = 0
        while None == None:
            print( "No Input: {}".format(I))
            I += 1
            time.sleep(30)

    