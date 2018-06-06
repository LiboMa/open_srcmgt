### This system is used to manage IT information ###

Update History:

    2014-6.2:  ambiguous and exact search engine supported. by mode 1 and 2
    2013-7-03: add new function for supporting host view, change main program index.py to hosts.py.
               Version updated, 1.2
    2013-6-14: opsapi supported. opsapi?getrst=all, all_storage, Version 1.1
    2013-5-8 : basic session and autentication supported with mysql.
    2013-5-6 : basic search engine supported.

Packages depencency:

    This program used the web framewrok web.py and which dependency packages are:

    * MySQLdb
    * web.py
    * swpan-fcgi
    * nginx or apache
    * flup
    * libapache2-mod-wsig


Installation:
    
    #>git clone https://github.com/LiboMa/sourcemgt

Update:

    #> git add files..
    #> git commit -m "comment"
    #> git remote add second https://github.com/LiboMa/$(dirname .) #when creating new repository.
    #> git push

####### Ubuntu Linux installation

apt-get install apache2 libapache2-mod-wsgi 
apt-get install python-pip python-mysqldb

sudo -E pip install web.py


