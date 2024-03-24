#!/usr/bin/python3
""" deploy_web_static module """
from fabric.api import *
from os.path import getsize
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['100.26.215.136', '100.26.20.75']


path = do_pack()


def deploy():
    """jsut calling pack and deploy"""
    if path is None:
        return False
    print("web_static packed: {} -> {}Bytes"
          .format(path, getsize(path)))
    return do_deploy(path)
