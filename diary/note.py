#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""note -- DESCRIPTION

"""


class DiaryNote(object):
    """Class DiaryNote
    """
    # Attributes:
    __slots__ = ('_date', '_text')

    def __init__(self, date, text=''):
        r"""

        @Arguments:
        - `date`:
        - `text`:
        """
        self._date = date
        self._text = text

    # Operations
    def get_date(self):
        """function get_date

        returns datetime
        """
        return self._date

    date = property(get_date)

    def get_text(self):
        """function get_text

        returns str
        """
        return self._text

    text = property(get_text)

    def as_dict(self):
        """function as_dict

        returns dict
        """
        return {'date': self.date,
                'text': self.text,}

    def __gt__(self, other):
        if isinstance(other, (DiaryNote, )):
            return self.date > other.date
        return self.date > other

    def __ge__(self, other):
        if isinstance(other, (DiaryNote, )):
            return self.date >= other.date
        return self.date >= other

    def __lt__(self, other):
        if isinstance(other, (DiaryNote, )):
            return self.date < other.date
        return self.date < other

    def __le__(self, other):
        if isinstance(other, (DiaryNote, )):
            return self.date <= other.date
        return self.date <= other

    def __eq__(self, other):
        if isinstance(other, (DiaryNote, )):
            return (self.date, self.text) == (other.date, other.text)
        return (self.date, self.text) == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '{}\n{}'.format(self.date, self.text)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# note.py ends here
