#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _japan.py 460 2015-08-10 16:51:55Z t1 $
# $Revision: 460 $
# $Date: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $

r"""_japan -- DESCRIPTION

"""
import datetime
from calendar import MONDAY, SUNDAY
from itertools import izip

from holiday.period import Period
from holiday._holiday import YearlyHoliday, YearlyWeekNthHoliday, Holiday
from holiday._holidays import Holidays
from holiday.international_name import InternationalName


class VernalEquinoxHoliday(Holiday):
    r"""VernalEquinoxHoliday

    VernalEquinoxHoliday is a Holiday.
    Responsibility:
    """
    def __init__(self, default='en'):
        r"""
        """
        Holiday.__init__(
            self, InternationalName(
                default=default, en='Vernal Equinox Day', ja=u'春分の日'))

    def is_match_date(self, date):
        r"""SUMMARY

        is_match_date(date)

        @Arguments:
        - `date`:

        @Return:

        @Error:
        """
        year = date.year
        if not 1949 < year < 2051:
            return False
        float_ = 0
        if year <= 1979:
            float_ = 20.8357
        elif year <= 2099:
            float_ = 20.8431
        elif year <= 2150:
            float_ = 21.8510
        else:
            return False
        day = int(float_ + 0.242194 * (year - 1980) - int((year - 1980) // 4))
        return date == datetime.date(year, 3, day)


class AutumnalEquinoxHoliday(Holiday):
    r"""AutumnalEquinoxHoliday

    AutumnalEquinoxHoliday is a Holiday.
    Responsibility:
    """
    def __init__(self, default='en'):
        r"""

        @Arguments:
        - `name`:
        """
        Holiday.__init__(
            self, InternationalName(
                default=default, en='Autumnal Equinox Day', ja=u'秋分の日'))

    def is_match_date(self, date):
        r"""SUMMARY

        is_match_date(date)

        @Arguments:
        - `date`:

        @Return:

        @Error:
        """
        year = date.year
        if not 1949 < year < 2051:
            return False
        float_ = 0
        if year <= 1979:
            float_ = 23.2588
        elif year <= 2099:
            float_ = 23.2488
        elif year <= 2150:
            float_ = 24.2488
        else:
            return False
        day = int(float_ + 0.242194 * (year - 1980) - int((year - 1980) // 4))
        return date == datetime.date(year, 9, day)


class JapanHolidays(Holidays):
    r"""JapanHolidays

    JapanHolidays is a Holidays.
    Responsibility:
    """
    def __init__(self, lang=None):
        r"""
        """
        Holidays.__init__(self, lang or 'ja')
        self.max = datetime.date(2050, 12, 31)
        self._substitute_name = InternationalName(default=self.default_lang,
                                                  en='Substitute Holiday',
                                                  ja=u'振替休日')
        self._national_name = InternationalName(default=self.default_lang,
                                                en='National Holiday',
                                                ja=u'国民の休日')
        # 元日 1949 ~ 2050
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(1949, 1, 1), self.max),
                          month=1, day=1,
                          name=InternationalName(default=self.default_lang,
                                                 en="New Year's Day",
                                                 ja=u'元日')))
        # 旧成人の日 1949~1999
        age = InternationalName(
            default=self.default_lang, en='Coming of Age Day', ja=u'成人の日')
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1949, 1, 1),
                       datetime.date(2000, 1, 1) - datetime.timedelta(1)),
                month=1, day=15, name=age))
        # 成人の日 2000~2050
        self._factory.add_candidate(
            YearlyWeekNthHoliday(Period(datetime.date(2000, 1, 1), self.max),
                                 month=1, weekday=MONDAY, nth=2, name=age))
        # 建国記念の日 1967~2050 ※恐らく変更はない
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(1967, 1, 1), self.max),
                          month=2, day=11,
                          name=InternationalName(default=self.default_lang,
                                                 en='National Foundation Day',
                                                 ja=u'建国記念の日')))
        # 春分の日
        self._factory.add_candidate(VernalEquinoxHoliday(self.default_lang))
        # 昭和の日
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(2007, 1, 1), self.max),
                          month=4, day=29,
                          name=InternationalName(default=self.default_lang,
                                                 en='Showa Day',
                                                 ja=u'昭和の日')))
        # 憲法記念日 ※恐らく変更はない
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(1949, 1, 1), self.max),
                          month=5, day=3,
                          name=InternationalName(default=self.default_lang,
                                                 en='Constitution Memorial Day',
                                                 ja=u'憲法記念日')))
        # みどりの日
        green = InternationalName(
            default=self.default_lang, en='Green [Greenery] Day',
            ja=u'みどりの日')
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(2007, 1, 1), self.max),
                          month=5, day=4, name=green))
        # 旧みどりの日
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1989, 1, 1),
                       datetime.date(2007, 1, 1) - datetime.timedelta(1)),
                       month=4, day=29, name=green))
        # こどもの日
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(1949, 1, 1), self.max),
                          month=5, day=5,
                          name=InternationalName(default=self.default_lang,
                                                 en="Children's Day",
                                                 ja=u'こどもの日')))
        # 海の日
        marine = InternationalName(
            default=self.default_lang, en='Marine Day', ja=u'海の日')
        self._factory.add_candidate(
            YearlyWeekNthHoliday(Period(datetime.date(2003, 1, 1), self.max),
                                 month=7, weekday=MONDAY, nth=3, name=marine))
        # 旧海の日
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1996, 1, 1),
                       datetime.date(2003, 1, 1) - datetime.timedelta(1)),
                          month=7, day=20, name=marine))
        # 山の日
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(2016, 1, 1), self.max),
                          month=8, day=11,
                          name=InternationalName(default=self.default_lang,
                                                 en='Mountain Day',
                                                 ja=u'山の日')))

        # 敬老の日
        respect_age = InternationalName(
            default=self.default_lang, en='Respect for the Aged Day',
            ja=u'敬老の日')
        self._factory.add_candidate(
            YearlyWeekNthHoliday(Period(datetime.date(2003, 1, 1), self.max),
                                 month=9, weekday=MONDAY, nth=3,
                                 name=respect_age))
        # 旧敬老の日
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1966, 1, 1),
                       datetime.date(2003, 1, 1) - datetime.timedelta(1)),
                          month=9, day=15, name=respect_age))
        # 秋分の日
        self._factory.add_candidate(AutumnalEquinoxHoliday(self.default_lang))
        # 体育の日
        sports = InternationalName(
            default=self.default_lang, en='(Health and) Sports Day',
            ja=u'体育の日')
        self._factory.add_candidate(
            YearlyWeekNthHoliday(Period(datetime.date(2000, 1, 1), self.max),
                                 month=10, weekday=MONDAY, nth=2, name=sports))
        # 旧体育の日
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1966, 1, 1),
                       datetime.date(2000, 1, 1) - datetime.timedelta(1)),
                       month=10, day=10, name=sports))
        # 文化の日
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(1948, 1, 1), self.max),
                                 month=11, day=3,
                                 name=InternationalName(
                                     default=self.default_lang,
                                     en='Culture Day',
                                     ja=u'文化の日')))
        # 勤労感謝の日
        self._factory.add_candidate(
            YearlyHoliday(Period(datetime.date(1948, 1, 1), self.max),
                                 month=11, day=23,
                                 name=InternationalName(
                                     default=self.default_lang,
                                     en='Labor Thanksgiving Day',
                                     ja=u'勤労感謝の日')))
        # 昭和天皇誕生日
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1949, 1, 1),
                       datetime.date(1989, 1, 1) - datetime.timedelta(1)),
                       month=4, day=29,
                       name=InternationalName(default=self.default_lang,
                                              en="Emperor's Birthday",
                                              ja=u'天皇誕生日')))
        # 平成天皇誕生日
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1989, 1, 1), self.max),
                       month=12, day=23,
                       name=InternationalName(default=self.default_lang,
                                              en="Emperor's Birthday",
                                              ja=u'天皇誕生日')))
        # #天皇誕生日
        # self._factory.add_candidate(
        #     YearlyHoliday(
        #         Period(datetime.date(#, 1, 1), self.max),
        #                month=2, day=23,
        #                name=InternationalName(default=self.default_lang,
        #                                       en="Emperor's Birthday",
        #                                       ja=u'天皇誕生日')))
        # 皇太子明仁親王の結婚の儀
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1959, 1, 1),
                       datetime.date(1960, 1, 1) - datetime.timedelta(1)),
                       month=4, day=10,
                       name=InternationalName(
                           default=self.default_lang,
                           en='The Rite of Wedding of HIH Crown Prince Akihito',
                           ja=u'皇太子明仁親王の結婚の儀')))
        # 昭和天皇の大喪の礼
        self._factory.add_candidate(
            YearlyHoliday(
                Period(datetime.date(1989, 1, 1),
                       datetime.date(1990, 1, 1) - datetime.timedelta(1)),
                       month=2, day=24,
                       name=InternationalName(
                           default=self.default_lang,
                           en='The Funeral Ceremony of Emperor Showa',
                           ja=u'昭和天皇の大喪の礼')))
        # 即位礼 正殿の儀
        self._factory.add_candidate(
            YearlyHoliday(
                Period(
                    datetime.date(1990, 1, 1),
                    datetime.date(1991, 1, 1) - datetime.timedelta(1)),
                    month=11, day=12,
                    name=InternationalName(
                        default=self.default_lang,
                        en='The Ceremony of the Enthronement of His Majesty the Emperor',
                        ja=u'即位礼正殿の儀')))
        # 皇太子徳仁親王の結婚の儀
        self._factory.add_candidate(
            YearlyHoliday(
                Period(
                    datetime.date(1993, 1, 1),
                    datetime.date(1994, 1, 1) - datetime.timedelta(1)),
                    month=6, day=9,
                    name=InternationalName(
                        default=self.default_lang,
                        en='The Rite of Wedding of HIH Crown Prince Naruhito',
                        ja=u'皇太子徳仁親王の結婚の儀')))

    def _substitute_holidays(self, holidays):
        r"""SUMMARY

        _substitute_holidays(holidays)

        @Arguments:
        - `holidays`:

        @Return:

        @Error:
        """
        hdays = holidays.copy()
        dates = hdays.keys()
        start = datetime.date(1973, 4, 1)
        for date in dates:
            if date < start:
                continue
            weekday = date.weekday()
            if weekday != SUNDAY:
                continue
            sub = date.replace(day=date.day + abs(weekday - 7))
            # increment 1 day if already exists holiday
            while sub in dates:
                sub = sub.replace(day=sub.day + 1)
            hdays[sub] = self._substitute_name
            dates = hdays.keys()
        return hdays

    def _national_holidays(self, holidays):
        r"""SUMMARY

        _national_holidays(holidays)

        @Arguments:
        - `holidays`:

        @Return:

        @Error:
        """
        hdays = holidays.copy()
        started = datetime.date(1985, 12, 27)
        twodays = datetime.timedelta(days=2)
        dates = hdays.keys()
        dates.sort()
        for left, right in izip(dates[:], dates[1:]):
            if right < started:
                continue
            if (right - left) != twodays:
                continue
            date = right.replace(day=right.day - 1)
            if date.weekday() == SUNDAY:
                continue
            hdays[date] = self._national_name
        return hdays

    def between_holidays(self, period):
        r"""SUMMARY

        between_holidays(period)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        holidays = super(JapanHolidays, self).between_holidays(period)
        holidays = self._substitute_holidays(holidays)
        return self._national_holidays(holidays)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _japan.py ends here
