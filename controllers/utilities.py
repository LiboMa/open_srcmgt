import web
import forms
import model
from config.settings import render, render_ori

##### Utils #######

class GEN_Password:

    def __init__(self):

        self.form=forms.generate_password()

    def GET(self):
        return render.generate(self.form)

    def POST(self):
        import string
        import random
        chars = string.digits + string.letters + "_-+!#^"
        try:
            length = web.input().length
            password = "".join(random.choice(chars) for i in range(int(length)))
            self.form=forms.generate_password(password)
            return render.generate(self.form)
        except Exception:
            return render.generate(self.form,title="Length must be notnull!")

class opsapi:

    def GET(self):
        ''' This func is used to return server configurations from db '''
        try:
            data = web.input()
        except AttributeError, e:
            return None
        if data.getinfo == 'all':
            rst = model.get_allentries()
        elif data.getinfo == 'vhost':
            rst = model.get_entries(type='vhost')
        elif data.getinfo == 'host':
            rst = model.get_entries(type='host')
        else:
            return None
        return render_ori.rawdata(rst,None)

class Send_msg:

    def GET(self):
        '''This func is used to handle server api from sitescope '''

        try:
            data = web.input()
        except AttributeError, e:
            return None
        try:
            fb=open('/tmp/warning_msg','a+')
        except IOError, e:
            return e
        if data.contact and data.msg:
            import time
            dt = time.strftime("%F %T")
            msg = "%s: Number: %s MSG: %s\n"%(dt,data.contact,data.msg)
            fb.writelines(msg)
        else:
            return None
        fb.close()

    def POST(self):
        '''This func is used to handle server api from sitescope '''

        try:
            data = web.input()
        except AttributeError, e:
            return None
        try:
            fb=open('/tmp/warning_msg','a+')
        except IOError, e:
            return e
        group=data.Group
        monitor=data.Monitor
        status = data.Status
        sample = data.Sample
        wtime = data.Time
        category = data.category
        import time
        dt = time.strftime("%F %T")
        w_msg = "Group:%s, monitor: %s, status: %s,sample:%s, time:%s\n Category: %s" %(group, monitor, status, sample, wtime, category)
        msg = "%s: Number: %s MSG: %s\n"%(dt,data.contact,w_msg)
        fb.writelines(msg)
        fb.close()

class check_ajax:

    def POST(self):

        '''this func is used to check login user wheather available'''
        input=web.input()
        check_user=input.username
        #print check_user
        if check_user:
            rst=model.find_user(check_user)
            if rst:
                return 'OK'
            else:
                return '<font color="#cc000"><b> '+ check_user + ' </b> invalid user.'

class check_host:

    def POST(self):
        '''this func is used to check login user wheather available'''
        input=web.input()
        check_host=input.hostname
        if check_host:
            rst=model.find_host(check_host)
            if rst:
                return '<font color="#cc000"><b> '+ check_host + ' </b> already exist.'
            else:
                return 'OK'
