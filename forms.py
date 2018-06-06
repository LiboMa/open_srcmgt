from web import form as f

notnull = f.Validator("must", bool)
vname = f.regexp(r".{3,20}$", 'between 3-20')
vpass = f.regexp(r".{5,20}$", 'between 3-20')
OSLIST = ['RHEL5.8','RHEL5.9','RHEL6.0','RHEL6.1','RHEL6.2','RHEL6.3','RHEL6.4','RHEL5.x','RHEL6.x']
DMZ=["dmz1","dmz2","dmz3","inter"]
STATUS=["pending","online","offline"]
DC=['FSB','NTT','JDC','SGDC']

def newhost(DC=DC,type='vhost'):

    if type == 'vhost':
        eth0_vlan=f.Hidden('eth0_vlan',description='eth0_vlan')
        eth1_vlan=f.Hidden('eth1_vlan',description='eth1_vlan')
        hosted=f.Textbox('hosted',description='dom0')
    elif type == 'host':
        eth0_vlan=f.Textbox('eth0_vlan', description="eth0_vlan",)
        eth1_vlan=f.Textbox('eth1_vlan', description="eth1_vlan",)
        hosted=f.Hidden('hosted',description='Dom0')
    form=f.Form(
            f.Textbox('hostname',f.notnull,
                description="Hostname",),

            f.Textbox('eth0',f.notnull,
                description="eth0",),
            eth0_vlan, # depends on the server type.
            f.Textbox('eth1',f.notnull,
                description="eth1",),
            eth1_vlan, # depends on the server type.
            f.Textbox('eth2', description="eth2",),
            hosted,# depends on tye server type.
            f.Textbox('gateway',f.notnull,
                description="Gateway",),
            f.Textbox('owners',description="Owners",),

            f.Textbox(name='os', value="RHEL5.9", description="Operating System Version",),

            f.Textbox('project',f.notnull,
                description="Project Team",),
            f.Hidden('type',value=type,description='server type'), # select the server type.
            f.Radio('datacenter',value='FSB',args=DC,description='Data Center'),
            f.Dropdown('status',value=STATUS[0],args=STATUS,description='Status'),
            f.Radio('dmz',value=DMZ[1],args=DMZ, description="DMZ"),

            )
    return form


def new_p_host(DC=DC):
    form=f.Form(
            f.Textbox('hostname',f.notnull,
                description="Hostname",),

            f.Textbox('eth0',f.notnull,
                description="Admin IP",),

            f.Textbox('eth0_vlan',description="eth0_vlan",),

            f.Textbox('eth1',f.notnull,
                description="Production IP",),

            f.Textbox('eth1',description="eth1_vlan",),
            f.Textbox('gateway',f.notnull,
                description="Gateway",),
            f.Textbox('os', description="Operating System Version",)
            ,

            f.Textbox('project',f.notnull,
                description="Project Team",),

            f.Radio('datacenter',value='FSB',args=DC,description='Data Center'),

            f.Radio('dmz',value=DMZ[1],args=DMZ, description="DMZ"),

            )
    return form

def editform(DC=DC, type='vhost'):

    if type == 'vhost':
        eth0_vlan=f.Hidden('eth0_vlan', description='eth0_vlan')
        eth1_vlan=f.Hidden('eth1_vlan', description='eth1_vlan')
        hosted=f.Textbox('hosted',description='dom0')
    elif type == 'host':
        eth0_vlan=f.Textbox('eth0_vlan', description="eth0_vlan",)
        eth1_vlan=f.Textbox('eth1_vlan', description="eth1_vlan",)
        hosted=f.Hidden('hosted', description='Dom0')

    form=f.Form(
            f.Hidden('id',f.notnull),

            f.Textbox('hostname',f.notnull,
                description="Hostname",disabled='on'),

            f.Textbox('eth0',f.notnull,
                description="eth0",),
            eth0_vlan,
            f.Textbox('eth1',f.notnull,
                description="eth1",),
            eth1_vlan,
            f.Textbox('eth2',f.notnull,
                description="eth2",),
            hosted,
            f.Textbox('gateway',f.notnull,
                description="Gateway",),
            f.Textbox('os', description="Operating System Version",),

            f.Textbox('project',f.notnull,
                description="Project Team",),

            f.Hidden('type',value=type,description='server type'), # select the server type.
            f.Radio('datacenter',args=DC,description='Data Center'),
            f.Radio('dmz',args=DMZ, description="DMZ"),)
    return form

def login():

    form = f.Form(
            f.Textbox('username',notnull, ),
            f.Password('password',notnull),
            )
    return form

def Password():

    form = f.Form(
            f.Password('old_password',notnull,description="Old Password"),
            f.Password('new_password',vpass,description="New Password"),
            f.Password('check_password',vpass,description="Confirm"),
            validators = [f.Validator(" Passwords not match", lambda i: i.new_password == i.check_password)]
            )
    return form



def createuser():

    form = f.Form(

            f.Input('username',f.notnull,description="Username"),
            f.Password('password',f.notnull,description="Password")

            )
    return form

def testform():

    form=f.Form(

            f.Textbox('hostname',f.notnull,description="Hostname"),
            )
    return None

#### urtils

def generate_password(Password=None):

    form = f.Form(
            f.Textbox('Password',value=Password,description="Password"),
            f.Radio("length",value=12,args=[12,16,18],description="Length"),
            f.Button("Generate", type="submit")
            )
    return form
