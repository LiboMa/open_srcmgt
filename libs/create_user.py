#!/usr/bin/env python

import os
import sys
import hashlib

curdir=os.path.abspath(os.path.dirname(__file__))
os.chdir("..")
sys.path.append(os.path.abspath(os.path.curdir))

import model_debug

def newuser(username,password,alias):

    try:
        inputpassword=hashlib.md5(password).hexdigest()
        inputuser=username.lower()
        return model_debug.new_user(inputuser,inputpassword)
    except ValueError:
        return None

if __name__ == '__main__':
    username,password,alias = sys.argv[1],sys.argv[2],sys.argv[3]
    newuser(username,password,alias)

