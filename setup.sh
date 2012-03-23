#!/bin/bash

if [ `id -u` != "0" ];
then
    echo "[!] This script must be run as root"
    exit
fi

buzzni_path="/usr/share/buzzni"

install_uwsgi(){
    echo "[+] start install uwsgi scripts.."

    mkdir $buzzni_path
    cp -R ./py_src/uwsgi $buzzni_path

    # /usr/share/buzzni/uwsgi에 스크립트 추가
    chmod 755 $buzzni_path/uwsgi/uwsgi_start.py
    chmod 755 $buzzni_path/uwsgi/uwsgi_stop.py
    chmod 755 $buzzni_path/uwsgi/uwsgi_show.py
    chmod 755 $buzzni_path/uwsgi/uwsgi_reload.py
    cp ./py_src/sample/uwsgi/buwsgi.sh $buzzni_path/uwsgi/buwsgi
    chmod 755 $buzzni_path/uwsgi/buwsgi

    ln -s $buzzni_path/uwsgi/uwsgi_start.py /usr/sbin/uwsgi_start
    ln -s $buzzni_path/uwsgi/uwsgi_stop.py /usr/sbin/uwsgi_stop
    ln -s $buzzni_path/uwsgi/uwsgi_show.py /usr/sbin/uwsgi_show
    ln -s $buzzni_path/uwsgi/uwsgi_reload.py /usr/sbin/uwsgi_reload
    ln -s $buzzni_path/uwsgi/buwsgi /usr/sbin/buwsgi

    mkdir -p /etc/buzzni/uwsgi/
    cp ./py_src/sample/uwsgi/uwsgi.ini /etc/buzzni/uwsgi/

    echo "[+] success."
    echo "[!!] add scripts at /usr/share/buzzni/uwsgi/buwsgi"
}

remove(){
    rm -rf $buzzni_path
    rm -rf /etc/buzzni
    rm -rf /tmp/buzzni

    rm /usr/sbin/uwsgi_*
}
case "$1" in
    uwsgi)
        install_uwsgi
        ;;
    remove)
        remove
        ;;
    *)
        echo "usage : setup.sh {uwsgi|remove}"
        ;;
esac