#!/usr/bin/env python
#
# This scripts is used to set config for source management.
# created on 2013-05-07
#
# update on 2013-6-25 add to db connection

import sys
import os
import web

# settings templates
# render = web.template.render('templates', base='base')
render = web.template.render('templates', base='base')
render_ori = web.template.render('templates',)
session = web.config.session

# - globals var for templates
web.template.Template.globals['render_ori'] = render_ori
web.template.Template.globals['render'] = render

# database

database='yourdatabase'
db_user='itadmin'
db_passwd='yourdbpassword'
db=web.database(dbn='mysql',db=database,user=db_user,passwd=db_passwd)

### Sessions ###
#if web.config.get('_session') is None:
#    store = web.session.DiskStore('sessions')
#    session = web.session.Session(app,store,initializer={'login':
#    0,'privilege':0})
#    web.config['_session'] = session
#else:
#    session = web.config._session
#print web.config._session.login

#store = web.session.DiskStore('sessions')
#session = web.session.Session(app,store,initializer={'login':'no','user_id':None, 'privilege':0})
#web.config.session = session
#web.template.Template.globals['session'] = session
