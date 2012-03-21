#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" uWSGI Start script.
    이 스크립트로 django + uWSGI를 실행시킨다.
"""

from scripts_utils import make_optparser
from scripts_utils import read_file
from scripts_utils import ini_parser
from scripts_utils import check_path

def main(options):
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


if __name__ == "__main__":
    desc = "%prog [options]\n\nInfo : uWSGI Start Script."
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