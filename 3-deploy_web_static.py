#!/usr/bin/python3
# should create and distribute archive to the server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["54.172.84.154", "54.236.230.59"]


def do_pack():
    """should .tgz archive"""
    dateTime = datetime.utcnow()
    content = "versions/web_static_{}{}{}{}{}{}.tgz".format(dateTime.year,
                                                         dateTime.month,
                                                         dateTime.day,
                                                         dateTime.hour,
                                                         dateTime.minute,
                                                         dateTime.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(content)).failed is True:
        return None
    return content


def do_deploy(archive_path):
    """should distributes archive to the server.

    Args:
        archive_path: string
    Returns: boolean
    """
    if os.path.isfile(archive_path) is False:
        return False
    file_path = archive_path.split("/")[-1]
    file_name = file_path.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_path)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(file_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(file_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file_path, file_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file_path)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(file_name, file_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
