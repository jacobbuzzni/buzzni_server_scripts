#!/bin/bash

if [ `id -u` != "0" ];
then
    echo "[!] This script must be run as root"
    exit
fi

_start(){
    #uwsgi_start --name=[name] --ini=[ini_path];
    service nginx restart;
}

_stop(){
    #uwsgi_stop --name=[name] --ini=[ini_path];

    sleep 2;
    service nginx restart;
}

case "$1" in
    start)
        _start;
        ;;
    stop)
        _stop;
        ;;
    restart)
        _stop;
        _start;
        ;;
    *)
        echo "usage : buwsgi {start|stop|restart|reload}"
        ;;
esac