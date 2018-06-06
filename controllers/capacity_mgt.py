#!/usr/bin/env python
from config.settings import *
from controllers.hosts import isactived
import model
session = web.config.session

class Index:

    def GET(self):
        # show tags
        data = model.get_tags()
        return render_ori.show_capacitytag(data,"INPUT TAG NUMBERS YOU NEED?",isactived())
    def POST(self):
        pass

class New:

    def GET(self):
        data = model.get_tags()
        return render.show_capacitytag(data, "INPUT TAG NUMBERS YOU NEED?",isactived())
    def POST(self):
        data = web.input()
        if isactived() and (session.user_id == 'dkx4oih' or session.user_role == 'manager'):
            try:
                numbers_of_tags = int(data.tag_numbers)
                comment = data.comment
                #print numbers_of_tags
                assignedby = session.user_alias
                #print assignedby
                status = 'used'
            except Exception:
                raise web.seeother("./capacity")
        else:
            raise web.seeother("./capacity")

        # check generate the tags
        maxtag = model.get_maxtag()
        if maxtag:
            for i in maxtag:
                tag_type = i.tagname[:2]
                tag_number = int(i.tagname[2:])
                start_number = tag_number + 1
                end_number = start_number + numbers_of_tags
        else:
            tag_type = 'CM'
            start_number = 1
            end_number = start_number + numbers_of_tags

        for n in range(start_number, end_number):
            tagname = tag_type.upper() +'{:004}'.format(n)
            print tagname
            model.new_tags(tagname, assignedby, status, comment)
        return web.seeother("./capacity")



class Update:

    def GET(self):
        pass
    def POST(self):
        pass

class Delete:

    def GET(self):
        pass
    def POST(self,id):
        if isactived() and (session.user_id == 'dkx4oih' or session.user_role == 'manager'):
            model.del_tags(id)
        return web.seeother("/capacity")

