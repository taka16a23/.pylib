#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""Name: __init__.py

This Library remote control for Sharp Aquos TV.

* SETTING
Setting target IP address and port.
Setting user name and password.

* USE
Remote controlloer try connect presetted target IP and port.
Try login.
Send each command.
Receive response.

Prevent multi command, send each command after received response.

Search hosts in internal network.

* Controllable
Power        : On, Off, Current State
Input Change : Toggle, Change TV, Change Input 1~5, Toggle Degital Network
Channel      : Change BS ch, Change CS ch, Change TS ch, Up ch, Down ch
Sellect Input: Auto, D Terminal, Composite Video?
AV Position  : Toggle, Standard, Movie, Game, AV Memory, Static Dynamic, Dynamic, PC, Photo
Volume       : Set Value
Display      : Horizon, Vertical, Clock, Clock Phase
Display Size : Toggle, Normal, SmartZoom, Wide4:3, Cinema, Full, Full1, Full2, UnderScan, Dot by Dot, Wide 16:9
Mute         : Toggle, Mute, MuteOff
Surround     : Toggle, On, Off, Auto
Audio        : Toggle
Off Timer    : Cancell, 30m, 1h, 1h30m, 2h, 2h30m


Protocol Manual: http://www.sharp.co.jp/support/aquos/doc/lc46-26v7_mn_exp.pdf


IP, port, Remote Controller, Login, Command, response, hosts,

"""

# Singleton Connection for prevent multi command.

__revision__ = "$Revision: 227 $"
__version__ = "0.1.0"

__all__ = [ ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
