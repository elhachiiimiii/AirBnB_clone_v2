#!/usr/bin/python3
# should delete archives data
import os
from fabric.api import *

env.hosts = ["54.172.84.154", "54.236.230.59"]


def do_clean(number=0):
    """should clean the archives date

    Args:
        number: intager
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
