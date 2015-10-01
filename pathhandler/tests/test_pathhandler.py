#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_pathhandler.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
import os
from mocker import *
import tempfile
import posix
from collections import Iterable
from pathhandler._handler2 import PathHandler
import io


class TestBase(MockerTestCase):
    """2015/02/04"""
    @classmethod
    def setUpClass(cls):
        cls.tmpdir = tempfile.gettempdir()
        os.chdir(cls.tmpdir)
        cls.tmpfile1 = tempfile.NamedTemporaryFile(suffix='.tes')
        cls.filename1 = cls.tmpfile1.name
        cls.obj1 = PathHandler(cls.filename1)

    def setUp(self):
        self.tmpfile2 = tempfile.NamedTemporaryFile(suffix='.tes')
        self.filename2 = self.tmpfile2.name
        self.obj2 = PathHandler(self.filename2)
        self.mocker.replay()

    def tearDown(self):
        pass
        # if os.path.exists(self.filename2):
        #     os.remove(self.filename2)

    @classmethod
    def tearDownClass(cls, ):
        pass
        # if os.path.exists(cls.filename1):
        #     os.remove(cls.filename1)


class TestTypesPathHandler(TestBase):
    """2015/02/04"""
    def test_from_cwd(self, ):
        self.assertIsInstance(PathHandler.from_cwd(), PathHandler)

    def test_copy(self, ):
        dst = tempfile.mktemp(suffix='.tes')
        self.assertIsInstance(self.obj2.copy(dst=dst, ), PathHandler)
        # if os.path.exists(dst):
        #     os.remove(dst)

    def test_copytree(self, ):
        src = tempfile.mkdtemp()
        dst = tempfile.mktemp()
        self.assertIsNone(PathHandler(src).copytree(dst), None)
        for dir_ in (src, dst):
            if os.path.exists(dir_):
                os.rmdir(dir_)

    def test_copymode(self, ):
        self.assertIsNone(self.obj1.copymode(self.filename2))

    def test_copystat(self, ):
        self.assertIsNone(self.obj1.copystat(self.filename2))

    def test_exists(self, ):
        self.assertIsInstance(self.obj2.exists(), bool)

    def test_expanduser(self, ):
        self.assertIsInstance(self.obj2.expanduser(), PathHandler)

    def test_expandvars(self, ):
        self.assertIsInstance(self.obj2.expandvars(), PathHandler)

    def test_get_absolute(self, ):
        self.assertIsInstance(self.obj2.get_absolute(), PathHandler)

    def test_atime(self, ):
        self.assertIsInstance(self.obj2.get_atime(), float)

    def test_get_basename(self, ):
        self.assertIsInstance(self.obj2.get_basename(), PathHandler)

    def test_get_conf(self, ):
        self.assertIsInstance(self.obj2.get_conf(name='PC_MAX_INPUT'), int)

    def test_get_ctime(self, ):
        self.assertIsInstance(self.obj2.get_ctime(), float)

    def test_get_drive(self, ):
        self.assertIsInstance(self.obj2.get_drive(), PathHandler)

    def test_get_extension(self, ):
        self.assertTrue(isinstance(self.obj2.get_extension(), (str, unicode)))
        # self.assertIsInstance(self.obj2.get_extension(), str)

    def test_get_mtime(self, ):
        self.assertIsInstance(self.obj2.get_mtime(), float)

    def test_get_normal(self, ):
        self.assertIsInstance(self.obj2.get_normal(), PathHandler)

    def test_get_size(self, ):
        self.assertIsInstance(self.obj2.get_size(), long)

    def test_get_stem(self, ):
        self.assertIsInstance(self.obj2.get_stem(), str)

    def test_get_stat(self, ):
        self.assertIsInstance(self.obj2.get_stat(), posix.stat_result)

    # def test_get_real(self, ):
    #     self.assertIsInstance(self.obj2.get_real(), PathHandler)

    def test_get_root(self, ):
        self.assertIsInstance(self.obj2.get_root(), PathHandler)

    def test_get_relative(self, ):
        self.assertIsInstance(self.obj2.get_relative(start='.'), PathHandler)

    def test_isabsolute(self, ):
        self.assertIsInstance(self.obj2.isabsolute(), bool)

    def test_isdir(self, ):
        self.assertIsInstance(self.obj2.isdir(), bool)

    def test_isfifo(self, ):
        self.assertIsInstance(self.obj2.isfifo(), bool)

    def test_isfile(self, ):
        self.assertIsInstance(self.obj2.isfile(), bool)

    def test_ismount(self, ):
        self.assertIsInstance(self.obj2.ismount(), bool)

    def test_issymlink(self, ):
        self.assertIsInstance(self.obj2.issymlink(), bool)

    def test_join(self, ):
        self.assertIsInstance(self.obj2.join('hello'), PathHandler)

    def test_listdir(self, ):
        obj = PathHandler(tempfile.gettempdir())
        self.assertIsInstance(obj.listdir(), list)

    def test_link(self, ):
        linkname = tempfile.mktemp(suffix='.link')
        obj = self.obj2.link(linkname)
        self.assertIsInstance(obj, PathHandler)
        obj.unlink()

    def test_mkdir(self, ):
        dirname = tempfile.mktemp()
        obj = PathHandler(dirname)
        self.assertIsNone(obj.mkdir(mode=0o777, parents=False))
        if os.path.exists(dirname):
            os.rmdir(dirname)

    def test_move(self, ):
        mvname = tempfile.mktemp(suffix='.tes')
        self.assertIsInstance(self.obj2.move(mvname), PathHandler)

    def test_open(self, ):
        self.assertTrue(
            isinstance(self.obj2.open('r'), (file, io.TextIOWrapper)))
        # self.assertIsInstance(self.obj2.open('r'), file)

    def test_samefile(self, ):
        self.assertIsInstance(self.obj2.samefile(self.filename2), bool)

    def test_splitdrive(self, ):
        self.assertIsInstance(self.obj2.splitdrive(), tuple)

    def test_splitext(self, ):
        self.assertIsInstance(self.obj2.splitext(), tuple)

    def test_walk(self, ):
        self.assertIsInstance(self.obj2.walk(), Iterable)

    def test_with_name(self, ):
        self.assertIsInstance(self.obj2.with_name(name='hello'), PathHandler)

    def test_with_ext(self, ):
        self.assertIsInstance(self.obj2.with_ext(suffix='.py'), PathHandler)


class TestPathHandler(TestBase):

    def test___init__(self, ):
        self.assertEqual(self.obj2, PathHandler(self.obj2))

    # def test___init__err(self, ):
    #     with self.assertRaises(TypeError):
    #         PathHandler(1)
    #     with self.assertRaises(TypeError):
    #         PathHandler(type)

    def test_from_cwd(self, ):
        expects = os.getcwd()
        got = PathHandler.from_cwd()
        self.assertEqual(expects, got)

    def test_chmod(self, ):
        mod = 0o777
        self.assertIsNone(self.obj2.chmod(mode=mod))
        self.assertEqual(os.stat(self.filename2).st_mode & 0777, mod)
        mod2 = 0o555
        self.obj2.chmod(mode=mod2)
        self.assertEqual(os.stat(self.filename2).st_mode & 0777, mod2)

    def test_chown(self, ):
        uid, gid = 1000, 1000
        self.assertIsNone(self.obj2.chown(uid=uid, gid=gid))
        self.assertEqual(os.stat(self.filename2).st_uid, uid)
        self.assertEqual(os.stat(self.filename2).st_gid, gid)
        uid2, gid2 = 2000, 2000
        self.obj2.chown(uid=uid2, gid=gid2)
        self.assertEqual(os.stat(self.filename2).st_uid, uid2)
        self.assertEqual(os.stat(self.filename2).st_gid, gid2)

    def test_copy(self, ):
        dst = tempfile.mktemp(suffix='.tes')
        self.obj2.copy(dst=dst)
        self.assertTrue(os.path.exists(dst))
        # if os.path.exists(dst):
        #     os.remove(dst)

    def test_copymode(self, ):
        mod = os.stat(self.filename1).st_mode & 0777
        self.obj1.copymode(self.filename2)
        self.assertEqual(mod, os.stat(self.filename2).st_mode & 0777)

    def test_copystat(self, ):
        self.obj1.copystat(self.filename2)
        self.assertEqual(
            os.stat(self.filename1).st_mode, os.stat(self.filename2).st_mode)
        self.assertEqual(
            os.stat(self.filename1).st_dev, os.stat(self.filename2).st_dev)
        self.assertEqual(
            os.stat(self.filename1).st_nlink, os.stat(self.filename2).st_nlink)
        self.assertEqual(
            os.stat(self.filename1).st_uid, os.stat(self.filename2).st_uid)
        self.assertEqual(
            os.stat(self.filename1).st_gid, os.stat(self.filename2).st_gid)
        self.assertEqual(
            os.stat(self.filename1).st_size, os.stat(self.filename2).st_size)
        # self.assertEqual(
        #     os.stat(self.filename1).st_atime, os.stat(self.filename2).st_atime)
        # self.assertEqual(
        #     os.stat(self.filename1).st_mtime, os.stat(self.filename2).st_mtime)
        # self.assertEqual(
        #     os.stat(self.filename1).st_ctime, os.stat(self.filename2).st_ctime)

    def test_exists(self, ):
        self.assertTrue(self.obj2.exists())

    def test_expanduser(self, ):
        expects = os.path.expanduser('~')
        got = PathHandler('~').expanduser()
        self.assertEqual(expects, got)

    def test_expandvars(self, ):
        expects = os.path.expandvars('$HOME')
        got = PathHandler('$HOME').expandvars()
        self.assertEqual(expects, got)

    def test_get_absolute(self, ):
        fname = os.path.split(self.filename2)[-1]
        expects = os.path.abspath(fname)
        got = PathHandler(fname).get_absolute()
        self.assertEqual(expects, got)

    def test_get_atime(self, ):
        self.assertEqual(
            os.path.getatime(self.filename2), self.obj2.get_atime())

    def test_get_basename(self, ):
        expects = os.path.basename(self.filename2)
        got = self.obj2.get_basename()
        self.assertEqual(expects, got)

    def test_get_conf(self, ):
        expects = os.pathconf(self.filename2, 'PC_MAX_INPUT')
        got = self.obj2.get_conf('PC_MAX_INPUT')
        self.assertEqual(expects, got)

    def test_get_ctime(self, ):
        self.assertEqual(
            os.path.getctime(self.filename2), self.obj2.get_ctime())

    def test_get_drive(self, ):
        drive, _ = os.path.splitdrive(self.filename2)
        got = self.obj2.get_drive()
        self.assertEqual(drive, got)

    def test_get_dirname(self, ):
        expects = os.path.dirname(self.filename2)
        got = self.obj2.get_dirname()
        self.assertEqual(expects, got)

    def test_get_extension(self, ):
        expects = os.path.splitext(self.filename2)[-1]
        got = self.obj2.get_extension()
        self.assertEqual(expects, got)

    def test_get_mtime(self, ):
        self.assertEqual(
            os.path.getmtime(self.filename2), self.obj2.get_mtime())

    def test_get_normal(self, ):
        # TODO: (Atami) [2015/02/05]
        # write windows version
        pth = '/tmp//' + os.path.basename(self.filename2)
        expects = os.path.normpath(pth)
        got = self.obj2.get_normal()
        self.assertEqual(expects, got)

    def test_get_size(self, ):
        expects = os.path.getsize(self.filename2)
        got = self.obj2.get_size()
        self.assertEqual(expects, got)

    def test_get_stem(self, ):
        expects = os.path.splitext(os.path.basename(self.filename2))[0]
        got = self.obj2.get_stem()
        self.assertEqual(expects, got)

    # def test_get_real(self, ):
    #     tmp = tempfile.mktemp()
    #     os.link(self.filename2, tmp)
    #     got = PathHandler(tmp).get_real()
    #     self.assertEqual(self.obj2, got)
    #     if os.path.exists(tmp):
    #         os.unlink(tmp)

    def test_get_root(self, ):
        # TODO: (Atami) [2015/02/05]
        # write windows version
        self.assertEqual('/', self.obj2.get_root())

    def test_get_relative(self, ):
        expects = os.path.relpath(self.filename2, '.')
        got = self.obj2.get_relative('.')
        self.assertEqual(expects, got)

    def test_isabsolute(self, ):
        self.assertTrue(self.obj2.isabsolute())
        self.assertFalse(PathHandler('tes.ts').isabsolute())

    def test_isdir(self, ):
        self.assertTrue(PathHandler(self.tmpdir).isdir())
        self.assertFalse(self.obj2.isdir())

    def test_isfifo(self, ):
        # TODO: (Atami) [2015/02/05]
        # test fifo file
        self.assertFalse(self.obj2.isfifo())

    def test_isfile(self, ):
        self.assertTrue(self.obj2.isfile())
        self.assertFalse(PathHandler(self.tmpdir).isfile())

    def test_ismount(self, ):
        self.assertTrue(PathHandler('/').ismount())
        self.assertFalse(self.obj2.ismount())

    def test_issymlink(self, ):
        tmp = tempfile.mktemp()
        os.symlink(self.filename2, tmp)
        self.assertTrue(PathHandler(tmp).issymlink())
        if os.path.exists(tmp):
            os.unlink(tmp)

    def test_join(self, ):
        name = 'hello.tes'
        expects = os.path.join(self.filename2, name)
        got = self.obj2.join(name)
        self.assertEqual(expects, got)

    def test_listdir(self, ):
        for pth in PathHandler(self.tmpdir).listdir():
            self.assertIsInstance(pth, PathHandler)

    def test_link(self, ):
        tmp = tempfile.mktemp()
        self.obj2.link(tmp)
        self.assertTrue(os.path.islink(tmp))
        if os.path.exists(tmp):
            os.unlink(tmp)

    def test_mkdir(self, ):
        tmpdir = tempfile.mktemp()
        PathHandler(tmpdir).mkdir(0o555)
        self.assertTrue(os.path.isdir(tmpdir))
        if os.path.exists(tmpdir):
            os.rmdir(tmpdir)
        tmpdir2 = tempfile.mktemp()
        tmpdir2sub = os.path.join(tmpdir2, 'hello')
        PathHandler(tmpdir2sub).mkdir(0o555, parents=True)
        self.assertTrue(os.path.isdir(tmpdir2sub))
        if os.path.exists(tmpdir2sub):
            os.rmdir(tmpdir2sub)
        if os.path.exists(tmpdir2):
            os.rmdir(tmpdir2)

    def test_move(self, ):
        dst = tempfile.mktemp(suffix='.tes')
        self.obj2.move(dst=dst)
        self.assertTrue(os.path.exists(dst))
        self.assertFalse(os.path.exists(self.filename2))
        # if os.path.exists(dst):
        #     os.remove(dst)

    def test_open(self, ):
        fobj = self.obj2.open('wb')
        expects = 'hello'
        fobj.write(expects)
        fobj.close()
        fobj2 = open(self.filename2, 'rb')
        self.assertEqual(expects, fobj2.read())
        fobj2.close()

    def test_readlink(self, ):
        tmp = tempfile.mktemp()
        os.symlink(self.filename2, tmp)
        got = PathHandler(tmp).readlink()
        self.assertEqual(self.obj2, got)
        if os.path.exists(tmp):
            os.unlink(tmp)

    def test_remove(self, ):
        self.assertTrue(os.path.exists(self.filename2))
        self.obj2.remove()
        self.assertFalse(os.path.exists(self.filename2))

    def test_rename(self, ):
        self.assertTrue(os.path.exists(self.filename2))
        rename = tempfile.mktemp()
        self.obj2.rename(rename)
        self.assertFalse(os.path.exists(self.filename2))
        self.assertTrue(os.path.exists(rename))
        # if os.path.exists(rename):
        #     os.remove(rename)

    def test_samefile(self, ):
        self.assertTrue(self.obj2.samefile(self.filename2))

    def test_splitdrive(self, ):
        self.assertEqual(
            os.path.splitdrive(self.filename2), self.obj2.splitdrive())

    def test_splitext(self, ):
        self.assertEqual(
            os.path.splitext(self.filename2), self.obj2.splitext())

    def test_touch(self, ):
        tmp = tempfile.mktemp()
        self.assertFalse(os.path.exists(tmp))
        PathHandler(tmp).touch()
        self.assertTrue(os.path.exists(tmp))
        # if os.path.exists(tmp):
        #     os.remove(tmp)

    def test_unlink(self, ):
        tmp = tempfile.mktemp()
        link = self.obj2.link(tmp)
        self.assertTrue(os.path.islink(tmp))
        link.unlink()
        self.assertFalse(os.path.exists(tmp))
        if os.path.exists(tmp):
            os.unlink(tmp)

    def test_walk(self, ):
        self.skipTest('Not Implemented')

    def test_with_name(self, ):
        name = 'hello.ts'
        expects = os.path.join(self.tmpdir, name)
        got = self.obj2.with_name(name)
        self.assertEqual(expects, got)

    def test_with_ext(self, ):
        ext = '.py'
        expects = os.path.splitext(self.filename2)[0] + ext
        got = self.obj2.with_ext(ext)
        self.assertEqual(expects, got)

    def test___ne__(self, ):
        self.assertNotEqual(self.obj1, self.obj2)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_pathhandler.py ends here
