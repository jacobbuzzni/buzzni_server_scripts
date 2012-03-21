# -*- coding : utf-8 -*-

import os
from optparse import OptionParser

def read_file(path, read_type="line_list", option="r"):
    """ read_type : all_string, line_list
    """
    fp = open(path, option)
    if read_type == "all_string":
        return fp.read()
    elif read_type == "line_list":
        return fp.readlines()

def make_optparser(description, options):
    parser = OptionParser(usage=description.decode("utf-8"))
    for option in options:
        name = "--"+option["name"]
        default = option["default"]
        desc = option["description"]
        parser.add_option(name, default=default, help=desc)
    (result, args) = parser.parse_args()

    return result, args

def ini_parser(ini_lines):
    info_dict = {}
    obj_name = ""
    for line in ini_lines:
        line = line.replace("\n", "").replace(" ","")
        if line[0] == "#": # ignore lines
            continue

        if line[0] == "[":
            obj_name = line.replace("[","").replace("]","")
            if not info_dict.has_key(obj_name):
                info_dict[obj_name] = {}
            continue

        info = line.split("=")
        if info[1].lower() == "true":
            info[1] = True
        elif info[1].lower() == "false":
            info[1] = False
        elif info[1].lower() == "on":
            info[1] = True
        elif info[1].lower() == "off":
            info[1] = False

        info_dict[obj_name][info[0]] = info[1]

    return info_dict

def check_path(path_list):
    for path in path_list:
        if not os.path.isdir(path):
            os.makedirs(path)














