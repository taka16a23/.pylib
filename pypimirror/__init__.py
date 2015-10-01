#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import sys
import os
from os import path
from pathhandler import PathHandler

import xmlrpclib
import urllib2
from abstract.singleton import SingletonMeta
from xml.etree import ElementTree
import httplib
import cPickle
import time
import urlparse
import pip
import threading

from pep381client.sqlite import SqliteStorage
if sys.version_info < (2, 4):
    from sets import Set as set

if sys.version_info < (2, 4):
    from sets import Set as set




__version__ = "0.1.0"

__all__ = [ '' ]

NETLOC = 'pypi.python.org'
BASE_URL = 'https://' + NETLOC
PYPI_URL = BASE_URL + '/pypi'
SIMPLE_URL = BASE_URL + '/simple/'
USER_AGENT = 'pypimirror/' + __version__


def gethtml(url):
    r"""SUMMARY

    gethtml(project='')

    @Arguments:
    - `project`:

    @Return:
    """
    try:
        fobj = urllib2.urlopen(url)
    except urllib2.HTTPError, err:
        if err.code == 404:
            return None
        elif err.code == 301:
            return None
        else:
            raise
    if fobj.code != 200:
        raise ValueError('Status {} on {}'.format(fobj.status, url))
    return fobj.read()


def savefile(fpath, data):
    r"""SUMMARY

    savefile(fpath)

    @Arguments:
    - `fpath`:

    @Return:
    """
    with open(fpath, 'wb') as fobj:
        fobj.write(data)


def download(url, dest):
    r"""SUMMARY

    download()

    @Return:
    """
    html = gethtml(url)
    if html:
        savefile(dest, html)


def parse_html(data):
    r"""SUMMARY

    parse_html(data)

    @Arguments:
    - `data`:

    @Return:
    """
    soup = ElementTree.fromstring(data)
    res = []
    append = res.append
    for elm_a in soup.findall(".//a"):
        url = elm_a.attrib['href']
        if not url.startswith('../../packages/'):
            continue
        url = url.split('#')[0]
        url = url[len('../..'):]
        append(url)
    return res


class PYPI_RPC(object, xmlrpclib.ServerProxy):
    r"""
    """
    __metaclass__ = SingletonMeta

    def __init__(self, ):
        r"""
        """
        xmlrpclib.ServerProxy.__init__(self, PYPI_URL)


class PYPI_HTTP(object, httplib.HTTPSConnection):
    r"""
    """
    __metaclass__ = SingletonMeta

    def __init__(self, ):
        r"""
        """
        httplib.HTTPSConnection.__init__(self, NETLOC)


class Info(object):
    r"""
    """
    basedir = None
    last_started = None
    pending_projects = None


    def __init__(self, ):
        r"""
        """


class PathInfo(object):
    r"""
    """
    _sqlfiles = 'files'
    _web = 'web'
    _simple = 'simple'
    _packages = 'packages'
    _signature = 'serversig'
    _local_stats_days = 'local-stats/days'
    _sapphire_devices = 'spphire-devices'

    def __init__(self, basedir):
        r"""
        """
        self.basedir = basedir

    @property
    def sqlfiles(self, ):
        r"""SUMMARY

        status()

        @Return:
        """
        return path.join(self.basedir, self._sqlfiles)

    @property
    def web(self, ):
        r"""SUMMARY

        web()

        @Return:
        """
        return path.join(self.basedir, self._web)

    @property
    def simple(self, ):
        r"""SUMMARY

        simple()

        @Return:
        """
        return path.join(self.web, self._simple)

    @property
    def packages(self, ):
        r"""SUMMARY

        packages()

        @Return:
        """
        return path.join(self.web, self._packages)

    @property
    def signature(self, ):
        r"""SUMMARY

        serversig()

        @Return:
        """
        return path.join(self.web, self._signature)

    @property
    def local_stats_days(self, ):
        r"""SUMMARY

        local_stats_days()

        @Return:
        """
        return path.join(self.web, self._local_stats_days)

    @property
    def sapphire_device(self, ):
        r"""SUMMARY

        sapphire_device()

        @Return:
        """
        return path.join(self.web, self._sapphire_devices,)


class LocalPath(PathInfo):
    r"""
    """

    def __init__(self, basedir):
        r"""

        @Arguments:
        - `basedir`:
        """
        PathInfo.__init__(self, basedir)

    def list_dirs(self, ):
        r"""SUMMARY

        list_dirs()

        @Return:
        """
        return [self.web, self.simple, self.packages, self.signature,
                self.local_stats_days, self.sapphire_device]

    def make_all_dirs(self, ):
        r"""SUMMARY

        makedirs()

        @Return:
        """
        import errno
        for dir_ in self.list_dirs():
            try:
                os.makedirs(dir_)
            except OSError as err:
                # skip if directory exists
                if not err.errno == errno.EEXIST:
                    raise


class PackageHolder(object):
    r"""
    """
    def __init__(self, ):
        r"""SUMMARY

        __init__()

        @Return:
        """
        self.pending_projects = set()

    def set_all_projects(self, ):
        r"""SUMMARY

        set_all_projects()

        @Return:
        """
        self.pending_projects.update(PYPI_RPC().list_packages())

    def set_changed_projects(self, times):
        r"""SUMMARY

        set_changed_projects(times)

        @Arguments:
        - `times`:

        @Return:
        """
        changes = PYPI_RPC().changelog(times - 1)
        if not changes:
            return False
        for change in changes:
            self.pending_projects.add(change[0])

    def get_package_list(self, ):
        r"""SUMMARY

        get_list()

        @Return:
        """
        return sorted(self.pending_projects)


class Projects(object):
    r"""
    """
    _baseurl = SIMPLE_URL

    def __init__(self, project, basedir):
        r"""

        @Arguments:
        - `project`:
        - `basedir`:
        """
        self._project = project
        self._basedir = basedir

    @property
    def simple_url(self, ):
        r"""SUMMARY

        simple_url()

        @Return:
        """
        url = urlparse.urljoin(self._baseurl, urllib2.quote(self._project))
        if not url.endswith(('/')):
            url += '/'
        return url

    @property
    def signature_url(self, ):
        r"""SUMMARY

        signature_url()

        @Return:
        """
        url = urlparse.urljoin(self._basedir, '/serversig/')
        url = urlparse.urljoin(url, urllib2.quote(self._project))
        if not url.endswith(('/')):
            url += '/'
        return url

    @property
    def signature_path(self, ):
        r"""SUMMARY

        signature_path()

        @Return:
        """
        return path.join(self._basedir, 'serversig', self._project)

    @property
    def simple_dir(self, ):
        r"""SUMMARY

        simple_dir()

        @Return:
        """
        return path.join(self._basedir, 'simple', self._project)

    @property
    def simple_index_path(self, ):
        r"""SUMMARY

        simple_index_path()

        @Return:
        """
        return path.join(self.simple_dir, 'index.html')


class ProjectsHandle(Projects):
    r"""
    """

    def __init__(self, project, basedir, sqlite):
        r"""

        @Arguments:
        - `project`:
        - `basedir`:
        - `sqlite`:
        """
        self._project = project
        self._basedir = basedir
        self._sqlite = sqlite
        Projects.__init__(self, project, basedir)

    def download(self, ):
        r"""SUMMARY

        download()

        @Return:
        """
        html = self._download_project()
        if html:
            self._download_signature()
        return html

    def _download_project(self, ):
        r"""SUMMARY

        _download_project()

        @Return:
        """
        html = gethtml(self.simple_url)
        if not html:
            return None
        if not path.exists(self.simple_dir):
            os.mkdir(self.simple_dir)
        savefile(self.simple_index_path, html)
        return html

    def _download_signature(self, ):
        r"""SUMMARY

        download_signature()

        @Return:
        """
        html = gethtml(self.signature_url)
        if not html:
            return None
        savefile(self.signature_path, html)

    def delete(self, ):
        r"""SUMMARY

        delete()

        @Return:
        """
        for file_ in self._sqlite.files(self._project):
            self.remove_file(file_)

    def remove_file(self, file_):
        r"""SUMMARY

        remove_file(file_)

        @Arguments:
        - `file_`:

        @Return:
        """
        self._sqlite.remove_file(file_)
        lpath = path.join(self._basedir, file_)
        if os.path.exists(lpath):
            os.unlink(lpath)

        if path.exists(self.simple_dir):
            if path.exists(self.simple_index_path):
                os.unlink(self.simple_index_path)
            os.rmdir(self.simple_dir)

        if path.exists(self.signature_path):
            os.unlink(self.signature_path)


class SavePickle(object):
    r"""
    """

    def __init__(self, basedir, filename='pickle'):
        r"""SUMMARY

        __init__(basedir)

        @Arguments:
        - `basedir`:

        @Return:
        """
        self.basedir = basedir
        self._pickle_fname = filename

    @property
    def pickle_file(self, ):
        r"""SUMMARY

        pickle_file()

        @Return:
        """
        return path.join(self.basedir, self._pickle_fname)

    def save_pickle(self, ):
        r"""SUMMARY

        save()

        @Return:
        """
        with open(self.pickle_file, 'wb') as fobj:
            cPickle.dump(self, fobj, cPickle.HIGHEST_PROTOCOL)

    def resume(self, ):
        r"""SUMMARY

        resume(basedir)

        @Arguments:
        - `basedir`:

        @Return:
        """
        return cPickle.load(
            open(path.join(self.basedir, self._pickle_fname), 'rb'))


class TimeState(object):
    r"""
    """
    _strffmt = '%Y%m%dT%H:%M:%S\n'

    def __init__(self, filepath, times=0):
        r"""

        @Arguments:
        - `times`:
        """
        self.last_modified_fpath = filepath
        self.last_started = times
        self.last_completed = None

    def update_time_save(self, ):
        r"""SUMMARY

        update_time_save()

        @Return:
        """
        self._update_last_started()
        self._save_last_modified()

    def _update_last_started(self, ):
        r"""SUMMARY

        update_last_started()

        @Return:
        """
        self.last_started = int(time.time())

    def _save_last_modified(self, ):
        r"""SUMMARY

        save_time_last_modified()

        @Return:
        """
        with open(self.last_modified_fpath, 'wb') as fobj:
            str_ = time.strftime(self._strffmt, time.gmtime(self.last_started))
            fobj.write(str_)


class HandleTempName(SqliteStorage, LocalPath, SavePickle):
    r"""
    """

    def __init__(self, targetdir):
        r"""
        """
        LocalPath.__init__(self, targetdir)
        SqliteStorage.__init__(self, self.sqlfiles)
        SavePickle.__init__(self, self.basedir)
        self.pending_projects = None

    def save(self, ):
        r"""SUMMARY

        save()

        @Return:
        """
        SavePickle.save_pickle(self)
        self.commit()




def get_simple_page(project=None):
    r"""SUMMARY

    get_simple_page(project=None)

    @Arguments:
    - `project`:

    @Return:
    """
    url = SIMPLE_URL
    if project:
        project = project.encode('utf-8')
        url += urllib2.quote(project) + '/'
    try:
        fobj = urllib2.urlopen(url)
    except urllib2.HTTPError, err:
        print(err)
        print(err.url)
        return None
    html = fobj.read()



# get target directory
# create target, /archive, /source directory if not exists

# check pickle file in target directory
# resume if exists pickle file
#    add pending change log
# if not exists pickle file
#    list all package list
#
# get package url
# if exists package directory in /source, /archive
#     remove package directory in /source, /archive
# if not exists package directory in /archive
#     make directory in /archive

# download and save in /archive
# extract archive to /source package directory

# save pickle on target directory

# from pip import util
# util.unpack_file('/tmp/paramiko-1.12.0.tar.gz', '/tmp', '', '')

class PackageInfo(object):
    r"""
    """
    _archive_dir = 'archive'
    _source_dir = 'source'
    _baseurl = SIMPLE_URL

    def __init__(self, name, basedir):
        r"""

        @Arguments:
        - `project`:
        - `basedir`:
        """
        self._name = name
        self._basedir = basedir

    @property
    def simple_url(self, ):
        r"""SUMMARY

        simple_url()

        @Return:
        """
        url = urlparse.urljoin(self._baseurl, urllib2.quote(self._name))
        if not url.endswith(('/')):
            url += '/'
        return url

    # @property
    # def archive_dir(self, ):
    #     r"""SUMMARY

    #     archive_dir()

    #     @Return:
    #     """
    #     return path.join(self._basedir, self._archive_dir, self._name)

    # @property
    # def source_dir(self, ):
    #     r"""SUMMARY

    #     source_dir()

    #     @Return:
    #     """
    #     return path.join(self._basedir, self._source_dir, self._name)


class Package(PackageInfo):
    r"""
    """
    _baseurl = SIMPLE_URL

    def __init__(self, name):
        r"""

        @Arguments:
        - `basedir`:
        - `name`:
        """
        self.name = name

    def get_latest_url(self, ):
        r"""SUMMARY

        get_latest_url()

        @Return:
        """
        files = self.list_files()
        if not files:
            return None
        return urlparse.urljoin(self._baseurl, sorted(set(files))[-1])

    def list_files(self, ):
        r"""SUMMARY

        list_files()

        @Return:
        """
        html = gethtml(self.simple_url)
        if not html:
            return None
        return parse_html(html)

    @property
    def simple_url(self, ):
        r"""SUMMARY

        simple_url()

        @Return:
        """
        url = urlparse.urljoin(self._baseurl, urllib2.quote(self.name))
        if not url.endswith(('/')):
            url += '/'
        return url



class PYPILATEST(PackageHolder):
    r"""
    """
    _archive_dir = 'archive'
    _source_dir = 'source'

    def __init__(self, basedir):
        r"""
        """
        PackageHolder.__init__(self)
        self.basedir = basedir
        self.failed = []
        # SavePickle.__init__(self, basedir)
        # self.last_started = 0
        # self.last_modified = None
        # self.last_completed = None


    def init(self, ):
        r"""SUMMARY

        init()

        @Return:
        """
        for dir_ in (self.basedir, self.archive_dir, self.source_dir):
            path = PathHandler(dir_)
            if not path.isdir():
                path.mkdir(0777)

    # def first_run(self, ):
    #     r"""SUMMARY

    #     first_run()

    #     @Return:
    #     """
    #     self.set_all_projects()

    # def load_changelog(self, ):
    #     r"""SUMMARY

    #     requme()

    #     @Return:
    #     """
    #     if self.last_completed:
    #         changes = PYPI_RPC().changelog(self.last_completed -1)
    #         self.last_completed = None
    #         for change in changes:
    #             self.pending_projects.add(change[0])

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        self.set_all_projects()
        self.init()
        mainthread = threading.currentThread()
        for pkg in self.get_package_list():
            thrd = threading.Thread(target=self._run, args=(pkg, ))
            thrd.start()
            # self._run(pkg)
        for thd in threading.enumerate():
            if mainthread != thd:
                thd.join()
        print('### Failed.')
        for pkg in self.failed:
            print(pkg)

    def _run(self, pkg):
        r"""SUMMARY

        _run(pkg)

        @Arguments:
        - `pkg`:

        @Return:
        """
        try:
            pkgobj = Package(pkg)
            pkgdir = PathHandler(path.join(self.archive_dir, pkgobj.name))
            if not pkgdir.isdir():
                pkgdir.mkdir(0777)
            url = pkgobj.get_latest_url()
            if not url:
                self.failed.append(pkg)
                return
            print('Downloaded {}'.format(url))
            filename = url.split('/')[-1]
            dest = path.join(pkgdir, filename)
            download(url, dest)
            src_dest = PathHandler(path.join(self.source_dir, pkg))
            if not src_dest.isdir():
                src_dest.mkdir()
            pip.util.unpack_file(dest, src_dest, '', '')
            print('Successed {}\n\n'.format(dest))
        except KeyboardInterrupt:
            sys.exit(os.EX_OK)
        except:
            print('!!! Failed {}\n\n'.format(pkg))
            self.failed.append(pkg)



    @property
    def archive_dir(self, ):
        r"""SUMMARY

        archive_dir()

        @Return:
        """
        return path.join(self.basedir, self._archive_dir)

    @property
    def source_dir(self, ):
        r"""SUMMARY

        archive_dir()

        @Return:
        """
        return path.join(self.basedir, self._source_dir)


def mirror(basedir):
    r"""SUMMARY

    mirror(basedir)

    @Arguments:
    - `basedir`:

    @Return:
    """
    pypimirror = PYPILATEST(basedir)
    pypimirror.run()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
