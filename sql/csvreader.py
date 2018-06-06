#!/usr/bin/env python


import csv
import model
import sys
test_file = sys.argv[1]

# keys : Comment
#Logical_Name
#Layout
#Serials_Number
#Hardware_Info
#Device_Type

#logic_name, device_type, serial_number, hardware_info="NULL",layout="NULL",status="NULL",history="NULL")


csv_file = csv.DictReader(open(test_file,'rb'), delimiter=',', quotechar='"')

for line in csv_file:

    #print line['Logical_Name'],line['Device_Type'],line['Serials_Number'],hardware_info=line['Hardware_Info'],layout=line['Layout'],status='online',history=line['Comment']
    model.new_asset(line['Logical_Name'],line['Device_Type'],line['Serials_Number'],hardware_info=line['Hardware_Info'],layout=line['Layout'],status='online',history=line['Comment'])

