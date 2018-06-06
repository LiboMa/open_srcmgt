#!/usr/bin/env python

import os
import sys
import hashlib

curdir=os.path.abspath(os.path.dirname(__file__))
os.chdir("..")
sys.path.append(os.path.abspath(os.path.curdir))

import model_debug
#f=open(sys.argv[1],'r')

def insert_db(_file_):
    f=open(_file_, 'r')
    for line in f.readlines():

        if not line.startswith("#"):
            entry=line.strip("\n").split()
            hostname=entry[0]
            eth0=entry[1]
            eth1=entry[2]
            hosted=entry[5]
            gateway=entry[6]
            project=entry[7]
            dmz=entry[8]
            datacenter=entry[9]
            status=entry[-1]
            os=entry[4]
            eth2=entry[3]
            eth0_vlan="null"
            eth1_vlan="null"
            #print hostname, eth0, eth1, eth2, os, hosted, gateway, project, dmz, datacenter, status
            #continue
     #hostname, eth0, eth1, gateway, project, dmz, datacenter,hosted='NULL',eth0_vlan='NULL', eth1_vlan='NULL',type='NULL',eth2='NULL',os='NULL', status='NULL'

            try:
                model_debug.new_host(hostname, eth0, eth1, gateway, project, dmz,datacenter,hosted,eth0_vlan, eth1_vlan, 'vhost', eth2,os,status)
            except:
                print "DB Error"


if __name__ == '__main__':

    insert_db("./libs/lsi_server.txt",)


