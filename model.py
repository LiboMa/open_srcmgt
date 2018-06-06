import web
import datetime
from config.settings import db

#db=web.database(dbn='sqlite',db='itvw.db')

tb='vserver_info'

def get_entries(type='vhost'):
    return db.select(tb, where='type=$type', order='hostname ASC',vars=locals())

# This model is used for entry sorting.
def get_entries_orderby_dc(type='vhost',item='datacenter',order='ASC'):
    return db.select(tb, where='type=$type', order=item+' '+order,vars=locals())

def get_allentries(tb='vserver_info'):
    return db.select(tb, order='hostname ASC',vars=locals())

def get_hosts():
    return db.select(tb, where="type='host'", order='hostname ASC')

def get_hosts_orderby_db(order='ASC'):
    return db.select(tb, where="type='host'", order='datacenter '+ order)

def get_entry(id,tb='vserver_info'):
    try:
        return db.select(tb, where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def get_id_byname(name):

    try:
        return db.select(tb,what="id",where="hostname=$name", vars=locals())[0]
    except IndexError:
        return None

def new_host(hostname, eth0, eth1, eth2, gateway,os, project, owners, dmz, datacenter,hosted, eth0_vlan, eth1_vlan, status):

    try:
        print "info:host,eth0,eth1,eth2,gateway,os,project,owners,dmz,datacenter,hosted,eth0_vlan,eth1_vlan,status", hostname,eth0,eth1,eth2,gateway,os,project,owners,dmz,datacenter,hosted,eth0_vlan,eth1_vlan,status
        db.insert(tb,
        hostname=hostname,
        eth0=eth0,
        eth1=eth1,
        eth2=eth2,
        hosted=hosted,
        gateway=gateway,
        os=os,
        project=project,
        owners=owners,
        dmz=dmz,
        datacenter=datacenter,
        updated_on=datetime.datetime.now(),
        eth0_vlan=eth0_vlan,
        eth1_vlan=eth1_vlan,
        status=status,
        type='vhost'
        )
    except Exception,e:
        raise
        return e

def up_entry(id,eth0, eth1,eth2,gateway,os, project, owners,dmz, datacenter, hosted, eth0_vlan, eth1_vlan, status, type=None):
    db.update(tb,where='id=$id',vars=locals(),
           eth0=eth0,
           eth1=eth1,
           eth2=eth2,
           hosted=hosted,
           gateway=gateway,
           os=os,
           project=project,
           dmz=dmz,
           datacenter=datacenter,
           updated_on=datetime.datetime.now(),
           eth0_vlan=eth0_vlan,
           eth1_vlan=eth1_vlan,
           status=status,
           owners=owners
            )

def del_entry(id):
    db.delete(tb,where='id=$id', vars=locals())

def find_host(hostname):
    return get_id_byname(hostname)

####### User admin #####
def new_user(username,passwd,alias=''):
    return db.insert('users',username=username,password=passwd,alias=alias, status=0,created_on=datetime.datetime.now())
    #0=logon
    #1=logout
    #2=disabled

def find_user(username):
    try:
        return db.select('users',what="*", where="username=$username",vars=locals())[0]
    except IndexError:
        return None

def up_passwd(username,password):

    db.update('users',where="username=$username",password=password,vars=locals())

def del_user(username):
    try:
        return db.delete('users',where="username=$username",vars=locals())
    except IndexError:
        return None

def get_status_by_name(username):
    try:
        return db.select('users',what='status',where="username=$username",vars=locals())[0]
    except IndexError:
        return None

def set_status_by_user(username,status):
    try:
        db.update('users', status=status, where="username=$username",vars=locals())
    except IndexError:
        return None

###### Utilities #######

####### asset ###########

def get_assets(tb='asset'):

    return db.select(tb, order="logic_name ASC", vars=locals())

def get_asset(id, tb='asset'):

    return db.select(tb, where='id=$id', vars=locals())

def get_asset_by_name(name, tb='asset'):
    return db.select(tb, where='logic_name=$logic_name', vars=locals())

def new_asset(logic_name, device_type, serial_number, hardware_info="NULL",layout="NULL",status="NULL",history="NULL",updated_on=datetime.datetime.now(), comment="NULL", tb='asset'):

    try:
        db.insert(tb,
            logic_name=logic_name,
            device_type=device_type,
            serial_number=serial_number,
            hardware_info=hardware_info,
            layout=layout,
            status=status,
            history=history,
            updated_on=updated_on,
            comment_1=comment
            )
    except Exception, e:
        return e

    #db.insert(tb, )

def up_asset(id, logic_name, device_type, serial_number, hardware_info, layout, status, history, updated_on=datetime.datetime.now(), tb='asset',):

    db.update(tb,where='id=$id',vars=locals(),
           logic_name=logic_name,
           device_type=device_type,
           serial_number=serial_number,
           hardware_info=hardware_info,
           layout=layout,
           status=status,
           history=history,
           updated_on=updated_on
            )
    #try:
    #    db.update(tb, where='id=$id')
def del_asset(id, tb='asset'):
    try:
        return db.delete(tb, where='id=$id', vars=locals())
    except IndexError:
        return None


#############################################################################
# Capacity tag Management;
#from config.settings import db
#db=web.database(dbn='sqlite',db='itvw.db')
tb_ctmgt='capacity_tags'

####### tags ###########

def get_tags(tb=tb_ctmgt):
    return db.select(tb, order="tagname ASC", vars=locals())

def get_maxtag(tb=tb_ctmgt):
    return db.select(tb, what="*",where="tagname=(select max(tagname) from capacity_tags)", vars=locals())

def get_tags_by_id(id, tb=tb_ctmgt):

    return db.select(tb, where='id=$id', vars=locals())

def get_tags_by_name(name, tb=tb_ctmgt):

    return db.select(tb, where='tagname=$name', vars=locals())

def new_tags(tagname, assignedby, status='NULL', comment='NULL',tb=tb_ctmgt):
#def new_tags(tagname, assignedby, status='NULL', comment='NULL',tb=tb_ctmgt):

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

def up_tags(id, tagname, assignedby, status, comment='NULL',update_on=datetime.datetime.now(), tb=tb_ctmgt):

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

def del_tags(id, tb=tb_ctmgt):
    try:
        return db.delete(tb, where='id=$id', vars=locals())
    except IndexError:
        return None

