#!/usr/bin/env python3

import os
from os import path
import shutil


def main():
    print("shell_start")
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dst = src + ".bak"
        shutil.copy(src, dst)




if __name__ == "__main__":
    main()
