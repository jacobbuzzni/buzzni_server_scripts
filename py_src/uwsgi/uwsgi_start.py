#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" uWSGI Start script.
    uWSGI를 실행시킨다.
"""

from scripts_utils import make_optparser
from scripts_utils import read_file
from scripts_utils import ini_parser
from scripts_utils import check_path
from scripts_utils import cmd
from scripts_utils import read_json, write_json
from scripts_utils import root_check
import datetime

def main(options):
    print "[+] starting uwsgi server"
    name = options.name
    ini = options.ini

    if not(name and ini):
        print options
        raise Exception, "Check parameters"

    ini_lines = read_file(ini, "line_list", "r")
    ini_info = ini_parser(ini_lines)["buzzni"]

    pid_path = ini_info["pid_path"]
    socket_path = ini_info["socket_path"]
    dict_path = ini_info["dict_path"]

    check_path([pid_path, socket_path, dict_path])

    dict_obj = read_json(dict_path+"/dictionary.info")
    if dict_obj.has_key(name):
        print "\t[!] already exist name!"
    else:
        sock = socket_path+"/"+name
        pid = pid_path+"/"+name+"_pid.pid"

        cmd_string = "uwsgi --pidfile=%s --socket=%s --ini=%s" % (pid, sock, ini)

        print cmd_string
        status, msg = cmd(cmd_string)
        print status, msg

        dict_obj[name] = {
            "date":str(datetime.datetime.now()),
            "sock":sock,
            "pid":pid,
            "ini":ini
        }
        write_json(dict_path+"/dictionary.info", dict_obj)

    print "[+] finish!"

if __name__ == "__main__":
    root_check()
    desc = "%prog [options]\n\nInfo : uWSGI start"
    options = [
        {
            "name":"name",
            "default":"",
            "description":"set name",
            "require":True
        },
        {
            "name":"ini",
            "default":"",
            "description":"set ini configure file path"
        }
    ]
    options, args = make_optparser(desc, options)
    main(options)