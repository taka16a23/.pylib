#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""xsend -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from enum import IntEnum


class Behave(IntEnum):
    r"""Behave

    Behave is a I.
    Responsibility:
    """
    pressrelease = 0
    press = 1
    release = 2


class Send(object):
    """Class Send
    """
    # Attributes:
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def send(self, param):
        raise NotImplementedError()

    @abstractmethod
    def setbehave(self, behave):
        raise NotImplementedError()

    @abstractmethod
    def setmodifier(self, modifier):
        raise NotImplementedError()


class KeySend(Send):
    """Class KeySend
    """
    # Attributes:
    def __init__(self, key, behave=Behave.pressrelease):
        r"""

        @Arguments:
        - `key`:
        """
        self._key = key
        self._behave = behave

    # Operations
    def send(self, param):
        """function send

        param:

        returns
        """
        (propagate, window, sequence_number, time, child, rootx, rooty,
         eventx, eventy, state, samescreen, display) = (
            param['propagate'], param['window'], param['sequence_number'],
            param['time'], param['child'], param['rootx'], param['rooty'],
            param['eventx'], param['eventy'], param['state'],
            param['samescreen'], param['display'])
        if self._behave in (Behave.pressrelease, Behave.press):
            self._key.press(
                propagate, window, sequence_number, time, child, rootx, rooty,
                eventx, eventy, state, samescreen, display)
        if self._behave in (Behave.pressrelease, Behave.release):
            self._key.release(
                propagate, window, sequence_number, time, child, rootx, rooty,
                eventx, eventy, state, samescreen, display)

    def setbehave(self, behave):
        """function setbehave

        behave: int

        returns
        """
        self._behave = behave

    def setmodifier(self, modifier):
        """function setmodifier

        modifier:

        returns
        """
        self._key |= modifier


class ButtonSend(Send):
    """Class ButtonSend
    """
    # Attributes:
    __button = None  # ()

    # Operations
    def send(self, param):
        """function send

        param:

        returns
        """
        return None # should raise NotImplementedError()

    def setbehave(self, behave):
        """function setbehave

        behave: int

        returns
        """
        return None # should raise NotImplementedError()

    def setmodifier(self, modifier):
        """function setmodifier

        modifier:

        returns
        """
        return None # should raise NotImplementedError()


class SendRepeater(Send):
    """Class SendRepeater
    """
    # Attributes:
    def __init__(self, sender, times):
        r"""

        @Arguments:
        - `sender`:
        - `times`:
        """
        self._sender = sender
        self._times = times
    # Operations
    def send(self, param):
        """function send

        param:

        returns
        """
        for _ in range(self._times):
            self._sender.send(param)

    def setbehave(self, behave):
        """function setbehave

        behave:

        returns
        """
        self._sender.setbehave(behave)

    def setmodifier(self, modifier):
        """function setmodifier

        modifier:

        returns
        """
        self._sender.setmodifier(modifier)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xsend.py ends here
