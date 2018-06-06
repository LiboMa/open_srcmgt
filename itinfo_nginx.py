#!/usr/bin/env python

######## Set environment for apache #####
import os
import sys

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
curdir=os.path.dirname(__file__)
sys.path.append(curdir)
sys.path.append(curdir+"controllers/admin")
os.chdir(curdir)
##########################################
import web
from config.urls import *
####### Set Apps #########################

web.config.debug = False
app = web.application(urls, globals())
application = app.wsgifunc()

###### Sessions ##########################

if web.config.get('session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app,store,initializer={'login':'no','user_id':None, 'privilege':0})
    web.config.session = session
else:
    session = web.config.session
web.template.Template.globals['session'] = session

if __name__ == '__main__':
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()

