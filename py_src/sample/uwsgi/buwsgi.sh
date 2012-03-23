#!/bin/bash

if [ `id -u` != "0" ];
then
    echo "[!] This script must be run as root"
    exit
fi

case "$1" in
    start)
        ;;
    stop)
        ;;
    restart)
        ;;
    reload)
        ;;
    *)
        echo "usage : buwsgi {start|stop|restart|reload}"
        ;;
esac