#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" async -- asynchronous decorator


"""

import sys as _sys
import itertools as _itertools

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


def on_success(result): # default implementation
    "Called on the result of the function"
    return result
def on_failure(exc_info): # default implementation
    "Called if the function fails"
    pass
def on_closing(): # default implementation
    "Called at the end, both in case of success and failure"
    pass
class Async(object):
    """
    A decorator converting blocking functions into asynchronous
    functions, by using threads or processes. Examples:

    async_with_threads =  Async(threading.Thread)
    async_with_processes =  Async(multiprocessing.Process)
    """

    def __init__(self, threadfactory, on_success=on_success,
                 on_failure=on_failure, on_closing=on_closing):
        self.threadfactory = threadfactory
        self.on_success = on_success
        self.on_failure = on_failure
        self.on_closing = on_closing

    def __call__(self, func, *args, **kw):
        try:
            counter = func.counter
        except AttributeError: # instantiate the counter at the first call
            counter = func.counter = _itertools.count(1)
        name = '%s-%s' % (func.__name__, counter.next())
        def func_wrapper():
            try:
                result = func(*args, **kw)
            except:
                self.on_failure(_sys.exc_info())
            else:
                return self.on_success(result)
            finally:
                self.on_closing()
        thread = self.threadfactory(None, func_wrapper, name)
        thread.start()
        return thread



# http://code.activestate.com/recipes/576684-simple-threading-decorator/
def async2(func):
    """
        run_async(func)
            function decorator, intended to make "func" run in a separate
            thread (asynchronously).
            Returns the created Thread object

            E.g.:
            @run_async
            def task1():
                do_something

            @run_async
            def task2():
                do_something_too

            t1 = task1()
            t2 = task2()
            ...
            t1.join()
            t2.join()
    """
    from multiprocessing import Process
    from functools import wraps
    # from threading import Thread

    @wraps(func)
    def async_func(*args, **kwargs):
        # func_hl = Thread(target = func, args = args, kwargs = kwargs)
        func_hl = Process(target = func, args = args, kwargs = kwargs)
        func_hl.start()
        return func_hl

    return async_func


# https://wiki.python.org/moin/PythonDecoratorLibrary#Asynchronous_Call
from Queue import Queue
from threading import Thread

class asynchronous(object):
    def __init__(self, func):
        self.func = func

        def threaded(*args, **kwargs):
            self.queue.put(self.func(*args, **kwargs))

        self.threaded = threaded

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def start(self, *args, **kwargs):
        self.queue = Queue()
        thread = Thread(target=self.threaded, args=args, kwargs=kwargs);
        thread.start();
        return asynchronous.Result(self.queue, thread)

    class NotYetDoneException(Exception):
        def __init__(self, message):
            self.message = message

    class Result(object):
        def __init__(self, queue, thread):
            self.queue = queue
            self.thread = thread

        def is_done(self):
            return not self.thread.is_alive()

        def get_result(self):
            if not self.is_done():
                raise asynchronous.NotYetDoneException('the call has not yet completed its task')

            if not hasattr(self, 'result'):
                self.result = self.queue.get()

            return self.result


if __name__ == '__main__':
    # sample usage
    import time

    @asynchronous
    def long_process(num):
        time.sleep(10)
        return num * num

    fmt = 'result {0}'.format
    result = long_process.start(12)
    for i in range(20):
        print i
        time.sleep(1)
        if result.is_done():
            print fmt(result.get_result())


    result2 = long_process.start(13)

    try:
        print "result2 {0}".format(result2.get_result())

    except asynchronous.NotYetDoneException as ex:
        print ex.message


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    from time import sleep

    @async2
    def print_somedata():
        print 'starting print_somedata'
        sleep(2)
        print 'print_somedata: 2 sec passed'
        sleep(2)
        print 'print_somedata: 2 sec passed'
        sleep(2)
        print 'finished print_somedata'

    def main():
        print_somedata()
        print 'back in main'
        print_somedata()
        print 'back in main'
        print_somedata()
        print 'back in main'

    main()
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# async.py ends here
