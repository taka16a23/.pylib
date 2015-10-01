#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""international_name -- DESCRIPTION

"""


class InternationalName(object):
    r"""InternationalName

    InternationalName is a object.
    Responsibility:
    """
    languages = ['en', 'ja', ]

    def __init__(self, default=None, **kwargs):
        r"""

        @Arguments:
        - `default`:
        - `kwargs`:
        """
        self.default = default or 'en'
        self._names = dict.fromkeys(self.languages)
        for lang, name in kwargs.items():
            self.set_name(lang, name)

    # Operations
    def set_name(self, lang, name):
        """function set_name

        lang: str
        name:

        returns
        """
        if not lang in self.languages:
            # TODO: (Atami) [2015/08/10]
            raise StandardError()
        self._names[lang] = name

    def get_name(self, lang=None):
        """function get_name

        lang:

        returns
        """
        return self._names.get(lang or self.default, None) or ''

    def set_default_lang(self, lang):
        """function set_default_lang

        lang: str

        returns
        """
        self.default = lang

    def __str__(self):
        """function __str__

        returns
        """
        return self.get_name()

    def __repr__(self):
        """function __repr__

        returns
        """
        return "'{}'".format(self.get_name().encode('utf-8'))

    # TODO: (Atami) [2015/08/10]
    def __eq__(self, other):
        return other in self._names.values()

    def __ne__(self, other):
        return not self == other



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# international_name.py ends here
