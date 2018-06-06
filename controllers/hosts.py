import web
import model
import forms

from config.settings import *

# import session infomation from global settings.
session = web.config.session

def isactived():
    if session.login == 'yes':
        return True
    else:
        return False
def isactived_resource():
    if session.login == 'yes' and session.user_role == 'admin':
        return True
    else:
        return False

class Index:

    def GET(self):
        entries=model.get_entries()
        status=isactived_resource()
        return render.index(entries,status)

class sorted:

    def GET(self):
        if web.input().has_key('order') and web.input().has_key('item'):
            order=web.input().order
            item=web.input().item
	    if order == 'reverse':
                entries=model.get_entries_orderby_dc(type='vhost',item=item, order='DESC')
            else:
                entries=model.get_entries_orderby_dc(type='vhost',item=item, order='ASC')
        else:
            entries=model.get_entries_orderby_dc(type='vhost',item=item, order='ASC')

        if isactived_resource():
            status=True
        else:
            status=False

        return render.index(entries,status)

class ori_Index:

    def GET(self):
        '''show info'''
        entries=model.get_entries()
        if isactived_resource():
            status=True
        else:
            status=False
        entries=model.get_entries()
        return render_ori.index(entries,status)

class New:

    def GET(self):
        ''' add host info '''
        #type=web.input().type
        form=forms.newhost()
        return render_ori.new(form)

    def POST(self):
        if isactived_resource():
            '''Receive data '''
            '''Set default data for updating'''
            tData=web.input(eth2='NULL', eth0_vlan='NULL', eth1_vlan='NULL', hosted='NULL',gateway="NULL",owners="NULL")

            if not (tData.hostname or tData.eth0 or tData.hosted or tData.datacenter):
                raise web.seeother("./")
            try:
                model.new_host(
                        #data.id,
                        tData.hostname,
                        tData.eth0,
                        tData.eth1,
                        tData.eth2,
                        tData.gateway,
                        tData.os,
                        tData.project,
                        tData.owners,
                        tData.dmz,
                        tData.datacenter,
                        tData.hosted,
                        tData.eth0_vlan,
                        tData.eth1_vlan,
                        tData.status,
                        )
            except Exception:
                raise
        else:
            raise web.seeother("/login")


class Save:

    form = forms.editform()

    def GET(self, id=None):
        '''return form by user ID to edit. #render_ori.save_entry(id,form'''
        entry = model.get_entry(int(id))
        try:
            _type = entry.type
        except Exception,e:
            print "DB ERROR,%s", e
            return None
        self.form = forms.editform(type=_type)
        self.form.fill(entry)
        return render_ori.save_entry(id,self.form)

    def POST(self,id):

        if isactived_resource():
            '''Receive data '''
            '''Set default data for updating'''
            data=web.input(eth2='NULL', eth0_vlan='NULL', eth1_vlan='NULL', hosted='NULL',gateway="NULL")
            try:
                model.up_entry(data.id,
                        data.eth0,
                        data.eth1,
                        data.eth2,
                        data.gateway,
                        data.os,
                        data.project,
                        data.owners,
                        data.dmz,
                        data.datacenter,
                        data.hosted,
                        data.eth0_vlan,
                        data.eth1_vlan,
                        data.status,
                        )
            except Exception,e:
                print "Error With:",e
        else:
            raise web.seeother("/login")

class Delete:

    def POST(self, id):
        if isactived_resource():
            model.del_entry(int(id))
            raise web.seeother('/')
        else:
            return False

class Test:

    def GET(self):
#        import base64
#        data=web.input()
#        id=data.id
#        type=data.type
#        if type == 'host':
#            s=str(id)+type
#        else:
#            s=str(id)
#        s="Teststrings_datetime"+str(id)+type
#        en64_s=base64.encodestring(s)
#        web.setcookie('testb64',en64_s,3600)
#        b64=web.cookies().get('testb64')
        return render.test(web.input())
        #return render.test("1")

    def POST(self):

        data = web.input()
        return render.test(data)


