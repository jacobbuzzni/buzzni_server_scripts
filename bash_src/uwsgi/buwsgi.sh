#!/bin/bash

start(){
    name=$1
    python /usr/share/buzzni/uwsgi/uwsgi_start.py --name=$name --ini=/etc/buzzni/uwsgi/uwsgi.ini
}

stop(){
    echo "uwsgi stop!"
}

reload(){
    echo "uwsgi reload!"
}

case "$1" in
    start)
        if [ $2 ];
        then
            start $2
        else
            echo "[!] usage : buwsgi start [name]"
        fi
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    reload)
        ;;
    *)
        echo "[!] usage : buwsgi {start|stop|reload}"
        ;;
esac
