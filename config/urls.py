# Full model supported by Java Script

prefix='controllers.'
backend='controllers.admin.'

urls = (

    # vhost management
        '/', prefix+ 'hosts.Index',
        '/test_index', prefix+ 'hosts.TestIndex',
        '/ori_show', prefix + 'hosts.ori_Index',
#        '/detail', prefix + 'hosts.Full_model',
        '/sortedv', prefix + 'hosts.sorted',
        '/new', prefix + 'hosts.New',
        '/delete/(\d+)', prefix + 'hosts.Delete',
        '/test', prefix + 'hosts.Test',
#        '/edit_entry/?(\d*)', prefix + 'index.Edit_Entry',
        '/save/(\d*)', prefix + 'hosts.Save',
        '/search', prefix +  'search.Search',
    # user management Settings
        '/login',  backend +  'user.Login',
        '/logout', backend +  'user.Logout',
        '/password', backend + 'user.Password',
    # utilities

        '/gen_password', prefix + 'utilities.GEN_Password',
        '/opsapi', prefix + 'utilities.opsapi',
        '/check_ajax', prefix + 'utilities.check_ajax',
        '/check_host', prefix + 'utilities.check_host',
        '/hostinfo', prefix + 'host_info.Index',
        '/send_msg', prefix + 'utilities.Send_msg',
    ## asset management settings
        '/asset', prefix + 'asset.asset_info',
        '/addasset', prefix + 'asset.new_asset',
        '/delasset/(\d+)', prefix + 'asset.del_asset',
        '/upasset/(\d+)', prefix + 'asset.up_asset',
    ## wiki system
        '/wiki', prefix + 'wiki.Wiki',
    ## Tag management
        '/tags', prefix + 'tags.New',
        '/ori_show_tag', prefix + 'tags.Index',
        '/delete_tag/(\d+)', prefix + 'tags.Delete',
    ## Capacity Tag management
        '/capacity', prefix + 'capacity_mgt.New',
        '/ori_show_capacitytag', prefix + 'capacity_mgt.Index',
        '/delete_capacitytag/(\d+)', prefix + 'capacity_mgt.Delete',

        )
