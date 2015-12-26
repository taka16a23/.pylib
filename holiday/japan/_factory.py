#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_define -- DESCRIPTION

"""
from datetime import date as _date
from datetime import timedelta
from calendar import MONDAY, SUNDAY
from itertools import izip

from holiday.period import Period
from holiday.international_name import InternationalName
from holiday._holiday import YearlyHoliday, YearlyWeekNthHoliday, Holiday
from holiday._factory import HolidayFactory


# 名前の変更があればここを編集
# 基本的には追加で対処すること
SUBSTITUTE_DAY_NAME = InternationalName(en='Substitute Holiday', ja=u'振替休日')

NATIONAL_DAY_NAME = InternationalName(en='National Holiday', ja=u'国民の休日')

NEW_YEARS_DAY_NAME = InternationalName(en="New Year's Day", ja=u'元日')

COMING_OF_AGE_DAY_NAME = InternationalName(en='Coming of Age Day', ja=u'成人の日')

NATIONAL_FOUNDATION_DAY_NAME = InternationalName(
    en='National Foundation Day', ja=u'建国記念の日')

VERNAL_EQUINOX_DAY_NAME = InternationalName(en='Vernal Equinox Day', ja=u'春分の日')

SHOWA_DAY_NAME = InternationalName(en='Showa Day', ja=u'昭和の日')

CONSTITUTION_MEMORIAL_DAY_NAME = InternationalName(
    en='Constitution Memorial Day', ja=u'憲法記念日')

GREEN_DAY_NAME = InternationalName(en='Green [Greenery] Day', ja=u'みどりの日')

CHILDRENS_DAY_NAME = InternationalName(en="Children's Day", ja=u'こどもの日')

MARINE_DAY_NAME = InternationalName(en='Marine Day', ja=u'海の日')

MOUNTAIN_DAY_NAME = InternationalName(en='Mountain Day', ja=u'山の日')

RESPECT_FOR_AGED_DAY_NAME = InternationalName(
    en='Respect for the Aged Day', ja=u'敬老の日')

AUTUMNAL_EQUINOX_DAY_NAME = InternationalName(en='Autumnal Equinox Day', ja=u'秋分の日')

SPORTS_DAY_NAME = InternationalName(en='(Health and) Sports Day', ja=u'体育の日')

CULTURE_DAY_NAME = InternationalName(en='Culture Day', ja=u'文化の日')

LABOR_THANKSGIVING_DAY_NAME = InternationalName(
    en='Labor Thanksgiving Day', ja=u'勤労感謝の日')

SHOWA_EMPERORS_BIRTHDAY_DAY_NAME = InternationalName(
    en="Emperor's Birthday", ja=u'天皇誕生日')

HEISEI_EMPERORS_BIRTHDAY_DAY_NAME = InternationalName(
    en="Emperor's Birthday", ja=u'天皇誕生日')

THE_RITE_OF_WEDDING_OF_HIH_CROWN_PRINCE_AKIHITO = InternationalName(
    en='The Rite of Wedding of HIH Crown Prince Akihito',
    ja=u'皇太子明仁親王の結婚の儀')

THE_FUNERAL_CEREMONY_OF_EMPEROR_SHOWA = InternationalName(
    en='The Funeral Ceremony of Emperor Showa', ja=u'昭和天皇の大喪の礼')

THE_CEREMONY_OF_THE_ENTHRONEMENT_OF_HIS_MAJESTY_THE_EMPEROR = InternationalName(
    en='The Ceremony of the Enthronement of His Majesty the Emperor',
    ja=u'即位礼正殿の儀')

THE_RITE_OF_WEDDING_OF_HIH_CROWN_PRINCE_NARUHITO = InternationalName(
    en='The Rite of Wedding of HIH Crown Prince Naruhito',
    ja=u'皇太子徳仁親王の結婚の儀')

########


class VernalEquinoxHoliday(Holiday):
    r"""VernalEquinoxHoliday

    VernalEquinoxHoliday is a Holiday.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        Holiday.__init__(self, VERNAL_EQUINOX_DAY_NAME)

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
        return date == _date(year, 3, day)


class AutumnalEquinoxHoliday(Holiday):
    r"""AutumnalEquinoxHoliday

    AutumnalEquinoxHoliday is a Holiday.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `name`:
        """
        Holiday.__init__(self, AUTUMNAL_EQUINOX_DAY_NAME)

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
        return date == _date(year, 9, day)


class JapaneseHolidayFactory(HolidayFactory):
    r"""JapaneseHolidayFactory

    JapaneseHolidayFactory is a HolidayFactory.
    Responsibility:
    """

    def __init__(self, ):
        r"""
        """
        HolidayFactory.__init__(self, )
        max_date = _date(2050, 12, 31)
        ## 不変なもの ##
        # 旧成人の日 1949~1999 1月15日
        self.add_candidate(
            YearlyHoliday(Period(_date(1949, 1, 1),
                                 _date(2000, 1, 1) - timedelta(1)),
                          month=1, day=15, name=COMING_OF_AGE_DAY_NAME))
        # 旧みどりの日
        self.add_candidate(
            YearlyHoliday(Period(_date(1989, 1, 1),
                                 _date(2007, 1, 1) - timedelta(1)),
                          month=4, day=29, name=GREEN_DAY_NAME))
        # 旧海の日
        self.add_candidate(
            YearlyHoliday(Period(_date(1996, 1, 1),
                                 _date(2003, 1, 1) - timedelta(1)),
                          month=7, day=20, name=MARINE_DAY_NAME))
        # 旧敬老の日
        self.add_candidate(
            YearlyHoliday(Period(_date(1966, 1, 1),
                                 _date(2003, 1, 1) - timedelta(1)),
                          month=9, day=15, name=RESPECT_FOR_AGED_DAY_NAME))
        # 旧体育の日
        self.add_candidate(
            YearlyHoliday(Period(_date(1966, 1, 1),
                                 _date(2000, 1, 1) - timedelta(1)),
                          month=10, day=10, name=SPORTS_DAY_NAME))
        # 昭和天皇誕生日
        self.add_candidate(
            YearlyHoliday(Period(_date(1949, 1, 1),
                                 _date(1989, 1, 1) - timedelta(1)),
                          month=4, day=29,
                          name=SHOWA_EMPERORS_BIRTHDAY_DAY_NAME))
        # 皇太子明仁親王の結婚の儀
        self.add_candidate(
            YearlyHoliday(Period(_date(1959, 1, 1),
                                 _date(1960, 1, 1) - timedelta(1)),
                          month=4, day=10,
                          name=THE_RITE_OF_WEDDING_OF_HIH_CROWN_PRINCE_AKIHITO))
        # 昭和天皇の大喪の礼
        self.add_candidate(
            YearlyHoliday(
                Period(_date(1989, 1, 1),
                       _date(1990, 1, 1) - timedelta(1)),
                       month=2, day=24,
                       name=THE_FUNERAL_CEREMONY_OF_EMPEROR_SHOWA))
        # 即位礼 正殿の儀
        self.add_candidate(
            YearlyHoliday(Period(_date(1990, 1, 1),
                                 _date(1991, 1, 1) - timedelta(1)),
                          month=11, day=12,
                          name= THE_CEREMONY_OF_THE_ENTHRONEMENT_OF_HIS_MAJESTY_THE_EMPEROR))
        # 皇太子徳仁親王の結婚の儀
        self.add_candidate(
            YearlyHoliday(Period(_date(1993, 1, 1),
                                 _date(1994, 1, 1) - timedelta(1)),
                          month=6, day=9,
                          name=THE_RITE_OF_WEDDING_OF_HIH_CROWN_PRINCE_NARUHITO))

        ## 変更のなさそうなもの ##
        # 建国記念の日 1967~2050 2月11日 ※恐らく変更はない
        self.add_candidate(
            YearlyHoliday(Period(_date(1967, 1, 1), max_date),
                          month=2, day=11, name=NATIONAL_FOUNDATION_DAY_NAME))
        # 憲法記念日 5月3日 ※恐らく変更はない
        self.add_candidate(
            YearlyHoliday(Period(_date(1949, 1, 1), max_date),
                          month=5, day=3, name=CONSTITUTION_MEMORIAL_DAY_NAME))

        ## 変更がありそうなもの ##
        # 元日 1949 ~ 2050 1月1日
        self.add_candidate(
            YearlyHoliday(Period(_date(1949, 1, 1), max_date),
                          month=1, day=1, name=NEW_YEARS_DAY_NAME))
        # 成人の日 2000~2050 1月第二月曜日
        self.add_candidate(
            YearlyWeekNthHoliday(Period(_date(2000, 1, 1), max_date),
                                 month=1, weekday=MONDAY, nth=2,
                                 name=COMING_OF_AGE_DAY_NAME))
        # 春分の日
        self.add_candidate(VernalEquinoxHoliday())
        # 昭和の日 4月29日
        self.add_candidate(
            YearlyHoliday(Period(_date(2007, 1, 1), max_date),
                          month=4, day=29, name=SHOWA_DAY_NAME))
        # みどりの日 5月4日
        self.add_candidate(
            YearlyHoliday(Period(_date(2007, 1, 1), max_date),
                          month=5, day=4, name=GREEN_DAY_NAME))
        # こどもの日 5月5日
        self.add_candidate(
            YearlyHoliday(Period(_date(1949, 1, 1), max_date),
                          month=5, day=5, name=CHILDRENS_DAY_NAME))
        # 海の日
        self.add_candidate(
            YearlyWeekNthHoliday(Period(_date(2003, 1, 1), max_date),
                                 month=7, weekday=MONDAY, nth=3,
                                 name=MARINE_DAY_NAME))
        # 山の日
        self.add_candidate(
            YearlyHoliday(Period(_date(2016, 1, 1), max_date),
                          month=8, day=11,
                          name=MOUNTAIN_DAY_NAME))
        # 敬老の日
        self.add_candidate(
            YearlyWeekNthHoliday(Period(_date(2003, 1, 1), max_date),
                                 month=9, weekday=MONDAY, nth=3,
                                 name=RESPECT_FOR_AGED_DAY_NAME))
        # 秋分の日
        self.add_candidate(AutumnalEquinoxHoliday())
        # 体育の日
        self.add_candidate(
            YearlyWeekNthHoliday(Period(_date(2000, 1, 1), max_date),
                                 month=10, weekday=MONDAY, nth=2,
                                 name=SPORTS_DAY_NAME))
        # 文化の日
        self.add_candidate(
            YearlyHoliday(Period(_date(1948, 1, 1), max_date),
                                 month=11, day=3,
                                 name=CULTURE_DAY_NAME))
        # 勤労感謝の日
        self.add_candidate(
            YearlyHoliday(Period(_date(1948, 1, 1), max_date),
                                 month=11, day=23,
                                 name=LABOR_THANKSGIVING_DAY_NAME))
        # 平成天皇誕生日
        self.add_candidate(
            YearlyHoliday(Period(_date(1989, 1, 1), max_date),
                          month=12, day=23,
                          name=HEISEI_EMPERORS_BIRTHDAY_DAY_NAME))
        ## 追加予定 ##
        # #　　天皇誕生日
        # self.add_candidate(
        #     YearlyHoliday(
        #         Period(_date(#, 1, 1), max_date),
        #                month=2, day=23,
        #                name=InternationalName(default=self.default_lang,
        #                                       en="Emperor's Birthday",
        #                                       ja=u'天皇誕生日')))

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
        start = _date(1973, 4, 1)
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
            hdays[sub] = SUBSTITUTE_DAY_NAME
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
        started = _date(1985, 12, 27)
        twodays = timedelta(days=2)
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
            hdays[date] = NATIONAL_DAY_NAME
        return hdays

    def between_holidays(self, period):
        r"""SUMMARY

        between_holidays(period)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        holidays = super(JapaneseHolidayFactory, self).between_holidays(period)
        holidays = self._substitute_holidays(holidays)
        return self._national_holidays(holidays)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _define.py ends here
