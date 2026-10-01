import fnmatch
import os
import time
from threading import Thread
from zipfile import ZipFile

from Component.FileManager import loadDump, dump
from Utils.GlobalVars import logger, config
from Utils.sad import dict_to_list_keys, lists_difference


def scanner(directory, rate: int = 10) -> dict:
    Thread(target=target, args=(directory,rate,)).start()

def target(directory, rate: int) -> None:
    while True:
        time.sleep(rate)
        dump_c = loadDump()
        dump_n = dump(directory)
        dump_n_l = dict_to_list_keys(dump_n)
        dump_c_l = dict_to_list_keys(dump_c)
        deleted = lists_difference(dump_c_l, dump_n_l)
        created = lists_difference(dump_n_l, dump_c_l)


        edited = []

        for key, value in dump_c.items():
            if key in dump_n:
                if value['sha256'] != dump_n[key]['sha256']:
                    edited.append(key)

        types = ['critical', 'warn', 'info']
        actions = ['Edited', 'Created', 'Deleted']
        sorted_d = sort(created, edited, deleted)
        time_mask = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))

        for type in types:
            for action_type in actions:
                for msg in sorted_d[type][action_type.lower()]:
                    logger.log(time_mask, type.lower(), action_type + " " + msg)

        if len(created) > 0:
            isolation(created)

        if not (len(edited) == len(created) == len(deleted) == 0):
            dump(directory, True)
        else:
            pass

def isolation(created):

    for file in created:
        for mask in config['isolation']:
            if fnmatch.fnmatch(file, mask):
                with ZipFile(os.path.abspath(file) + ".zip", "w") as myzip:
                    myzip.write(file)
                logger.info(file + " Помещён в архив")
                os.remove(os.path.abspath(file))

def sort(created, edited, deleted):
    sorted = {
        "critical": {
            "created": [],
            "edited": [],
            "deleted": [],
        },
        "info": {
            "created": [],
            "edited": [],
            "deleted": [],
        },
        "warn": {
            "created": [],
            "edited": [],
            "deleted": [],
        }
    }

    for file in created:
        sorted[what_type(file)]["created"].append(file)

    for file in edited:
        sorted[what_type(file)]["edited"].append(file)

    for file in deleted:
        sorted[what_type(file)]["deleted"].append(file)

    return sorted

def what_type(file_path):
    # print(file_path)
    for mask in config['logging']['critical']:
        if fnmatch.fnmatch(file_path, mask):
            return "critical"

    for mask in config['logging']['warn']:
        if fnmatch.fnmatch(file_path, mask):
            return "warn"

    return 'info'