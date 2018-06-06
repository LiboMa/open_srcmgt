#!/usr/bin/env python

import model
from config.settings import *

#-*-utf-8-*-

session = web.config.session

def isactived():

    if session.login == 'yes' and session.user_id != 'dkx4gmf':
        return True
    else:
        return False


class asset_info:

    def GET(self):
        data=web.input(tpl='yes')
        if data.tpl == 'yes':
            RENDER=render
        else:
            RENDER=render_ori

        entries=model.get_assets()
        return RENDER.show_asset(entries,status=isactived())

class new_asset:

    def GET(self):
        if isactived():
            return render.new_asset()
        else:
            return web.seeother("./")

    def POST(self):

        if session.login == 'yes':
            data=web.input()
            try:
                model.new_asset(
                        data.logic_name,
                        data.device_type,
                        data.serial_number,
                        data.hardware_info,
                        data.layout,
                        data.status,
                        data.history)
                web.seeother("./asset")
            except Exception, e:
                return e
        else:
            return web.seeother("./asset")

class up_asset:

    def GET(self):
        return render.up_asset()

    def POST(self,id):

        data=web.input()
        try:
            model.up_asset(id, data.logic_name,data.device_type,data.serial_number, data.hardware_info,data.layout,data.status,data.history)
        except Exception, e:
            return e


class del_asset:

    def POST(self, id):
        if session.login == 'yes':
            return model.del_asset(id)
            raise web.seeother('./asset')
        else:
            return None

class search_asset:

    def GET(self):
        pass

    def POST(self):
        pass
