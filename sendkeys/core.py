#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: core.py 189 2014-05-17 09:44:59Z t1 $
# $Revision: 189 $
# $Date: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $

r"""sendkeys -- DESCRIPTION

"""
from time import sleep
from sendkeys.display import KeymapDisplay
from sendkeys.linereplacer import LineReplacer


# class SendKeys(KeymapDisplay):
#     r"""SUMMARY
#     """

#     def __init__(self, line, display=None):
#         r"""

#         @Arguments:
#         - `line`:
#         - `display`:
#         """
#         KeymapDisplay.__init__(self, display=display)
#         self._line = line

#     def replace(self, ):
#         r"""SUMMARY

#         replace()

#         @Return:
#         """
#         return LineReplacer(self._line, self.display).replace()

#     def get_tokenize(self, ):
#         r"""SUMMARY

#         tokenize()

#         @Return:
#         """
#         return LineReplacer(self._line, self.display).get_tokenize()

#     def get_analyze(self, ):
#         r"""SUMMARY

#         getanalyze()

#         @Return:
#         """
#         return self.get_tokenize().get_analyze()

#     def sendkeys(self, window=None):
#         r"""SUMMARY

#         sendkeys()

#         @Return:
#         """
#         window = window or self.connection.root.get_active_window()
#         for exp in self.get_analyze():
#             if exp.press:
#                 exp.code.press(window=window, **exp.kwargs)
#             if exp.release:
#                 exp.code.release(window=window, **exp.kwargs)
#         self.connection.flush()

#     def __iter__(self, ):
#         return iter(self.get_analyze())

#     def __call__(self, window=None):
#         self.sendkeys(window)

#     def __repr__(self, ):
#         return "{0.__class__.__name__}('{0._line}')".format(self)


class SendKeys(KeymapDisplay):
    r"""SUMMARY
    """

    def __init__(self, line, display=None, delay=0):
        r"""

        @Arguments:
        - `line`:
        - `display`:
        """
        KeymapDisplay.__init__(self, display=display)
        self._line = line
        # TODO: (Atami) [2014/04/30]
        self.delay = delay
        self._analyzed = None

    def replace(self, ):
        r"""SUMMARY

        replace()

        @Return:
        """
        return LineReplacer(self._line, self.display).replace()

    def get_tokenize(self, ):
        r"""SUMMARY

        tokenize()

        @Return:
        """
        return LineReplacer(self._line, self.display).get_tokenize()

    def get_analyze(self, ):
        r"""SUMMARY

        getanalyze()

        @Return:
        """
        return self.get_tokenize().get_analyze()

    def sendkeys(self, window=None):
        r"""SUMMARY

        sendkeys()

        @Return:
        """
        window = window or self.connection.root.get_active_window()
        self._analyzed = self._analyzed or list(self.get_analyze())
        for exp in self._analyzed:
            if exp.press:
                exp.code.press(window=window, **exp.kwargs)
            if exp.release:
                exp.code.release(window=window, **exp.kwargs)
            if self.delay:
                sleep(self.delay)
                self.connection.flush()
        self.connection.flush()

    def __iter__(self, ):
        return iter(self.get_analyze())

    def __call__(self, window=None):
        self.sendkeys(window)

    def __repr__(self, ):
        return "{0.__class__.__name__}('{0._line}')".format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendkeys.py ends here
