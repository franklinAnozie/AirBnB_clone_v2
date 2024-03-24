#!/usr/bin/python3
""" pack_web_static module """
from fabric.api import *
from os.path import isdir
from datetime import datetime


def do_pack():
    """crates a tar file of content of web_static"""
    n = datetime.now()
    stamp = "{}{}{}{}{}{}".format(n.year, n.month, n.day,
                                  n.hour, n.minute, n.second)

    try:
        if not isdir("versions"):
            local("mkdir versions")
        path = "versions/web_static_{}.tgz".format(stamp)

        code = local("tar -cvzf {} web_static".format(path)).succeeded

        if code:
            return (path)
        else:
            return None
    except:
        return None
