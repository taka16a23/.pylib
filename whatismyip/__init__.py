#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""
import urllib as _urllib
import random as _random
import re as _re

from ipaddress import IPv4Address

from reutil import RegexpPattern


__version__ = "0.1.1"

__all__ = ['whatismyip', ]


HOSTS = ('http://www.whatismyip.com/',
         'http://adresseip.com',
         'http://www.aboutmyip.com/',
         'http://www.ipchicken.com/',
         'http://www.showmyip.com/',
         'http://monip.net/',
         'http://checkrealip.com/',
         'http://ipcheck.rehbein.net/',
         'http://checkmyip.com/',
         'http://www.raffar.com/checkip/',
         'http://www.thisip.org/',
         'http://www.lawrencegoetz.com/programs/ipinfo/',
         'http://www.mantacore.se/whoami/',
         'http://www.edpsciences.org/htbin/ipaddress',
         'http://mwburden.com/cgi-bin/getipaddr',
         'http://checkipaddress.com/',
         'http://www.glowhost.com/support/your.ip.php',
         'http://www.tanziars.com/',
         'http://www.naumann-net.org/',
         'http://www.godwiz.com/',
         'http://checkip.eurodyndns.org/',)


def whatismyip():
    ''' Returns your public IP address.
        Output: The IP address in string format.
                None if not internet connection available.
    '''
    # List of host which return the public IP address:
    regexp = RegexpPattern.get_compile('ipv4')
    for _ in range(3):
        host = _random.choice(HOSTS)

        try:
            results = regexp.findall(_urllib.urlopen(host).read(200000))
            # assert isinstance(results, object)
            if results:
                return IPv4Address(unicode(results[0][0]))
        except:
            pass # Let's try another host
    return None


def _main():
    print(whatismyip())

if __name__ == '__main__':
    _main()




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
