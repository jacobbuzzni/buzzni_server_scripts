#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" uWSGI Start script.
    현재 띄워진 uWSGI 데몬 정보를 출력한다.
"""

from scripts_utils import make_optparser
from scripts_utils import read_file
from scripts_utils import ini_parser
from scripts_utils import read_json
from scripts_utils import root_check

_BUZZNI_CONF_PATH = "/etc/buzzni/uwsgi/"

def main(options):
    ini = options.ini
    ini = _BUZZNI_CONF_PATH + ini + ".ini"

    if not(ini):
        print options
        raise Exception, "Check parameters"

    dict_path = ini_parser(read_file(ini, "line_list", "r"))["buzzni"]["dict_path"]

    info_dict = read_json(dict_path+"/dictionary.info")
    if not(info_dict):
        print "[!] not exsit dictionary info.(%s)" % dict_path
        exit(0)

    for name, info in info_dict.iteritems():
        print "-"*50
        print "%s" % (name)
        print "-"*50
        for k, v in info.iteritems():
            print "%s : %s" % (k, v)
        print "-"*50
        print ""


if __name__ == "__main__":
    root_check()
    desc = "%prog [options]\n\nInfo : uWSGI get info"
    options = [
        {
            "name":"ini",
            "default":"",
            "description":"set ini configure file path"
        }
    ]
    options, args = make_optparser(desc, options)
    main(options)