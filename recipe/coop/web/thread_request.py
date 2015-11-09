#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""thred_request -- DESCRIPTION

"""


def thread_request(threads, concurrent=1):
    r"""SUMMARY

    thread_request(threads)

    @Arguments:
    - `threads`:

    @Return:

    @Error:
    """
    start, stop = 0, concurrent
    while threads[start:stop]:
        for p in threads[start:stop]:
            p.start()
        for p in threads[start:stop]:
            p.join()
        start, stop = stop, stop + concurrent



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# thred_request.py ends here
