#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_japan_holiday.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
from mocker import *
import datetime
from holiday.japan._japan import (
    JapanHolidays, VernalEquinoxHoliday, AutumnalEquinoxHoliday)
from holiday.period import Period


def get_predefined():
    r"""SUMMARY

    get_predefined()

    @Return:

    @Error:
    """
    fobj = open('japan_holidays.txt', 'rb')
    result = {}
    for line in fobj.readlines():
        dateline, name = line.split(',')
        year, month, day = dateline.split('/')
        date = datetime.date(int(year), int(month), int(day))
        name = name.replace('\n', '')
        result[date] = name.decode('utf-8')
    return result


class TestVernalEquinoxHoliday(MockerTestCase):
    """2015/08/10"""
    @classmethod
    def setUpClass(cls):
        cls.predefined = [
            x for x, name in get_predefined().items() if name == u'春分の日']
        cls.period = Period(
            datetime.date(1900, 1, 1), datetime.date(2100, 12, 31))

    def setUp(self):
        self.holidays = VernalEquinoxHoliday()
        self.mocker.replay()

    def test_is_match_date(self, ):
        for year in range(1900, 1950):
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 1, 1)))
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 12, 31)))
        for year in range(2051, 2100):
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 1, 1)))
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 12, 31)))
        for date in self.predefined:
            self.assertTrue(self.holidays.is_match_date(date))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestAutumnalEquinoxHoliday(MockerTestCase):
    """2015/08/10"""
    @classmethod
    def setUpClass(cls):
        cls.predefined = [
            x for x, name in get_predefined().items() if name == u'秋分の日']
        cls.period = Period(
            datetime.date(1900, 1, 1), datetime.date(2100, 12, 31))

    def setUp(self):
        self.holidays = AutumnalEquinoxHoliday()
        self.mocker.replay()

    def test_is_match_date(self, ):
        for year in range(1900, 1950):
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 1, 1)))
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 12, 31)))
        for year in range(2051, 2100):
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 1, 1)))
            self.assertFalse(
                self.holidays.is_match_date(datetime.date(year, 12, 31)))
        for date in self.predefined:
            self.assertTrue(self.holidays.is_match_date(date))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



class TestJapanHoliday(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.predefined = get_predefined()

    def setUp(self):
        self.holidays = JapanHolidays()
        self.mocker.replay()

    def test_between_holidays(self, ):
        generated = self.holidays.between_holidays(
            Period(datetime.date(1950, 1, 1), datetime.date(2050, 12, 31)))
        self.assertEqual(len(self.predefined), len(generated))
        for date, name in self.predefined.items():
            self.assertIn(date, generated)
            self.assertTrue(name == generated[date],
                            msg=u'{} {}'.format(name, generated[date]))
        for date, name in generated.items():
            self.assertIn(date, self.predefined)
            self.assertTrue(name == self.predefined[date])

    def test_get_next(self, ):
        next_date, next_name = self.holidays.get_next(datetime.date(2000, 1, 1))
        self.assertEqual(datetime.date(2000, 1, 10), next_date)
        self.assertEqual(u'成人の日', next_name)
        next_date2, next_name2 = self.holidays.get_next(
            datetime.date(2001, 2, 11))
        self.assertEqual(datetime.date(2001, 2, 12), next_date2)
        self.assertEqual(u'振替休日', next_name2)
        next_date3, next_name3 = self.holidays.get_next(
            datetime.date(2001, 5, 3))
        self.assertEqual(datetime.date(2001, 5, 4), next_date3)
        self.assertEqual(u'国民の休日', next_name3)

    def test_get_previous(self, ):
        prev_date, prev_name = self.holidays.get_previous(
            datetime.date(2001, 5, 4))
        self.assertEqual(datetime.date(2001, 5, 3), prev_date)
        self.assertEqual(u'憲法記念日', prev_name)

    def test_is_holiday(self, ):
        self.assertTrue(self.holidays.is_holiday(datetime.date(2000, 1, 1)))
        self.assertFalse(self.holidays.is_holiday(datetime.date(1900, 1, 1)))
        self.assertFalse(self.holidays.is_holiday(datetime.date(2000, 1, 2)))
        self.assertFalse(self.holidays.is_holiday(datetime.date(2100, 1, 1)))

    def test_substitute_holidays(self, ):
        self.skipTest('Not Implemented')

    def test_national_holidays(self, ):
        self.skipTest('Not Implemented')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_japan_holiday.py ends here
