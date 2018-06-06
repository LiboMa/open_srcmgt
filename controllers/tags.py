#!/usr/bin/env python
from config.settings import *
from controllers.hosts import isactived
import cabling_model
session = web.config.session

class Index:

    def GET(self):
        # show tags
        data = cabling_model.get_tags()
        return render_ori.show_tag(data,"INPUT TAG NUMBERS YOU NEED?",isactived())
    def POST(self):
        pass

class New:

    def GET(self):
        data = cabling_model.get_tags()
        return render.show_tag(data, "INPUT TAG NUMBERS YOU NEED?",isactived())
    def POST(self):
        data = web.input()
        if isactived() and (session.user_role == 'admin' or session.user_role == 'manager'):
            try:
                numbers_of_tags = int(data.tag_numbers)
                comment = data.comment
                #print numbers_of_tags
                assignedby = session.user_alias
                #print assignedby
                status = 'used'
            except Exception:
                raise web.seeother("./tags")
        else:
            raise web.seeother("./tags")

        # Check generate the tags
        maxtag = cabling_model.get_maxtag()
        if maxtag:
            for i in maxtag:
                tag_type = i.tagname[0]
                tag_number = int(i.tagname[1:])
                start_number = tag_number + 1
                end_number = start_number + numbers_of_tags
        else:
            # First record creation
            tag_type = 'C'
            start_number = 1
            end_number = start_number + numbers_of_tags

        for n in range(start_number, end_number):
            tagname = tag_type.upper() +'{:004}'.format(n)
            print tagname
            cabling_model.new_tags(tagname, assignedby, status, comment)
        return web.seeother("./tags")


class Update:

    def GET(self):
        pass
    def POST(self):
        pass

class Delete:

    def GET(self):
        pass
    def POST(self,id):
        if isactived() and (session.user_id == 'dkx4oih' or session.user_id == 'dkx4gmf'):
            cabling_model.del_tags(id)
        return web.seeother("/tags")

