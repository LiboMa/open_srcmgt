#!/bin/sh 

# This script is ussed start the spawn-fcgi for python project.
# written by Libo @ 2014.5.15

home='/opt/test/sourcemgt'
index=$home/itinfo_nginx.py
FCGI=`which spawn-fcgi`

start() {

    spawn-fcgi -d $home -f $index -a 127.0.0.1 -p 9002
}

stop() {

    kill `pgrep -f "python $index"`

}

case $1 in 

    start)
        start
        ;;
    stop)
        stop
        ;;
    reload|restart|reboot)
        stop
        sleep 1
        start
        ;;
    *)
        echo "Usage `basename $0` start|stop|[reboot|restart]"
        ;;
esac
