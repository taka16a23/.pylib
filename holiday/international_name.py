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
    default = 'en'

    def __init__(self, **kwargs):
        r"""

        @Arguments:
        - `default`:
        - `kwargs`:
        """
        self._names = dict.fromkeys(self.languages)
        for lang, name in kwargs.items():
            self.set_name(lang, name)

    @classmethod
    def get_default_lang(cls, ):
        r"""SUMMARY

        get_default_lang()

        @Return:

        @Error:
        """
        return cls.default

    @classmethod
    def set_default_lang(cls, lang):
        """function set_default_lang

        lang: str

        returns
        """
        if not lang in cls.languages:
            raise StandardError('{} Not supported languages. acceptable {}'
                                .format(lang, cls.languages))
        cls.default = lang

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


def set_default_lang(lang):
    r"""SUMMARY

    name()

    @Return:

    @Error:
    """
    InternationalName.set_default_lang(lang)


def get_default_lang():
    r"""SUMMARY

    name()

    @Return:

    @Error:
    """
    return InternationalName.get_default_lang()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# international_name.py ends here
