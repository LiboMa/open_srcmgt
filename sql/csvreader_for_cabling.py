#!/usr/bin/env python


import csv
import cabling_model
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

    #print line['rack'],line['device_name'],line['he'],line['card'],line['slot'],line['port'],line['device_type'],line['cable_id'],line['vlan_id'],line['func']
    for k,v in line.items():
        print "%s:%s" %(k,v)
    print "======"
    cabling_model.new_cable(line)
    #cabling_model.new_tags(line['tagname'],line['approvedby'],status=line['status'],comment=line['comment'])

