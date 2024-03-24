#!/usr/bin/python3
""" clean_web_static module"""
from fabric.api import *
from os import listdir
env.hosts = ['100.26.215.136', '100.26.20.75']


def do_clean(number=0):
    """delete all except number of files starting from oldest

    Args:
        number: number of files to not delete
    """
    number = 1 if int(number) == 0 else int(number)

    flist = sorted(listdir("versions"))
    for b in range(number):
        flist.pop()
    for a in flist:
        local("rm ./versions/{}".format(a))

    with cd("/data/web_static/releases"):
        tlist = run("ls -tr").split()
        flist = []
        for a in tlist:
            if "test" != a:
                flist.append(a)
        for i in range(number):
            flist.pop()
        for a in flist:
            run("rm -rf ./{}".format(a))
