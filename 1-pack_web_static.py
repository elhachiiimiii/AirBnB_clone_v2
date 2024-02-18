#!/usr/bin/python3
# should generates .tgz archive from the web
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """should create .tgz file"""
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
