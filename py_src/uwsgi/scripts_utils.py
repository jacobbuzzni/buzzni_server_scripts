# -*- coding : utf-8 -*-

import os, json
from optparse import OptionParser
import commands

def read_file(path, read_type="line_list", option="r"):
    """ read_type : all_string, line_list
    """
    if os.path.isfile(path):
        fp = open(path, option)
    else:
        raise Exception, "no search file.("+path+")"
    if read_type == "all_string":
        return fp.read()
    elif read_type == "line_list":
        return fp.readlines()

def open_file(path, option="r+"):
    if not os.path.isfile(path):
        open(path, "w").close()
    return open(path, option)

def rm_file(path):
    return os.remove(path)

def read_json(path):
    fp = open_file(path, "r+")
    read_result = fp.read()
    dict_obj = {}
    if read_result:
        dict_obj = json.loads(read_result)
    fp.close()
    return dict_obj

def write_json(path, obj):
    json_string = json.dumps(obj)
    fp = open_file(path, "w+")
    fp.write(json_string+"\n")
    fp.close()

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
        if line[0] == "#" or len(line) < 3: # ignore lines
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

def cmd(cmd_string):
    return commands.getstatusoutput(cmd_string)

def is_root():
    return not(os.getuid())

def root_check():
    if not is_root():
        print "[!] r u root?"
        exit(0)


