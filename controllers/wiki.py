#!/usr/bin/env python

import web
import model
from config.settings import *


class Wiki:

    def GET(self):

        return render.wiki()

    def POST(self):
        pass



