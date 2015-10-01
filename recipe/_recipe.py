#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" recipe -- my recipe info


"""
import os
import sys as _sys
import datetime

from dotavoider import ListDotAvoider
from t1.dateutil import (MONDAY, TUESDAY, WEDNESDAY,
                         THURSDAY, FRIDAY, SATURDAY, SUNDAY, WeekDay)
from mypath import MyArchive
from mygoogle import chrome


__version__ = '0.1.0'

###############################################################################
# Setting Variables
ARCHIVE_PATH = MyArchive().get_path().join('ref/recipe')
DIR_LINK_NAME = 'thisweek'
BASEDIR = os.path.expanduser('~/recipe')
MAXDIRNUM = 4
RECIPE_URL = 'http://taka16.no-ip.info:8000/'
# today
TODAY_LINK_NAME = 'today'
SEIKYO_URL = 'https://shop.nanairo.coop/front/bb/shiga/common/login?pc=15041000&b=TmpBean--2076791836'
###############################################################################

LINKPATH = os.path.join(BASEDIR, DIR_LINK_NAME)

WEEK = {MONDAY:     '4mon',
        TUESDAY:    '5tue',
        WEDNESDAY:  '6wed',
        THURSDAY:   '0thu',
        FRIDAY:     '1fri',
        SATURDAY:   '2sta',
        SUNDAY:     '3sun'}


def show_recipe_schedule():
    r"""SUMMARY

    show_recipe_schedule()

    @Return:

    @Error:
    """
    chrome.run('http://taka16.no-ip.info:8000/')


class Recipe(object):
    r"""
    """
    _subdirname = WEEK
    _maxdir = 4

    def __init__(self, dirlinkname=None, basedir=None, todaylinkname=None):
        r"""

        @Arguments:
        - `dirlinkname`:
        - `basedir`:
        - `todaylinkname`:
        """
        self._dirlinkname = dirlinkname or DIR_LINK_NAME
        self.basedir = basedir or BASEDIR
        self._todaylinkname = todaylinkname or TODAY_LINK_NAME

    @property
    def todaydir(self, ):
        r"""SUMMARY

        todaypath()

        @Return:
        """
        if not self.weekdir:
            return ''
        weekday = self._subdirname.get(datetime.date.today().weekday())
        return os.path.join(self.weekdir, weekday)

    @property
    def next_recipedir(self, ):
        r"""SUMMARY

        next_recipedir()

        @Return:
        """
        return os.path.realpath(os.path.join(self.basedir, self._todaylinkname,))

    def today_dir(self, ):
        r"""SUMMARY

        today_dir()

        @Return:

        @Error:
        """
        weekday = self._subdirname.get(datetime.date.today().weekday())
        return os.path.join(self.weekdir, weekday)

    @property
    def weekdirlink(self, ):
        r"""SUMMARY

        weekdirlink()

        @Return:
        """
        return os.path.join(self.basedir, self._dirlinkname)

    @property
    def weekdir(self, ):
        r"""SUMMARY

        weekdir()

        @Return:
        """
        if not os.path.islink(self.weekdirlink):
            return ''
        return os.path.realpath(self.weekdirlink)

    @property
    def todaylink(self, ):
        r"""SUMMARY

        todaylink()

        @Return:
        """
        return os.path.join(self.basedir, self._todaylinkname)

    def list_todays(self, ):
        r"""SUMMARY

        list_todays()

        @Return:

        @Error:
        """
        try:
            menulist = os.listdir(self.todaydir)
        except OSError:
            menulist = ()
        return menulist

    def get_today_menus(self):
        r"""SUMMARY

        get_today_menus()

        @Return:
        """
        menus, append = ListDotAvoider().append
        for elem in self.list_todays():
            fname, _ = os.path.splitext(elem) # trim extension
            append(fname)
        return menus

    def lotate_weeklink(self, ):
        r"""SUMMARY

        lotateweeklink()

        @Return:
        """
        if self.weekdir:
            dirnum = int(os.path.basename(self.weekdir))
            if dirnum == self._maxdir:
                dirnum = 1
            else:
                dirnum += 1
            os.unlink(self.weekdirlink)
            dir_ = os.path.join(self.basedir, str(dirnum),)
            os.symlink(dir_, self.weekdirlink)
        else:
            if os.path.exists(self.weekdirlink):
                os.remove(self.weekdirlink)
            dir_ = os.path.join(self.basedir, '1')
            os.symlink(dir_, self.weekdirlink)
        return (dir_, self.weekdirlink)

    def lotate_todaylink(self, timedelta=None):
        r"""SUMMARY

        lotate_todaylink()

        @Return:
        """
        today = datetime.date.today()
        if timedelta and isinstance(timedelta, datetime.timedelta):
            today += timedelta
        weekday = self._subdirname.get(today.weekday())
        targetdir = os.path.join(self.weekdir, weekday)
        if os.path.exists(self.todaylink):
            os.remove(self.todaylink)
        os.symlink(targetdir, self.todaylink)
        return (targetdir, self.todaylink)


def getrealpath():
    r"""SUMMARY

    getrealpath()

    @Return:
    """
    if os.path.islink(LINKPATH):
        return os.path.realpath(LINKPATH)
    return ''

def get_latest_path():
    r"""SUMMARY

    get_latest_path()

    @Return:
    """
    realpath = getrealpath()
    if not realpath:
        return ''
    weekday = WEEK.get(datetime.date.today().weekday())
    recipe_latest_path = os.path.join(realpath, weekday)
    return recipe_latest_path

def get_today_menus():
    r"""SUMMARY

    get_today_menus()

    @Return:
    """
    try:
        menulist = os.listdir(get_latest_path())
    except OSError:
        menulist = ()
    menus, append = ListDotAvoider().append
    for elem in menulist:
        fname, _ = os.path.splitext(elem)
        append(fname)
    return menus


def rotate_link():
    r"""SUMMARY

    rotate_link()

    @Return:
    """
    realpath = getrealpath()
    if realpath:
        dirnum = int(os.path.basename(realpath))
        if dirnum == MAXDIRNUM:
            dirnum = 1
        else:
            dirnum += 1
        os.unlink(LINKPATH)
        os.symlink(os.path.join(BASEDIR, str(dirnum),), LINKPATH)
    else:
        if os.path.exists(LINKPATH):
            os.remove(LINKPATH)
        os.symlink(os.path.join(BASEDIR, '1'), LINKPATH)


def reciped():
    r"""SUMMARY

    reciped()

    @Return:
    """
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    import BaseHTTPServer
    os.chdir(Recipe().basedir)
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('', 8000), SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(reciped())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# recipe.py ends here
