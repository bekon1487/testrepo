import hashlib
import json
import os
from pathlib import Path

def read_file(path):
    try:
        with open(file=path, mode='r', encoding='utf-8', errors="ignore") as f:
            return f.read()
    except:
        return ""

def list_files_pathlib(path):
    list = []
    try:
        for entry in path.iterdir():
            if entry.is_file():
                list.append(entry)
            elif entry.is_dir():
                for file in list_files_pathlib(entry):
                    list.append(file)
    except:
        pass

    return list

def dump(directory, write: bool = False):
    dump_file = {}
    for file in list_files_pathlib(Path(directory)):
        if os.path.exists(file):
            size = os.path.getsize(file)
            file_c = read_file(file)
            # print("\"", file_c, "\"")
            sha256_c = hashlib.sha256(file_c.encode()).hexdigest()
            dump_file[os.path.abspath(file)] = {
                'size': size,
                'sha256': sha256_c,
            }
    if write:
        with open(file='dump.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dump_file, indent=4))

            # print(dump_file)
    return dump_file

def loadDump() -> dict:
    with open('dump.json', 'r') as f:
        dump = json.loads(f.read())
        return dump