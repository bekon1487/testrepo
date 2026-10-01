import time

from Utils.GlobalVars import config


# config = {}
#
# with open("config.json", "r") as f:
#     config = json.load(f)

def dict_to_list_keys(dict_c):
    return list(dict_c.keys())

def dict_to_list_values(dict_c):
    return list(dict_c.values())

def lists_difference(lists_1, lists_2):
    dif = []
    for file in lists_1:
        file = str(file)
        if file not in lists_2:
            dif.append(file)
        else:
            lists_2.remove(file)

    return dif

def log(*content, debug: bool = False):
    time_obj = time.time()
    local_time = time.localtime(time.time())
    if config['debug']:
        print(time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time())), *content)
    else:
        if not debug:
            print(time.strftime("%d/%m/%y %H:%M:%S", local_time), *content)
