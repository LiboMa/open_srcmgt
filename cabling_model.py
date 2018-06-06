import web
import datetime
#from config.settings import db
#db=web.database(dbn='sqlite',db='itvw.db')
db=web.database(dbn='mysql',db='cabling_mgt',user='itadmin',passwd='Desert_eagle')
tb='cabling_tag'
tb_ci='cabling_info'

####### tags ###########

def get_tags(tb='cabling_tag'):
    return db.select(tb, order="tagname ASC", vars=locals())

def get_maxtag(tb='cabling_tag'):
    return db.select(tb, what="*",where="tagname=(select max(tagname) from cabling_tag)", vars=locals())

def get_tags_by_id(id, tb='cabling_tags'):

    return db.select(tb, where='id=$id', vars=locals())

def get_tags_by_name(name, tb='cabling_tag'):

    return db.select(tb, where='tagname=$name', vars=locals())

def new_tags(tagname, assignedby, status='NULL', comment='NULL',tb='cabling_tag'):
#def new_tags(tagname, assignedby, status='NULL', comment='NULL',tb='cabling_tag'):

    try:
        db.insert(tb,
            tagname = tagname,
            assignedby = assignedby,
            status = status,
            comment = comment,
            update_on = datetime.datetime.now(),
            )
    except Exception, e:
        return e

    #db.insert(tb, )

def up_tags(id, tagname, assignedby, status, comment='NULL',update_on=datetime.datetime.now(), tb='cabling_tag'):

    try:
        db.insert(tb, where='id=$id', vars=locals(),
            tagname = tagname,
            assignedby = assignedby,
            status = status,
            comment = comment,
            update_on=update_on,
            )
    except Exception, e:
        return e

def del_tags(id, tb='cabling_tag'):
    try:
        return db.delete(tb, where='id=$id', vars=locals())
    except IndexError:
        return None

############### cabling management ###############

def new_cable(data):

    if isinstance(data,type(dict())):
        try:
            db.insert(tb_ci,
                    rack=data['rack'],
                    device_name=data['device_name'],
                    he=data['he'],
                    card=data['card'],
                    slot=data['slot'],
                    port=data['port'],
                    device_type=data['device_type'],
                    cable_id=data['cable_id'],
                    vlan_id=data['vlan_id'],
                    func=data['func'],
                    updated_on = datetime.datetime.now(),
                    created_on = datetime.datetime.now()
                    )
        except Exception, e:
            print e
    else:
        print "Error: in proper data type"
        return None
