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

    echo "alias uwsgi_start=\"python $buzzni_path/uwsgi/uwsgi_start.py\"" >> ~/.bashrc
    echo "alias uwsgi_stop=\"python $buzzni_path/uwsgi/uwsgi_stop.py\"" >> ~/.bashrc
    echo "alias uwsgi_show=\"python $buzzni_path/uwsgi/uwsgi_show.py\"" >> ~/.bashrc
    echo "alias uwsgi_reload=\"python $buzzni_path/uwsgi/uwsgi_reload.py\"" >> ~/.bashrc

    cp ./bash_src/uwsgi/buwsgi.sh /etc/init.d/buwsgi
    chmod 755 /etc/init.d/buwsgi

    mkdir -p /etc/buzzni/uwsgi/
    cp ./py_src/sample/uwsgi.ini /etc/buzzni/uwsgi/

    echo "[+] success."

    bash
}

remove(){
    rm -rf $buzzni_path
    rm -rf /etc/buzzni
    rm -rf /tmp/buzzni

    rm /etc/init.d/buwsgi
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