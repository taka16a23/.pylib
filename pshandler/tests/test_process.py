#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_process.py

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
from mocker import *
from time import sleep
import os as _os
import sys as _sys
import getpass
from subprocess import PIPE
from pshandler._handler import ProcessHandler, Popen
from pshandler import _ntuple, _status, _err, _func


class TestProcessHandler(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.cmdlines = ["python", "-c", "print 'hi'"]
        cls.subproc = Popen(['python', 'spawn_child.py'], stdout=PIPE)

    def setUp(self):
        self.ps = Popen(self.cmdlines, stdout=PIPE)
        self.mocker.replay()

    def test_constract_err(self, ):
        with self.assertRaises(TypeError):
            ProcessHandler('')

    def test_get_pid_type(self, ):
        self.assertIsInstance(self.ps.get_pid(), int)

    def test_get_parent(self, ):
        for ps in _func.list_process():
            if ps.get_name() == 'nosetests':
                parent = ps
                break
        self.assertEqual(parent, self.ps.get_parent())

    def test_get_parent_type(self, ):
        self.assertIsInstance(self.ps.get_parent(), ProcessHandler)

    def test_get_name(self, ):
        self.assertEqual('python', self.ps.get_name())

    def test_get_name_type(self, ):
        self.assertIsInstance(self.ps.get_name(), str)

    # def test_get_path(self, ):
    #     self.assertEqual('', self.ps.get_path())

    def test_get_path_type(self, ):
        self.assertIsInstance(self.ps.get_path(), str)

    def test_get_status(self, ):
        sleep(2) # wait to zombie
        status = self.ps.get_status()
        self.assertEqual(_status.ZOMBIE, status)

    def test_get_status_type(self, ):
        self.assertIsInstance(self.ps.get_status(), str)

    def test_get_cmdline(self, ):
        cmdline = self.ps.get_cmdline()
        self.assertListEqual(self.cmdlines, cmdline)

    def test_get_cmdline_type(self, ):
        cmdline = self.ps.get_cmdline()
        self.assertIsInstance(cmdline, list)
        for el in cmdline:
            self.assertIsInstance(el, str)

    def test_get_username(self, ):
        user = getpass.getuser()
        self.assertEqual(user, self.ps.get_username())

    def test_get_username_type(self, ):
        self.assertIsInstance(self.ps.get_username(), str)

    def test_get_create_time_type(self, ):
        self.assertIsInstance(self.ps.get_create_time(), float)

    def test_get_cwd(self, ):
        cwd = _os.path.dirname(__file__)
        self.assertEqual(cwd, self.ps.get_cwd())

    def test_get_cwd_type(self, ):
        self.assertIsInstance(self.ps.get_cwd(), str)

    def test_get_nice(self, ):
        nice = 0
        self.assertEqual(nice, self.ps.get_nice())

    def test_set_nice(self, ):
        self.ps.set_nice(1)
        self.assertEqual(1, self.ps.get_nice())

    def test_get_nice_type(self, ):
        self.assertIsInstance(self.ps.get_nice(), int)

    def test_get_memory_info_type(self, ):
        self.assertIsInstance(self.ps.get_memory_info(), _ntuple.PSMEM)

    def test_suspend(self, ):
        self.ps.suspend()
        sleep(0.2)
        self.assertEqual('stopped', self.ps.get_status())

    def test_resume(self, ):
        self.test_suspend()
        self.ps.resume()
        sleep(0.2)
        self.assertNotEqual('stopped', self.ps.get_status())

    def test_is_running(self, ):
        self.assertTrue(self.ps.is_running())

    def test_is_running_type(self, ):
        self.assertIsInstance(self.ps.is_running(), bool)

    def test_list_threads_type(self, ):
        threads = self.ps.list_threads()
        self.assertIsInstance(threads, list)
        self.failIfEqual(threads, [])
        for thread in threads:
            self.assertIsInstance(thread, _ntuple.PSThread)

    def test_list_children_type(self, ):
        sleep(2) # wait launch
        children = self.subproc.list_children()
        self.assertIsInstance(children, list)
        self.failIfEqual(children, [])
        self.assertEqual(len(children), 1)
        for child in children:
            self.assertIsInstance(child, ProcessHandler)

    def test_recursive_children_type(self, ):
        sleep(2) # wait launch
        children = self.subproc.recursive_children()
        self.assertIsInstance(children, list)
        self.failIfEqual(children, [])
        self.assertEqual(len(children), 2)
        for child in children:
            self.assertIsInstance(child, ProcessHandler)

    def test_get_cpu_percent_type(self, ):
        self.assertIsInstance(self.ps.get_cpu_percent(), float)

    def test_get_cpu_times_type(self, ):
        self.assertIsInstance(self.ps.get_cpu_times(), _ntuple.PSCpuTimes)

    # def test_list_open_files_type(self, ):
    #     sleep(2)
    #     open_files = self.subproc.list_open_files()
    #     self.assertIsInstance(open_files, list)
    #     self.failIfEqual(open_files, [])
    #     for f in open_files:
    #         self.assertIsInstance(f, _ntuple.PSOpenFile)

    def test_list_connections_type(self, ):
        sleep(2)
        connections = self.subproc.list_connections()
        self.assertIsInstance(connections, list)
        self.failIfEqual(connections, [])
        for conn in connections:
            self.assertIsInstance(conn, _ntuple.PSCONN)

    def test_wait_timeout(self, ):
        with self.assertRaises(_err.Timeout):
            self.subproc.wait(timeout=1)

    def test_wait_type(self, ):
        self.ps.terminate()
        ret = self.ps.wait(timeout=5)
        self.assertIsInstance(ret, int)

    if _os.name == 'nt':
        def test_get_num_handles_type(self, ):
            self.skipTest('Not Implemented')

        def test_get_ionice_type(self, ):
            self.skipTest('Not Implemented')

        def test_get_io_counters_type(self, ):
            self.skipTest('Not Implemented')

    if _os.name == 'posix':
        def test_get_uids_type(self, ):
            self.assertIsInstance(self.ps.get_uids(), _ntuple.PSUIDs)

        def test_get_gids_type(self, ):
            self.assertIsInstance(self.ps.get_gids(), _ntuple.PSGIDs)

        def test_get_terminal_type(self, ):
            self.assertIsInstance(self.ps.get_terminal(), str)

        def test_num_fds_type(self, ):
            self.assertIsInstance(self.ps.num_fds(), int)

    if _sys.platform.startswith(('linux')):
        def test_get_ionice_type(self, ):
            self.assertIsInstance(self.ps.get_ionice(), _ntuple.PSIONice)

        def test_get_io_counters_type(self, ):
            self.assertIsInstance(self.ps.get_io_counters(), _ntuple.PSIO)

        def test_get_rlimit_type(self, ):
            self.skipTest('Not Implemented')

        def test_get_cpu_affinity_type(self, ):
            cpu_affinity = self.ps.get_cpu_affinity()
            self.assertIsInstance(cpu_affinity, list)
            for val in cpu_affinity:
                self.assertIsInstance(val, int)

    if _sys.platform.startswith(('freebsd')):
        def test_get_io_counters_type(self, ):
            self.assertIsInstance(self.ps.get_io_counters(), _ntuple.PSIO)

    def tearDown(self):
        if self.ps.is_running():
            self.ps.terminate()

    @classmethod
    def tearDownClass(cls, ):
        cls.subproc.terminate()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_process.py ends here
