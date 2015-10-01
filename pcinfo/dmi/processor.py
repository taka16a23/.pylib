#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: processor.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""processor -- DESCRIPTION

"""

import sys as _sys
import os as _os

import dmidecode
from pcinfo.dmi import parse


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 284 $'
__version__ = '0.1.0'


class DmiManufacturerFlags(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def acpi(self, ):
        r"""SUMMARY

        acpi()

        @Return:
        """
        return self._dic['ACPI (ACPI supported)']

    @property
    def apic(self, ):
        r"""SUMMARY

        apic()

        @Return:
        """
        return self._dic['APIC (On-chip APIC hardware supported)']

    @property
    def clflush(self, ):
        r"""SUMMARY

        clflush()

        @Return:
        """
        return self._dic['CLFLUSH (CLFLUSH instruction supported)']

    @property
    def cmov(self, ):
        r"""SUMMARY

        cmov()

        @Return:
        """
        return self._dic['CMOV (Conditional move instruction supported)']

    @property
    def cx8(self, ):
        r"""SUMMARY

        cx8()

        @Return:
        """
        return self._dic['CX8 (CMPXCHG8 instruction supported)']

    @property
    def de(self, ):
        r"""SUMMARY

        de()

        @Return:
        """
        return self._dic['DE (Debugging extension)']

    @property
    def ds(self, ):
        r"""SUMMARY

        ds()

        @Return:
        """
        return self._dic['DS (Debug store)']

    @property
    def fpu(self, ):
        r"""SUMMARY

        fpu()

        @Return:
        """
        return self._dic['FPU (Floating-point unit on-chip)']

    @property
    def fxsr(self, ):
        r"""SUMMARY

        fxsr()

        @Return:
        """
        return self._dic['FXSR (Fast floating-point save and restore)']

    @property
    def htt(self, ):
        r"""SUMMARY

        htt()

        @Return:
        """
        return self._dic['HTT (Hyper-threading technology)']

    @property
    def ia64(self, ):
        r"""SUMMARY

        ia64()

        @Return:
        """
        return self._dic['IA64 (IA64 capabilities)']

    @property
    def mca(self, ):
        r"""SUMMARY

        mca()

        @Return:
        """
        return self._dic['MCA (Machine check architecture)']

    @property
    def mce(self, ):
        r"""SUMMARY

        mce()

        @Return:
        """
        return self._dic['MCE (Machine check exception)']

    @property
    def mmx(self, ):
        r"""SUMMARY

        mmx()

        @Return:
        """
        return self._dic['MMX (MMX technology supported)']

    @property
    def msr(self, ):
        r"""SUMMARY

        msr()

        @Return:
        """
        return self._dic['MSR (Model specific registers)']

    @property
    def mtrr(self, ):
        r"""SUMMARY

        mtrr()

        @Return:
        """
        return self._dic['MTRR (Memory type range registers)']

    @property
    def pae(self, ):
        r"""SUMMARY

        pae()

        @Return:
        """
        return self._dic['PAE (Physical address extension)']

    @property
    def pat(self, ):
        r"""SUMMARY

        pat()

        @Return:
        """
        return self._dic['PAT (Page attribute table)']

    @property
    def pbe(self, ):
        r"""SUMMARY

        pbe()

        @Return:
        """
        return self._dic['PBE (Pending break enabled)']

    @property
    def pge(self, ):
        r"""SUMMARY

        pge()

        @Return:
        """
        return self._dic['PGE (Page global enable)']

    @property
    def pse(self, ):
        r"""SUMMARY

        pse()

        @Return:
        """
        return self._dic['PSE (Page size extension)']

    @property
    def pse_36(self, ):
        r"""SUMMARY

        pse_36()

        @Return:
        """
        return self._dic['PSE-36 (36-bit page size extension)']

    @property
    def psn(self, ):
        r"""SUMMARY

        psn()

        @Return:
        """
        return self._dic['PSN (Processor serial number present and enabled)']

    @property
    def sep(self, ):
        r"""SUMMARY

        sep()

        @Return:
        """
        return self._dic['SEP (Fast system call)']

    @property
    def ss(self, ):
        r"""SUMMARY

        ss()

        @Return:
        """
        return self._dic['SS (Self-snoop)']

    @property
    def sse(self, ):
        r"""SUMMARY

        sse()

        @Return:
        """
        return self._dic['SSE (Streaming SIMD extensions)']

    @property
    def sse2(self, ):
        r"""SUMMARY

        sse2()

        @Return:
        """
        return self._dic['SSE2 (Streaming SIMD extensions 2)']

    @property
    def tm(self, ):
        r"""SUMMARY

        tm()

        @Return:
        """
        return self._dic['TM (Thermal monitor supported)']

    @property
    def tsc(self, ):
        r"""SUMMARY

        tsc()

        @Return:
        """
        return self._dic['TSC (Time stamp counter)']

    @property
    def vme(self, ):
        r"""SUMMARY

        vme()

        @Return:
        """
        return self._dic['VME (Virtual mode extension)']


class DmiManufacturer(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def manufacturer(self, ):
        r"""SUMMARY

        manufacturer()

        @Return:
        """
        return DmiManufacturerFlags(self._dic['Manufacturer'])

    @property
    def id(self, ):
        r"""SUMMARY

        id()

        @Return:
        """
        return self._dic['ID']

    @property
    def signature(self, ):
        r"""SUMMARY

        signature()

        @Return:
        """
        return self._dic['Signature']

    @property
    def vendor(self, ):
        r"""SUMMARY

        vendor()

        @Return:
        """
        return self._dic['Intel']


class DmiProcessor(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def asset_tag(self, ):
        r"""SUMMARY

        asset_tag()

        @Return:
        """
        return self._dic['Asset Tag']

    @property
    def characteristics(self, ):
        r"""SUMMARY

        characteristics()

        @Return:
        """
        return self._dic['Characteristics']

    @property
    def core_count(self, ):
        r"""SUMMARY

        core_count()

        @Return:
        """
        return self._dic['Core Count']

    @property
    def core_enabled(self, ):
        r"""SUMMARY

        core_enabled()

        @Return:
        """
        return self._dic['Core Enabled']

    @property
    def current_speed(self, ):
        r"""SUMMARY

        current_speed()

        @Return:
        """
        return self._dic['Current Speed']

    @property
    def external_clock(self, ):
        r"""SUMMARY

        external_clock()

        @Return:
        """
        return self._dic['External Clock']

    @property
    def family(self, ):
        r"""SUMMARY

        family()

        @Return:
        """
        return self._dic['Family']

    @property
    def l1_cache_handle(self, ):
        r"""SUMMARY

        l1_cache_handle()

        @Return:
        """
        return self._dic['L1 Cache Handle']

    @property
    def l2_cache_handle(self, ):
        r"""SUMMARY

        l1_cache_handle()

        @Return:
        """
        return self._dic['L2 Cache Handle']

    @property
    def l3_cache_handle(self, ):
        r"""SUMMARY

        l1_cache_handle()

        @Return:
        """
        return self._dic['L3 Cache Handle']

    @property
    def manufacturer(self, ):
        r"""SUMMARY

        manufacturer()

        @Return:
        """
        return DmiManufacturer(self._dic['Manufacturer'])

    @property
    def max_speed(self, ):
        r"""SUMMARY

        max_speed()

        @Return:
        """
        return self._dic['Max Speed']

    @property
    def part_number(self, ):
        r"""SUMMARY

        part_number()

        @Return:
        """
        return self._dic['Part Number']

    @property
    def serial_number(self, ):
        r"""SUMMARY

        serial_number()

        @Return:
        """
        return self._dic['Serial Number']

    @property
    def socket_designation(self, ):
        r"""SUMMARY

        Socket_Designation()

        @Return:
        """
        return self._dic['Socket Designation']

    @property
    def status(self, ):
        r"""SUMMARY

        status()

        @Return:
        """
        return self._dic['Status']

    @property
    def thread_count(self, ):
        r"""SUMMARY

        thread_count()

        @Return:
        """
        return self._dic['Thread Count']

    @property
    def type(self, ):
        r"""SUMMARY

        type()

        @Return:
        """
        return self._dic['Type']

    @property
    def upgrade(self, ):
        r"""SUMMARY

        Upgrade()

        @Return:
        """
        return self._dic['Upgrade']

    @property
    def version(self, ):
        r"""SUMMARY

        version()

        @Return:
        """
        return self._dic['Version']

    @property
    def voltage(self, ):
        r"""SUMMARY

        Voltage()

        @Return:
        """
        return self._dic['Voltage']


def getprocessor():
    r"""SUMMARY

    getprocessor()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.processor()):
        yield DmiProcessor(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# processor.py ends here
