#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" uWSGI Start script.
    현재 띄워진 uWSGI 를 중지 시킨다.
"""

from scripts_utils import make_optparser
from scripts_utils import read_file, rm_file
from scripts_utils import ini_parser
from scripts_utils import read_json, write_json
from scripts_utils import root_check
from scripts_utils import cmd

_BUZZNI_CONF_PATH = "/etc/buzzni/uwsgi/"

def main(options):
    name = options.name
    ini = options.ini
    ini = _BUZZNI_CONF_PATH + ini + ".ini"

    if not(ini and name):
        print options
        raise Exception, "Check parameters"

    dict_path = ini_parser(read_file(ini, "line_list", "r"))["buzzni"]["dict_path"]

    info_dict = read_json(dict_path+"/dictionary.info")
    if name == "*":
        tmp = info_dict.keys()
        name = ""
        for _name in tmp:
            name += _name+","
        name = name[0:-1]

    name_list = name.split(",")
    for name in name_list:
        pid = info_dict[name]["pid"]
        sock = info_dict[name]["sock"]
        cmd_string = "uwsgi --stop %s" % (pid)
        status, msg = cmd(cmd_string)
        info_dict.pop(name)

        rm_file(pid)
        rm_file(sock)

    write_json(dict_path+"/dictionary.info", info_dict)

if __name__ == "__main__":
    root_check()
    desc = "%prog [options]\n\nInfo : uWSGI Stop."
    options = [
        {
            "name":"name",
            "default":"",
            "description":"uwsgi daemon name"
        },
        {
            "name":"ini",
            "default":"",
            "description":"set ini configure file name"
        }
    ]
    options, args = make_optparser(desc, options)
    main(options)
