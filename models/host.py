import web
from config.settings import db

tb='host_info'

def get_hosts():
    return db.select(tb, order='hostname ASC')
