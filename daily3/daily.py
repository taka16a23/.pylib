#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Name: daily.py

# Check Tomorrow Weather
# Read News
    - Read RSS
    - Read Chart
    - Foreign News
    - Nation News

# Diary
    - write diary
       - write daily Routine
       - write memo

    - Read past diary

# Recipe
    - Archive Recipe
    - Check Tomorrow Recipe

# Create Recipe
    - create recipe on thursday

# V2C
# Feedly

"""
from time import sleep
import sys
import os
import argparse
import subprocess as sbp

from confirm import yesnodialog
from t1.dateutil import now_weekday
from junk.mypsutil import psexists
from pathhandler import PathHandler
from mygoogle import chrome
from task import TaskManager, Task
from mypcs.king import King
import xcb, xcb.xproto, xcb.screensaver

from daily3 import exe
from daily3 import log
from daily3.debug import LoggingTaskManager


# for debug
import cgitb
cgitb.enable(format='text')

__version__ = '0.0.1'


EXE_PATH = PathHandler(exe.__file__).get_dirname()


class Prepare(Task):
    r"""Prepare

    Prepare is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        # close all thunar
        os.system(u'{} {}'.format(sys.executable,
                                  EXE_PATH.join('thunar.py')))


class ReadRSS(Task):
    r"""ReadRSS

    ReadRSS is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.Popen([sys.executable, EXE_PATH.join('sleipnir_launcher.py')])
        sleep(10)


class Sleep(Task):
    r"""Sleep

    Sleep is a object.
    Responsibility:
    """
    def __init__(self, interval):
        r"""

        @Arguments:
        - `display`:
        """
        self._interval = interval

    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        conn = xcb.connect()
        root = conn.get_setup().roots[0].root
        ex = conn(xcb.screensaver.key)
        idle = ex.QueryInfo(root).reply().ms_since_user_input
        return 180000 <= idle # 30 min

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sleep(self._interval)


class ShowWeather(Task):
    r"""ShowWeather

    ShowWeather is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('weather.py')))


class CreateRecipe(Task):
    r"""CreateRecipe

    CreateRecipe is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return now_weekday().is_thursday()

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        while psexists('Sleipnir.exe'):
            sleep(1)
        sbp.Popen([sys.executable, u'{}'.format(EXE_PATH.join('create_recipe.py'))])
        sbp.Popen([sys.executable, EXE_PATH.join('coop_database.py')])
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('mapping_menus.py')))
        if yesnodialog('Prompt', 'king halt?'):
            with King() as ki:
                ki.halt()


class ReadNews(Task):
    r"""ReadNews

    ReadNews is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('chrome_move.py')))
        os.system(
            u'{} {}'.format(
                sys.executable, EXE_PATH.join('webpage.py --daily --market')))
        while psexists('Sleipnir.exe'):
            sleep(1)
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('webpage.py --foreign')))
        if not now_weekday().is_saturday():
            return
        if not yesnodialog('Prompt', 'Please Click OK will next: '):
            return
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('webpage.py --nation')))


class MagazineCheck(Task):
    r"""MagazineCheck

    MagazineCheck is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return now_weekday().is_saturday()

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.check_call(
            (sys.executable, EXE_PATH.join('webpage.py'), '--magazine'))


class ArchiveRecipe(Task):
    r"""ArchiveRecipe

    ArchiveRecipe is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('archiving_recipe.py')))


class Etc(Task):
    r"""Etc

    Etc is a object.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        chrome.run('http://feedly.com/index.html#latest')
        os.system('/opt/v2c/v2c')
        sleep(10)


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument('--debug',
                        dest='debug',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Debug mode.')

    # (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    tmanager = TaskManager('/tmp/daily3.pickle')
    tmanager.add_observer(LoggingTaskManager())
    interval = 300
    if not sys.stdout.isatty:
        from daily3.notifier import Notifier
        tmanager.add_observer(Notifier(3000))
    if opts.debug:
        log.LOG.setLevel(log.logging.DEBUG)
        interval = 30
    if not tmanager.is_pickled():
        tmanager.add_task(Prepare())
        tmanager.add_task(ReadRSS())
        tmanager.add_task(Sleep(interval))
        tmanager.add_task(ShowWeather())
        tmanager.add_task(Sleep(interval))
        tmanager.add_task(CreateRecipe())
        tmanager.add_task(ReadNews())
        tmanager.add_task(MagazineCheck())
        tmanager.add_task(ArchiveRecipe())
        tmanager.add_task(Etc())
    tmanager.start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# daily.py ends here
